[//]: # (Image References)

[image1]: ./myfiles/tsneplots/HumanDogResNet50TSNE.png "TSNE for ResNet50 Features for Human Dog Detection"
[image2]: ./myfiles/tsneplots/DogBreedsVGG19TSNE.png "TSNE for VGG19 Features for Dog Breed Detection"
[image3]: ./myfiles/tsneplots/DogBreedsResnet50TSNE.png "TSNE for ResNet50 Features for Dog Breed Detection"
[image4]: ./myfiles/tsneplots/DogBreedsInceptionV3TSNE.png "TSNE for InceptionV3 Features for Dog Breed Detection"
[image5]: ./myfiles/tsneplots/DogBreedsXceptionTSNE.png "TSNE for Xception Features for Dog Breed Detection"

# Dog Project
- Project 2 in the Deep Learning Foundation Nanodegree Program at Udacity
- [html version of the solution notebook](https://sabinem.github.io/udacity-deeplearning-dog-project/)
- [Original project specfication](./original-project-specification.md)

## Parts
My submission consists of the following parts:
 - [the notebook dog_app.ipynb](./dog_app.ipynb)

 Several auxillary files
 - [a color palette for coloring of TSNE plots](./myfiles/palette/palette.npy)
 - [several TSNE plots](./myfiles/tsneplots/)
 - [several testimages](./myfiles/testimages/)
 - [saved parameters for the models](./saved_models/)


## Task
The task was to build an **app with Transfer Learning**, that
- **accepts images of humans and dogs** as valid input
- **rejects images that do not contain a human or dog** raising an error
- in the case of dogs the **breed is detected**
- in the case of a human a **human is detected** and the breed that the human resembles most is reported

# My Approach
The app that I built to solve the task above combines the predictions of several ML Algorithms:
- some given algorithms
- some algorithms that I built myself

## Given algorithms
We were given algorithms, that were already implemented for us:
### HaarCascadeFaceDetector
- a Haar feature based cascade classifier,
### Resnet50DogDetector
- a ResNet50 classifier, that was trained on Imagenet on labels that include
several dog breeds

## Obstacles
In order to distinguish between dogs humans and things, a classifier would normally need to see labeled training images of all three categories. In this case we were just given labeled images for dogs and humans. The dogs were labeled by their breeds. For the dogs we were also given bottleneck features for several well known networks pretrained on imagenet. Bottleneck-Features are CNNs were the last labeling layer is taken off, the features are then optimized for labeling imagenet images.
### Bottleneck-Features provided
- ResNet50
- VGG16
- VGG19
- InceptionV3
- Xception

# My Solution:
My solution used:
- the given **Resnet50DogDetector** above.
It did not use
- the given **HaarCascadeFaceDetector**
I combined it with:
- **MyHumanDetector**, see below
- **MyDogBreedDetector**, see below

## My HumanDetector
- It is based on ResNet50 Human- and Dog-Bottleneckfeatures.
- I calculated the Human Bottleneckfeatures from the given Human data on my own. MyHumanDetector got 100% accuracy on my chosen test data.

### TSNE of the ResNet50 Bottleneckfeatures
It shows, how good the Bottleneckfeatures were for differentiating between humans and dogs:
![TSNE for ResNet50 Features for Human Dog Detection][image1]

I guesss you could call this an overkill for the task at hand. I noticed it was biased towards humans. So everything not human was taken as a dog. This made it perfect for detecting humans, but really bad for detecting dogs.

## My DogHumanOtherDetector
- combines my **HumanDetector** with the provided **Resnet50DogDetector**
- is able to detect Humans if the HumanDetector returns True
- to detect Dogs if the Resnet50DogDetector is True
- everything else is considered neither dog nor human and raises an error

## My DogBreedDetector
Building the Dog Breed Detector was the harder ML task.
### Evaluating the bottleneck features
I evaluated the given bottleneck features by **comparing their TSNE mappings**:
You can see below how the features for some randomly chosen dog breeds are geometrically distributed:

#### TSNE mappings for VGG19, ResNet50, InceptionV3, Xception:
![TSNE for VGG19 Bottleneck Features for Dog Breed Detection][image2]
![TSNE for ResNet50 Bottleneck Features for Dog Breed Detection][image3]
![TSNE for InceptionV3 Bottleneck Features for Dog Breed Detection][image4]
![TSNE for Xception Bottleneck Features for Dog Breed Detection][image5]

### Transfer Learning Models
I decided to implement two simple models based on ResNet50 and InceptionV3 features:

#### ResNet50DogBreedDetector
- got **82.4163% test accuracy** for a these weights: [saved_models/weights.best.ResNet50_TL_model.hdf5](saved_models/weights.best.ResNet50_TL_model.hdf5)


#### InceptionV3DogBreedDetector
- got **82.0574% test accuracy** for a these weights: [saved_models/weights.best.InceptionV3_model.hdf5](saved_models/weights.best.ResNet50_TL_model.hdf5)

#### My CombinedDogBreedDetector
Since the two models make different predictions in about 20% of the cases, it makes sense to combine them and see whether I get an improvement:
- they are combined by taking the prediction where the model is surer (higher probability) of the breed it guesses
- the combined model has **86% test accuracy**, which is an improvement

## The App

The App works this way:

It combines:
- **my DogHumanOtherDetector** above
- **my CombinedDogBreedDetector** above

This is how it works:
- The **DogHumanOtherDetector** gives back whether this is a dog human or an error
- In case of a dog, the **CombinedDogBreedDetector** predicts the breed, in case of a human, the app also get the predictions and prints out, that the human resembles the breed.

## Evaluation

### What the app can do
- it detects humans quite well on photos with only humans
- it detects dog breeds well when they are pure breeds
- it rejects images with neither dogs nor humans

### Room for Improvement
- the app fails on mixed breeds: it just decides on one of the breeds
- the app also fails on photos with several dogs or dogs and humans. It doesn't detect how many dogs or people are on the picture
