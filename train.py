import subprocess
from ultralytics import YOLO
import torch

# paths
log_dir = '/media/datasets/runs/detect'
yaml_path = '/media/datasets/helm.yaml'

# # Define the command to launch TensorBoard
# tensorboard_command = f"tensorboard --logdir={log_dir}"

# # Use subprocess to run the command
# subprocess.Popen(tensorboard_command, shell=True)

# Select the device where we are going to train the model
device = 'cuda' if torch.cuda.is_available() else 'cpu'
print(device)

# Define the base model
model = YOLO('yolov8n.pt') 

# train the model
_ = model.train(data=yaml_path, epochs = 50, batch = 32)  

# evaluate model performance on the validation set
_ = model.val(data=yaml_path)