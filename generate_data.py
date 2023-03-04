import numpy as np
import cv2
import os

def reformat_dataset(path,folder_number=40,image_per_folder=10):
    data = []
    labels = []
    for i in range(1,folder_number+1):
        for j in range(1,image_per_folder+1):
            current_path = os.path.join(path,f"s{i}",f"{j}.pgm")
            img = cv2.imread(current_path,0).flatten()
            data.append(img)
            labels.append(i)

    return np.array(data), np.array(labels)
