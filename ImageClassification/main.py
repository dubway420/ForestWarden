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




    else:
        dims_verified = dims

    # make sure it is a tuple
    dims_verified = tuple(dims_verified)

    # If the user has specified a list as a single argument, then assume each item
    # in that list is a path to a folder of images
    if len(args) == 1:
        args = args[0]

    # Each arg should be the path to a folder containing images of a single category
    for i, img_folder_path in enumerate(args):
        print(float(i), img_folder_path)


    print(dims_verified)


dataset_generator((224, 224), ["hello", "google"])