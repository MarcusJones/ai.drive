'''
Created on Mar 8, 2018

@author: batman
'''
import keras as ks
import logging
import keras.preprocessing.image


def get_test_generator_sample(directory,batch_size):
    test_datagen_sample = ks.preprocessing.image.ImageDataGenerator(rescale=1. / 255)
    #print(path_test)
    test_generator = test_datagen_sample.flow_from_directory(
            directory,
            target_size = (150,150),
            batch_size = 8,
            #class_mode = "binary",
        );
    return(test_generator)





def get_test_generator(directory,batch_size):
    test_datagen = ks.preprocessing.image.ImageDataGenerator(rescale=1. / 255)

    test_generator = test_datagen.flow_from_directory(
        directory,
        target_size = (150,150),
        batch_size = batch_size,
        class_mode = "binary",
        shuffle=False,
    );
    
    return(test_generator)
    
    
def get_train_generator_aug(directory,batch_size):
    # Training generator - Augmentation
    train_datagen = ks.preprocessing.image.ImageDataGenerator(rescale=1/255,
                                                  rotation_range = 40,
                                                  width_shift_range = 0.2,
                                                  height_shift_range = 0.2,
                                                  shear_range = 0.2,
                                                  zoom_range= 0.2,
                                                  horizontal_flip=True)
    
    train_generator = train_datagen.flow_from_directory(
        directory,
        target_size = (150,150),
        batch_size = batch_size,
        class_mode = "binary",
    );
    
    logging.info("Training with augmentation: {} files over {} classes, resized to {}".format(
        len(train_generator.filenames),
        train_generator.num_classes,
        train_generator.target_size,
        ))

    return train_generator

def get_validation_generator(directory,batch_size):
    # Validation images
    validation_datagen = ks.preprocessing.image.ImageDataGenerator(rescale=1/255)
    validation_generator = validation_datagen.flow_from_directory(
        directory,
        target_size = (150,150),
        batch_size = batch_size,
        class_mode = "binary",
    )
    
    logging.info("Validation: {} files over {} classes, resized to {}".format(
        len(validation_generator.filenames),
        validation_generator.num_classes,
        validation_generator.target_size,
        ))
    
    return validation_generator

def get_train_generator_simple(directory,batch_size):
    train_datagen = ks.preprocessing.image.ImageDataGenerator(rescale=1/255)
    # Training images
    
    train_generator = train_datagen.flow_from_directory(
        directory,
        target_size = (150,150),
        batch_size = batch_size,
        class_mode = "binary",
    );
    
    logging.info("Training: {} files over {} classes, resized to {}".format(
        len(train_generator.filenames),
        train_generator.num_classes,
        train_generator.target_size,
        ))

    return train_generator



if __name__ == '__main__':
    pass
