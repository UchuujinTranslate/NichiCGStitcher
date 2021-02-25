import pandas as pd
from PIL import Image
import os
from NichiCGStitcher.order import grouper, sorted_nicely


def stitch(csvFile):
    image_size = (500, 500)  # until pandas image size is implemented

    new_image = Image.new('RGBA', image_size)

    # Make list of image files
    subdir = "cropped/"
    coords_dir = "coords/"

    image_list = []
    for file in os.listdir(subdir):
        if file.endswith(".png"):
            image_list.append(file)

    image_list = sorted_nicely(image_list)
    print(image_list)

    # Read csv
    csv_df = pd.read_csv(coords_dir + csvFile)
    index = list(csv_df.index.values)

    counter = 0
    for a, b in grouper(index, 2):

        print("counter:", counter)
        a_coords = [csv_df.X[a], csv_df.Y[a], csv_df.U[a], csv_df.V[a]]
        b_coords = [csv_df.X[b], csv_df.Y[b], csv_df.U[b], csv_df.V[b]]
        print("a index:", a, "   a coords:", a_coords)
        print("b index:", b, "   b coords:", b_coords)

        xy_coords = [a_coords[0], a_coords[1], b_coords[0], b_coords[1]]
        print(xy_coords)

        current_piece = subdir + image_list[counter]
        print(current_piece)
        counter = counter + 1

        from_cropped = Image.open(current_piece)
        new_image.paste(from_cropped, xy_coords)

        print("")

    new_image.save("merged_image.png", "PNG")
    new_image.show()
