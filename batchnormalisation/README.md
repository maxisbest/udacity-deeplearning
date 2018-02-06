# Batchnormalisation

## What is batch normalization?
A neuronal network is usually trained with batches that are formes from the data itself.
Normally the data is just partitioned into batches. The method in how that is done may vary, such as with RNNs,
but the data itself is not changed, when batches are formed.

**With batch normalization the batch data itself is normalized!**

## When is batch normalization used?
It is used for networks with many layers.

## What problem does it solve?
A neural network is usually very sensible to:
- Hyperparameters such as the learning rate
- the starting values that you use
- normalization of input features


