# Tutorial from: https://www.tensorflow.org/tutorials/keras/classification#import_the_fashion_mnist_dataset
import tensorflow as tf
from tensorflow import keras    # high level API

# Helper Libraries
import numpy as np
import matplotlib.pyplot as plt

# load dataset
data = keras.datasets.fashion_mnist