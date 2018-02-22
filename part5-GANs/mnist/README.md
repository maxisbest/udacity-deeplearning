# MNIST is good for everything, even as an example for GANs
MNIST have become the "Hello world" of machine learning. Almost everything you do there can be first study with MNIST. The same is true for GANs!

## MINIST for GANs
GANS are "generative adversial networks", so applied to MNIST this means:
- build a generator, that starts with noise and turns this into 784 black and white pixels (the input for MNIST)
- build a discriminator, that takes 784 black and white pixel images and return a probability for them to be real or fake
- train them both in parallel
- see how they both get better

## GANS are easy to understand but hard to train
The competition between generator and discriminator in Gans is easy to understand:

Both have a goals amd their goals are opposite to each other: 
- the genrator tries to produce fakes, that the discriminator takes for real
- the discriminator, does not want the generator to succeed

