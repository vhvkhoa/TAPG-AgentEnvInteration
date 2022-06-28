# AEI: Actors-Environment Interaction with Adaptive Attention for Temporal Action Proposals Generation

[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/aei-actors-environment-interaction-with/temporal-action-proposal-generation-on)](https://paperswithcode.com/sota/temporal-action-proposal-generation-on?p=aei-actors-environment-interaction-with)

A pytorch-version implementation codes of paper:
 "AEI: Actors-Environment Interaction with Adaptive Attention for Temporal Action Proposals Generation",
  which is accepted in BMVC 2021.

## Installation Guide

1. conda create -n aei python=3.8
2. conda activate aei
3. conda install pytorch torchvision torchaudio cudatoolkit=10.2 -c pytorch
4. pip install tqdm pandas tensorboard matplotlib fvcore scipy
5. cd into tapg-aei (root)
6. git clone https://github.com/frostinassiky/align1d
7. cd into tapg-aei/align1d
8. pip install -e .
9. cd ..

## Download Features
3D Resnet-50 features extracted from rescaled videos of ActivityNet-1.3 can be downloaded below:
* Environment features are [here](https://drive.google.com/file/d/1hPhcQ7EzyCh0A3SyZfgZScFVFZMEvVhe/view?usp=sharing) (~80GB uncompressed).
* Actor features are [here](https://drive.google.com/file/d/1lOQG1FgDseRKDs3RNgpKd000OOZiag1s/view?usp=sharing) (~215GB uncompressed).
* Annotations of [Activitynet-1.3](http://ec2-52-25-205-214.us-west-2.compute.amazonaws.com/files/activity_net.v1-3.min.json) can be downloaded from the [official website](http://activity-net.org/download.html).

## Training and Testing  of AEI
Default configurations of AEI are stored in config/defaults.py.
The modified configurations are stored in config/*.yaml for training and testing of AEI on different datasets (ActivityNet-1.3 and THUMOS-14).
We can also modify configurations through commandline arguments.

1. To train AEI on TAPG task of ActivityNet-1.3 with 1 GPU:
```
python main.py --cfg-file config/anet_proposals.yaml MODE 'training' GPU_IDS [0]
```

2. To evaluate AEI on validation set of ActivityNet-1.3 with 1 GPU:
```
python main.py --cfg-file config/anet_proposals.yaml MODE 'validation' GPU_IDS [0]
```

## Reference

This implementation is partly based on this [pytorch-implementation of BMN](https://github.com/JJBOY/BMN-Boundary-Matching-Network.git) for the boundary matching module.

paper: [AEI: Actors-Environment Interaction with Adaptive Attention for Temporal Action Proposals Generation](https://arxiv.org/abs/2110.11474)


## Q&A
1q. "UserWarning: This DataLoader will create 12 worker processes in total. Our suggested max number of worker in current system is #, which is smaller than what this DataLoader is going to create. Please be aware that excessive worker creation might get DataLoader running slow or even freeze, lower the worker number to avoid potential slowness/freeze if necessary."

1a. Change num_workers to # in line 171 of root>main.py>inference function

## Citation
If you find AEI useful for your research, please consider citing:
```
@article{khoavoAEI2021,
  author    = {Khoa Vo and
               Hyekang Joo and
               Kashu Yamazaki and
               Sang Truong and
               Kris Kitani and
               Minh{-}Triet Tran and
               Ngan Le},
  title     = {{AEI:} Actors-Environment Interaction with Adaptive Attention for
               Temporal Action Proposals Generation},
  journal   = {CoRR},
  volume    = {abs/2110.11474},
  year      = {2021},
  url       = {https://arxiv.org/abs/2110.11474},
  eprinttype = {arXiv},
  eprint    = {2110.11474},
}
```


## Contact
Khoa Vo:
```
khoavoho@uark.edu
```

