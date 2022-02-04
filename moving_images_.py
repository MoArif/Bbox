import os
import pandas as pd
import numpy as np
from glob import glob
from tqdm import tqdm
import shutil


workers = ["w1","w2","w3","w4","w5"]
img_source = '/home/mofassir/vwfs_p2/data/SHAYAN_PASTE_HERE/mofassir_data/cleaned_results/images/tuv_sud'

for worker in tqdm(workers, desc="Workers"):
    root_dir = f'./person/{worker}/csv_data/'
    files = glob(root_dir+'*.csv')
    for file in tqdm(files, desc="Files"):
        df = pd.read_csv(file)
        img_names = df.bildname.map(lambda x: os.path.join(img_source,x))
        for img ,row in tqdm(zip(img_names,df.iterrows()), desc="Images"):
            shutil.copy(img,row[1].img_file_path)
