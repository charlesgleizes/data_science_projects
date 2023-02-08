import pandas as pd
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers


def data_generation(
    image_size: tuple,
    batch_size: int,
    train_test_path: str,
    valid_path: str,
):
    """
    Generate the train, test and  validation datasets.
    :output: train, test and validation BatchDatasets
    """
    train_ds = tf.keras.preprocessing.image_dataset_from_directory(
        train_test_path,
        validation_split=0.2,
        subset="training",
        seed=1337,
        image_size=image_size,
        batch_size=batch_size
    )

    test_ds = tf.keras.preprocessing.image_dataset_from_directory(
        train_test_path,
        validation_split=0.2,
        subset="validation",
        seed=1337,
        image_size=image_size,
        batch_size=batch_size
    )

    val_ds = tf.keras.preprocessing.image_dataset_from_directory(
        valid_path,
        seed=1337,
        image_size=image_size,
        batch_size=batch_size,
    )

    train_ds = train_ds.prefetch(buffer_size=32)
    test_ds = test_ds.prefetch(buffer_size=32)
    val_ds = val_ds.prefetch(buffer_size=32)

    return train_ds, test_ds, val_ds


def make_model(input_shape: tuple):
    """
    Define the neural network for classification
    """
    inputs = keras.Input(shape=input_shape)
    # Image augmentation block
    data_augmentation = keras.Sequential(
        [
            layers.RandomFlip("horizontal"),
            layers.RandomRotation(0.1),
        ]
    )
    x = data_augmentation(inputs)

    # Entry block
    x = layers.Rescaling(1.0 / 255)(x)
    x = layers.Conv2D(32, 3, strides=2, padding="same")(x)
    x = layers.BatchNormalization()(x)
    x = layers.Activation("relu")(x)

    x = layers.Conv2D(64, 3, padding="same")(x)
    x = layers.BatchNormalization()(x)
    x = layers.Activation("relu")(x)

    previous_block_activation = x  # Set aside residual

    for size in [128, 256, 512, 728]:
        x = layers.Activation("relu")(x)
        x = layers.SeparableConv2D(size, 3, padding="same")(x)
        x = layers.BatchNormalization()(x)

        x = layers.Activation("relu")(x)
        x = layers.SeparableConv2D(size, 3, padding="same")(x)
        x = layers.BatchNormalization()(x)

        x = layers.MaxPooling2D(3, strides=2, padding="same")(x)

        # Project residual
        residual = layers.Conv2D(size, 1, strides=2, padding="same")(
            previous_block_activation
        )
        x = layers.add([x, residual])  # Add back residual
        previous_block_activation = x  # Set aside next residual

    x = layers.SeparableConv2D(1024, 3, padding="same")(x)
    x = layers.BatchNormalization()(x)
    x = layers.Activation("relu")(x)

    x = layers.GlobalAveragePooling2D()(x)

    activation = "sigmoid"
    units = 1

    x = layers.Dropout(0.5)(x)
    outputs = layers.Dense(units, activation=activation)(x)

    return keras.Model(inputs, outputs)


def define_model(image_size: tuple):
    """
    Defining and compiling the model
    :input: image size
    :output: compiled model
    """
    model = make_model(input_shape=image_size + (3,))
    model.compile(
        optimizer=keras.optimizers.Adam(1e-3),
        loss="binary_crossentropy",
        metrics=["accuracy"],
    )
    return model


def train(model, train_ds, test_ds, epochs: int = 2):
    """
    Train the model
    """
    model.fit(train_ds,
              epochs=epochs,
              validation_data=test_ds)
    return model


def classify(trained_model, eval_set):
    """
    Classify the images of the dataset into fake or real
    :input:
        trained model
        BatchedDataset of images

    :output: array of scores between 0 and 1 fro each image
    """
    predictions_proba = trained_model.predict(eval_set)
    return predictions_proba


def format_predictions(predictions, eval_id_path):
    """
    Format predictions for hfactory evaluation
    """
    eval_id = pd.read_csv(eval_id_path)
    final_predictions = pd.concat([eval_id.image_id,
                                   pd.DataFrame((predictions > .5) * 1)],
                                  axis=1)
    final_predictions = final_predictions.rename(columns={0: "label"})

    return final_predictions
