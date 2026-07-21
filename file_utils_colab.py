# file_utils_colab.py
"""
This is a re-use function that can only be used in Google colab 
"""

import os
import time
from google.colab import drive
from google.colab import userdata


def read_text_from_file(folder_path, file_name):

  # Always mount Drive explicitly when using Google Drive
  drive.mount('/content/drive', force_remount=True)
  print("Drive mounted.")

  # Wait until MyDrive is available
  mydrive_path = '/content/drive/MyDrive'
  while not os.path.exists(mydrive_path):
      print("Waiting for Drive to be ready...")
      time.sleep(1)

  # Path to the file
  file_path = os.path.join(mydrive_path, folder_path, file_name) #'Files/Text/example.txt')

  # Check if the file exists
  if os.path.exists(file_path):
      # Read the content of the file
      with open(file_path, 'r') as file:
          contents = file.read()
      return contents
  else:
      return "File not found!"
  
def write_text_to_file(folder_path, file_name, write_text):

  # Always mount Drive explicitly when using Google Drive
  drive.mount('/content/drive', force_remount=True)
  print("Drive mounted.")

  # Wait until MyDrive is available
  mydrive_path = '/content/drive/MyDrive'
  while not os.path.exists(mydrive_path):
      print("Waiting for Drive to be ready...")
      time.sleep(1)

  # Create folder path if it doesn't exist
  folder_path = os.path.join(mydrive_path, folder_path) #'Files/Text')
  os.makedirs(folder_path, exist_ok=True)

  # Define file path
  file_path = os.path.join(folder_path, file_name) #'example.txt')

  # Write content to the file
  with open(file_path, 'w') as file:
      file.write(write_text)


  print("File written successfully to:", file_path)