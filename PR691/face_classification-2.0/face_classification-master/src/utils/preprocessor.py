import numpy as np
import imageio
from skimage.transform import resize

def preprocess_input(image, target_size=None):
    if target_size is not None and target_size != True:
        image = resize(image, target_size)
    image = image.astype('float32')
    image /= 255.0
    return image
