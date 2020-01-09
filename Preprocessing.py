'''
Code By Lukious
Memvber of BMCL

github.com/Lukious
'''
from PIL import Image
import numpy
import os,glob

folder_path = './pokemon-dataset/images/images'

def PNG_case(filename):
    im = Image.open(folder_path+'/'+filename)
    size = (56, 56)
    im.thumbnail(size)  
    im.save('./pokemon-dataset/images/Preprocessed/'+filename[:-4]+'.png')

def JPG_case(filename):
    im = Image.open(folder_path+'/'+filename)
    size = (56, 56)
    im.thumbnail(size)  
    im.save('./pokemon-dataset/images/Preprocessed/'+filename[:-4]+'.png')

def Image2Matrix(filename):
    im = Image.open(folder_path+'/'+filename)
    size = (56, 56)
    im.thumbnail(size)  
    ImageMatrix = numpy.asarray(im.convert('L'))
    numpy.save('./pokemon-dataset/images/MatrixPreprocessed/'+filename[:-4],ImageMatrix)


for filename in os.listdir(folder_path):
    print(filename)
    if(filename[-3:] == 'png'):
        PNG_case(filename)
    elif(filename[-3:] == 'jpg'):
        JPG_case(filename)
    Image2Matrix(filename)