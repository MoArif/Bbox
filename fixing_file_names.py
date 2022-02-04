import os
from glob import glob
from tqdm import tqdm
img_root = '/home/mofassir/vwfs_p2/data/SHAYAN_PASTE_HERE/mofassir_data/end-results/images/tuv_sud'
files = glob(image_root+"/*.jpg")

dest_path = '/home/mofassir/vwfs_p2/data/SHAYAN_PASTE_HERE/mofassir_data/cleaned_results/images/tuv_sud'
new_names = []
for file in tqdm(files):
    new_names.append(file.replace(':','-').replace('|','-'))


assert len(new_names) == len(files)
print('names in agreement')


for new_name, old_name in tqdm(zip(new_names,files)):
    new_root = dest_path
    name = new_name.split('/')[-1]
    new_path = os.path.join(new_root,name)
    shutil.copy(file,new_path)