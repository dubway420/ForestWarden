from dataset_generation import dataset_generator
from classify_images import model

features, labels = dataset_generator(model.input_shape[1:3], "image_data/forest_fire_from_above", "image_data/forest_from_above")

print("\n\n")
print("The length of the features array is", len(features))
print("The length of the labels array is", len(labels))
print("\n\n")

print(labels)
print(features[0].shape)
