from NichiCGStitcher.cropping import crop
from NichiCGStitcher.stitch import stitch
# from NichiCGStitcher.strip_csv import strip_csv
import os

# strip_csv()

coords_dir = "coords/"

for subdir, dirs, files in os.walk(coords_dir):
    for file in files:
        crop(file)
        stitch(file)
