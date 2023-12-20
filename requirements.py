import torch
import os
import git
import sys
from git import Repo
import subprocess
import pip
import platform
from IPython.display import Image, clear_output

# Function to allow multiple mkl instances to run to resolve issue on macos
def check_mkl():
    osName = platform.system()
    if osName == 'Darwin':
        os.environ['KMP_DUPLICATE_LIB_OK']='True'

# Function to clone YoloV5 repo from Github, install EasyOCR, other pre-requisite packages and roboflow
def get_yolov5():   
    isExist = 'yolov5'
    isData = 'datasets'
    if not os.path.exists(isExist):
        git.Repo.clone_from('https://github.com/ultralytics/yolov5.git','yolov5')
        os.chdir('yolov5')
        package1 = 'easyocr'
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', package1])
        package2 = 'requirements.txt'
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', package2])
        package3 = 'roboflow'
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', package3])
        
        print(f"Setup complete. Using torch {torch.__version__} ({torch.cuda.get_device_properties(0).name if torch.cuda.is_available() else 'CPU'})")
    elif os.path.exists(isData):
        print("Yolov5 Repo and Dataset is already downloaded!!! Loading the Yolov5 directory...")
        os.chdir('yolov5')
    else:
        print("Yolov5 Repo is already downloaded!!! Loading the Yolov5 directory...")
        os.chdir('yolov5')

# Function to setup environment for Roboflow dataset (dataset created and annotated in Roboflow)
def prepare_dataset():
    from roboflow import Roboflow
    rf = Roboflow(model_format="yolov5", notebook="ultralytics")
    data_path = os.getcwd() 
    os.environ["DATASET_DIRECTORY"] = data_path + "/../datasets"

# Function to download Roboflow dataset using private API key
def download_dataset():
    from roboflow import Roboflow
    rf = Roboflow(api_key="4QWeeRxN4OmTfj66Wv0Z")
    project = rf.workspace("cbu").project("jersey-number-detection")
    dataset = project.version(8).download("yolov5")