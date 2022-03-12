# -*- coding: utf-8 -*-
"""
Spyder Editor
"""

#!/usr/bin/env python
import numpy as np

#Set the `numpy` pseudo-random generator at a fixed value
#This helps with repeatable results everytime you run the code. 
np.random.seed(1000)

import matplotlib.pyplot as plt
import os
import cv2
from PIL import Image
import keras