from tools.deepfake_reco import data_generation, define_model, train, classify, format_predictions
import yaml


def pipeline():
    """
    Full pipeline of training and classifying
    """
    with open('/home/jovyan/group4-deepfakes-detection/config.yaml', 'rb') as f:
        conf = yaml.safe_load(f.read())

    image_size = tuple(conf.get('IMAGE_SIZE'))
    batch_size = conf.get('BATCH_SIZE')
    n_epochs = conf.get('N_EPOCHS')
    train_test_path = conf.get('TRAIN_TEST_PATH')
    eval_path = conf.get('EVAL_PATH')
    eval_id_path = conf.get('EVAL_ID_PATH')

    # Pipeline start
    # Dataset
    train_ds, test_ds, eval_ds = data_generation(image_size, batch_size, train_test_path, eval_path)

    # Model
    model = define_model(image_size)
    trained_model = train(model, train_ds, test_ds, n_epochs)

    # Predict
    predictions_proba = classify(trained_model, eval_ds)
    final_predictions = format_predictions(predictions_proba, eval_id_path)
    # Save
    final_predictions.to_csv('/home/jovyan/group4-deepfakes-detection/results/results.csv', index=False, header=True)
    return


if __name__ == "__main__":
    pipeline()
