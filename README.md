# AEI: Actors-Environment Interaction with Adaptive Attention for Temporal Action Proposals Generation

A pytorch-version implementation codes of paper:
 "AEI: Actors-Environment Interaction with Adaptive Attention for Temporal Action Proposals Generation",
  which is accepted in BMVC 2021.

## Prerequisites
* Python 3.8
* Pytorch 1.9
* fvcore
* numpy, pandas, matplotlib, tensorboardX etc.


## Download Features
3D Resnet-50 features extracted from rescaled videos of ActivityNet-1.3 can be downloaded
[here](will be updated soon).

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

This implementation is partly based on this [pytorch-implementation of BMN](https://github.com/JJBOY/BMN-Boundary-Matching-Network.git).

paper:[AEI: Actors-Environment Interaction with Adaptive Attention for Temporal Action Proposals Generation](will update soon)
