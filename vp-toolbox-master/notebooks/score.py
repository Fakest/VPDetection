#py3.7.4

import itertools
import json
import math
import os
import time

import cv2
from matplotlib import pyplot as plt
import numpy as np

from platform import python_version

print(python_version())

from vp import draw_tools
from vp import scoring
from vp import vp_finder


import helpers
import toulouse
import york_urban

# Load York Urban dataset.
# YORK_URBAN_DATASET_FOLDER = 'YorkUrbanDB_2'
# york_urban_dataset_path = os.path.abspath(os.path.join(os.getcwd(), YORK_URBAN_DATASET_FOLDER))
# print('Loading dataset at %s.' % york_urban_dataset_path)
# york_urban_dataset = york_urban.load_dataset(york_urban_dataset_path)#.with_mask(set(range(5)))
# print('\nLoaded %s images from dataset.' % len(york_urban_dataset.image_paths))

TOULOUSE_DATASET_FOLDER = 'toulouse_dataset/tvpd_dataset'
toulouse_dataset_path = os.path.abspath(os.path.join(os.getcwd(), TOULOUSE_DATASET_FOLDER))
print('Loading dataset at %s.' % toulouse_dataset_path)
toulouse_dataset = toulouse.load_dataset(toulouse_dataset_path)
print('\nLoaded %s images from dataset.' % len(toulouse_dataset.image_paths))

main_results_tou = helpers.batch_detect_vps_and_score(
    toulouse_dataset,
    vp_finder.find_vanishing_points_in_image)


# main_results_yud = helpers.batch_detect_vps_and_score(
#     york_urban_dataset,
#     vp_finder.find_vanishing_points_in_image)

# print(main_results_yud.image_vp_to_lines[1].keys())

# SAMPLE_INDICES = range(len(york_urban_dataset.image_paths))[:5]
helpers.visualize_vp_detection_results(york_urban_dataset, main_results_yud)
# # array[Nx4] ===> array[1xN]{tuple[1x4]}
# # [[1 2 3 4], [5, 6, 7, 8]] --> [(1,2,3,4), (5, 6, 7, 8)]