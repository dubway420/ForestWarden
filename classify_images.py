from tensorflow.keras.applications.resnet50 import ResNet50
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions
import numpy as np
import os


def classify_image(img_path, model):

    _, image_name = os.path.split(img_path)
    print(f"\nAnalysising image: {image_name} \n")

    img = image.load_img(img_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)

    preds = model.predict(x)
    # decode the results into a list of tuples (class, description, probability)
    # (one such list for each sample in the batch)

    predictions = decode_predictions(preds, top=5)[0]

    print("\nThe top predictions for this image are as follows: \n")

    for i, (_, category, certainty) in enumerate(predictions):

        # get a percentage certainty for this image
        percentage = round(certainty * 100, 1)

        # if the percentage is less than 1%, disregard
        if percentage > 1:
            print(str(i+1) + ".", category, "-", str(percentage) + "%")


    print("\n --------------------------------- \n")


def list_of_images(directory):

    image_paths = []

    """Given a directory, will list all images contained within, including path."""

    img_extensions = [".png", ".jpg", ".jpeg"]

    for filename in os.listdir(directory):

        _, file_extension = os.path.splitext(filename)
        if file_extension in img_extensions:
           image_paths.append(os.path.join(directory, filename))

    return image_paths


# --------------- The Model ----------------------------------
# We are importing a built-in image classifer called ResNet50
# You can see the full list of models you can chose from here:
# https://keras.io/api/applications/

# As you can see, we are using the built-in weights that were
# optimised for the imagenet challenge. That is, the model was
# trained to identify the contents of images as one of 1000
# categories. You can see the full list here
# https://gist.github.com/yrevar/942d3a0ac09ec9e5eb3a
model = ResNet50(weights='imagenet')

# ------------------------------------------------------------

folder = "images"

images = list_of_images(folder)

for image_to_classify in images:
    classify_image(image_to_classify, model)