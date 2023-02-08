from tools.deepfake_reco import data_generation, define_model, train, classify, format_predictions
import yaml
import pandas as pd

with open('/builds/unit-test-group4/group4-deepfakes-detection/config.yaml', 'rb') as f:
    conf = yaml.safe_load(f.read())

image_size = tuple(conf.get('IMAGE_SIZE'))
batch_size = conf.get('BATCH_SIZE')
n_epochs = conf.get('N_EPOCHS')
train_test_path = conf.get('TEST_DATA_PATH')
eval_path = conf.get('TEST_DATA_PATH')
eval_id_path = conf.get('TEST_EVAL_ID_PATH')

train_ds, test_ds, eval_ds = data_generation(image_size, batch_size, train_test_path, eval_path)

def test_data_generation(train_ds=train_ds, test_ds=test_ds, eval_ds=eval_ds):
    """
    Tests data_generation function.
    """
    assert [len(ds) > 0 for ds in [train_ds, test_ds, eval_ds]]

model = define_model(image_size)

def test_define_model(model=model):
    """
    Tests define_model and make_model functions.
    """
    assert (len(model.layers) > 0) & (model._is_compiled)

train_ds = train_ds.take(1)
test_ds = test_ds.take(1)
eval_ds = eval_ds.take(1)
trained_model = train(model, train_ds, test_ds, n_epochs)

def test_train(trained_model=trained_model):
    """
    Tests train function.
    """
    assert trained_model.train_function is not None

def test_classify(trained_model=trained_model, eval_ds=eval_ds):
    """
    Tests classify function.
    """
    predictions_proba = classify(trained_model, eval_ds)
    assert all([0 <= output <= 1 for output in predictions_proba])

predictions_proba = classify(trained_model, eval_ds)

def test_format_predictions(predictions_proba=predictions_proba, eval_id_path=eval_id_path):
    """
    Tests format_predictions function.
    """
    final_predictions = format_predictions(predictions_proba, eval_id_path)
    assert final_predictions.shape == (len(predictions_proba), 2)
