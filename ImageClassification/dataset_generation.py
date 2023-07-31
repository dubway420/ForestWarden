import os
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import preprocess_input
import numpy as np

def list_of_images(directory):

    image_paths = []

    """Given a directory, will convert all images contained within to a useable format for ML."""

    img_extensions = [".png", ".jpg", ".jpeg"]
    

    for filename in os.listdir(directory):

        _, file_extension = os.path.splitext(filename)
        if file_extension in img_extensions:
           image_paths.append(os.path.join(directory, filename))

    return image_paths

def convert_image(img_path, img_dims_req):

    img = image.load_img(img_path, target_size=img_dims_req)
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    
    return x

def dataset_generator(dims, *args):

    features = []
    labels = []

    dims_verified = []

    # if the user has specified only an integer as the dimensions, they might have specified the 
    # second dimension as the second argument
    if type(dims) == int:

        dims_verified.append(dims)

        # if the first *arg is an integer
        if type(args[0]) == int:

            # set the second dim to this integer
            dims_verified.append(args[0])

            # remove it from the list to check for data
            args = args[1:]

        # otherwise, just use the same number again
        else:
            dims_verified.append(dims)    

    else:
        dims_verified = dims

    # make sure it is a tuple
    dims_verified = tuple(dims_verified)


    # If the user has specified a list as a single argument, then assume each item
    # in that list is a path to a folder of images
    if len(args) == 1:
        args = args[0]


    # this is for if there is a single folder passed as argument
    # makes the single str an iterable
    if type(args) == str:
        args = [args] 
    
    # Each arg should be the path to a folder containing images of a single category
    for i, img_folder_path in enumerate(args):
        
        # # This gets the path of all the images in the folder
        img_path_list = list_of_images(img_folder_path) 

        for image_path in img_path_list:
            
            try:
                converted_image = convert_image(image_path, dims_verified)
                features.append(converted_image)
                labels.append(float(i))

            except:
                print(f"Error converting image {image_path}. Ignoring this instance and moving on...")

    return features, labels
    


        



      