import os
import sys
import IPython
import subprocess

#Read config.py file from same folder path as your notebook
#file = open("config.py", "r")

#You can then set the contents in the file to a variable and print it out for example using:
#fileContents = file.read()
#print(fileContents)

def run_train():
    print(os.getcwd())
    os.chdir('yolov5')
    #!python train.py --img 640 --batch 16 --epochs 2 --data {dataset.location}/data.yaml --weights best_v1.pt --cache
    train_cmd = 'train.py --img 640 --batch 16 --epochs 2 --data {dataset.location}/data.yaml --weights best_v1.pt --cache'
    subprocess.check_call([sys.executable, train_cmd])
    #%python train.py --img 640 --batch 16 --epochs 2 --data {dataset.location}/data.yaml --weights best_v1.pt --cache