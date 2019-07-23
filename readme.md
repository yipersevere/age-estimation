## Multi-loss function for age estimation

### Git repository branch

1. label_smoothing, git checkout label_smoothing

### task

- [x] ~~clean the multitask learning source code to multi-loss age estimation task,~~  
- [x] ~~reference ni xingyang's repository.~~


****
## Contents
* [task](#task)
* [experiments](#experiments)
* [age dataset](#age-dataset)
* [face detection and alignment](#face-detection-and-alignment)
* [reference](#reference)
****


### experiments

#### run experiments for the age estimation task 

```
python main.py  
```

#### age dataset

1. [cleaned ChaLEARN CVPR 2016](http://chalearnlap.cvc.uab.es/dataset/19/description/) 
2. [IMDB-WIKI](https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/)
3. [AgeDB](https://ibug.doc.ic.ac.uk/resources/agedb/)


#### face detection and alignment

* using Yue's processed images on ChaLearn CVPR 2016 dataset; 
* - [ ] elaborate the method of the face detection and face alignment, currently I can not remember.



#### The state of the art result on age estimation from the [BridgeNet](https://arxiv.org/abs/1904.03358) paper

![Example](related_materials/state-of-the-art-result-age-estimation-on-chalearn-2016.png)



## reference

1. the current state of the art approach, [BridgeNet](https://arxiv.org/abs/1904.03358) CVPR 2019
2. the demo paper for writing, [SAF- BAGE](https://arxiv.org/abs/1803.05719), it was accepted by WACV 2019.
3. the similar idea as the head pose estimation, [hopenet](https://arxiv.org/abs/1710.00925), the GitHub repository is [here](https://github.com/natanielruiz/deep-head-pose)