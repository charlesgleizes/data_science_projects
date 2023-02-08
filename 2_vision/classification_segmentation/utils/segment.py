import tensorflow as tf

def segment_silo(file_bytes, model):
    '''
    Detects the probability that the pictures have a silo in them or not.
    Args
        list_input_image_path = list(str) : list of the path of the pictures (png)
        model : trained tensorflow model
    Returns
        prediction = np.array(proba) : array of the probabilities that each picture contains a silo.
    '''
    #### Parameters ####
    CHANNELS = 3
    IMG_SIZE = 256
    #####################

    # Image preprocessing
    def parse(image_bytes):
        img = tf.image.decode_jpeg(image_bytes,channels=CHANNELS)
        img = tf.cast(img, tf.float32)
        img/=255.0
        img = tf.image.resize(img, (IMG_SIZE, IMG_SIZE))
        img = tf.expand_dims(img, axis=0)
        return img

    dataset = parse(file_bytes)
    prediction = model.predict(dataset)
    
    return prediction

# Example of usage:
#input_image_path1 = 'images_classified/not_silos/silos_256-0-0--6-14-1247-31272.png'
#input_image_path2 = 'images_classified/not_silos/silos_256-0-0--6-14-1281-31369.png'
#pred = classif_silo([input_image_path1, input_image_path2], model)