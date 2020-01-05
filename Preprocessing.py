from PIL import Image
import os,glob

folder_path = './pokemon-dataset/images/images'

def PNG_case(filename):
    im = Image.open(folder_path+'/'+filename)
    size = (28, 28)
    im.thumbnail(size)  
    im.save('./pokemon-dataset/images/Preprocessed/'+filename[:-4]+'.png')

def JPG_case(filename):
    im = Image.open(folder_path+'/'+filename)
    size = (28, 28)
    im.thumbnail(size)  
    im.save('./pokemon-dataset/images/Preprocessed/'+filename[:-4]+'.png')


for filename in os.listdir(folder_path):
    print(filename)
    if(filename[-3:] == 'png'):
        PNG_case(filename)
    elif(filename[-3:] == 'jpg'):
        JPG_case(filename)