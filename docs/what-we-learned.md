# what we learned
Overview about what we learned:

## Introduction
As an introduction we were given some examples of what deep learning is capable of: 
1. Transfering an artist's styles to your own fotographs: [-> Fast Style Transfer](https://github.com/lengstrom/fast-style-transfer)
2. Learning to steer a car: [-> Deep Traffic](https://selfdrivingcars.mit.edu/deeptraffic/)
3. Learning to play flappybird: [-> DeepLearningFlappyBird](https://github.com/yenchenlin/DeepLearningFlappyBird)

### Literature
Here you can find some of the books and articles that got recommended to us during the course:
- [Literature on Deep Learning](literature.md)

### Tools
These tools were introduced to us in the course
- [Anaconda](anaconda.md)
- [Jupyter Notebooks](jupyter_notebooks.md)
- [Numpy](numpy.md)

## Neural Networks

## Convolutional Networks
## Project2: Dog breed recognising app build with a pretrained CNN
In this project we used pretrained CNNs to build an app that could distinguish dogs and humans and predict the breed for dogs. 
[Link to the project repo](https://github.com/sabinem/udacity-deeplearning-dog-project)

## Recurrent Networks
## Project3: Generate a TV script with an RNN
In this projects an RNN predicted the next word. It was trained on TV scripts of the Simpsons.
It uses LSTMs
[Link to the project directory](RNNs/tv_script_rnn)

## Generative Adversarial Networks

### GANs with MNIST
GANs are Generative Adverserial Networks. In these networks two players: a discriminator and a generator are trained in parallel with opposite goals: the generator wants to produce fakes, that go through as real and the discrimnator wants to detect fakes and reject them. The overall goal is to improve both player, where the focus might be on either of them. 

## Exercise 1: MNIST with a GAN
In this exercise a Gan was build to create fake handwritten digits:
- this is a small project, that does not take much time to train and you can none the less watch how a GAN works and trains
[Link to the project directory](GANs/gan_mnist)

### Batchnormalization
batch normalization can make NN training a lot more robust for deep networks 
- lesson that compares training with and without batch normalization: [html](Batch_Normalization_Lesson.html) / [notebook](https://github.com/sabinem/udacity_DL/blob/master/batch_normalization/README.md)

## Deep Reinforcement Learning

This repo summarizes what I have learned in the Udacity Deep Learning Nanodegree. The index includes links to the many exercises and projects that were part of this program.
