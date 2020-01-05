
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 21:49:50 2020
@author: Lukious
"""

import numpy as np
import os,glob

folder_path = './pokemon-dataset/images/MatrixPreprocessed'
counter = 0
filename_list = []

for filename in os.listdir(folder_path):
    counter = counter + 1
    filename_list.append(filename[:-4])
    print(filename)
    temp = np.load(folder_path+'/'+filename)
    temp = temp.reshape((1,28,28))
    if counter == 1:
        Pokemon_data = temp
        Pokemon_data = Pokemon_data.reshape((1,28,28))
    else:
        Pokemon_data = np.concatenate((Pokemon_data, temp),axis = 0)
print("DONE")
