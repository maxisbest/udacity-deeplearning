# Datasets

In Machine Learning there are many famous datasets, some of them have been used in this Udacity Nanodegree:

## MNIST
- MNIST is the dataset of handwritten digits
- it is avalable in Tensorflow:
```
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets('MNIST_data', one_hot=True)
```
