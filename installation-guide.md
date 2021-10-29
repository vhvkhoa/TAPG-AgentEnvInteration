# Installation Guide

## Validation
1. conda create -n aei python=3.8
2. conda activate aei
3. conda install pytorch torchvision torchaudio cudatoolkit=10.2 -c pytorch
4. pip install tqdm pandas tensorboard matplotlib fvcore scipy
5. cd into tapg-aei (root)
6. git clone https://github.com/frostinassiky/align1d
7. cd into tapg-aei/align1d
8. pip install -e .
9. cd ..
10. Run: python main.py --cfg-file config/anet_proposal.yaml MODE 'validation' GPU_IDS [0]

## Q&A
1q. UserWarning: This DataLoader will create 12 worker processes in total. Our suggested max number of worker in current system is #, which is smaller than what this DataLoader is going to create. Please be aware that excessive worker creation might get DataLoader running slow or even freeze, lower the worker number to avoid potential slowness/freeze if necessary.

1a. Change num_workers to # in line 171 of root>main.py>inference function
