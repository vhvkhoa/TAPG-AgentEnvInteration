import subprocess
import numpy as np


for threshold in np.arange(1., .1, -0.1):
    print('Threshold: {}'.format(threshold))
    command = ' '.join([
        'python main.py --cfg-file config/anet_detection.yaml',
        'BMN.POST_PROCESS.SOFT_NMS_ALPHA {}'
    ])
    subprocess.run(command.format(threshold), shell=True)

'''
for threshold in np.arange(0.1, 1.0, 0.1):
    alpha = 0.4
    print('Threshold: {}\tAlpha: {}'.format(threshold, alpha))
    command = ' '.join([
        'python main.py --cfg-file config/anet_proposal.yaml',
        'BMN.POST_PROCESS.SOFT_NMS_ALPHA {}',
        'BMN.POST_PROCESS.SOFT_NMS_LOW_THRESHOLD {}',
        'BMN.POST_PROCESS.SOFT_NMS_HIGH_THRESHOLD {}'
    ])
    subprocess.run(command.format(alpha, threshold, threshold), shell=True)
'''

'''
for i in range(10):
    model_path = 'checkpoints/thumos_c3d_checkpoints/checkpoint_{}/best_AR@100.pth'.format(i + 4)
    print('Evaluate model {}.'.format(model_path))
    command = ' '.join([
        'python main.py --cfg-file config/thumos_proposal.yaml',
        'MODE "validation"',
        'TEST.CHECKPOINT_PATH {}',
    ])
    subprocess.run(command.format(model_path), shell=True)
'''

'''
for nms_threshold in np.linspace(0.05, 1.0, 20):
    print('Evaluate Hard NMS Threshold {}.'.format(nms_threshold))
    command = ' '.join([
        'python main.py --cfg-file config/thumos_detection.yaml',
        'BMN.POST_PROCESS.HARD_NMS_THRESHOLD {}'.format(nms_threshold)
    ])
    subprocess.run(command, shell=True)
'''
