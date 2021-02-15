from NichiCGStitcher import * 
import os

# strip_csv()
coords_dir = "coords/"

for subdir, dirs, files in os.walk(coords_dir):
    for file in files:
        crop(file)
