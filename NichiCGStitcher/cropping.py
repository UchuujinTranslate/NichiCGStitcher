import pandas as pd
from PIL import Image
import sys

coords_dir = "coords/"
crops_dir = "cropped/"
cgs_dir = "cgs/"


def crop(coords_csv):
    print(f"Opening {coords_csv}")
    df = pd.read_csv(coords_dir + coords_csv)
    print(df)

    inImage = cgs_dir + df.img[0]
    print(inImage)

    # Create an Image Object from an Image
    im = Image.open(inImage)

    # Display actual image
    # im.show()

    # it1, it2 = more_itertools.pairwise(df.iterrows())
    # print(it1)
    # coords1 = [it1.X[it1.index], it1.Y[it1.index],
    #            it1.U[it1.index], it1.V[it1.index]]
    # print("Coords 1:", coords1)

    looped_once = False
    counter = 0

    for index, row in df.iterrows():
        print(row)
        print('------')
        if looped_once is False:
            coords1 = [df.X[index], df.Y[index], df.U[index], df.V[index]]
            print("Coords 1:", coords1)
            looped_once = True

        elif looped_once is True:
            coords2 = [df.X[index], df.Y[index], df.U[index], df.V[index]]
            print("Coords 2:", coords2)

            uvcoords = [coords1[2], coords1[3], coords2[2], coords2[3]]

            print("UV Coords:", uvcoords)

            counter = counter + 1
            looped_once = False

            cropped = im.crop(uvcoords)

            csvNoExt = coords_csv.rsplit('.', 1)[0]
            filename = f'{crops_dir}{csvNoExt}_{counter}.png'
            cropped.save(filename)
            print(f"Cropped and saved {filename}")

            # test
            # print(f"Processed: {filename}")
            print('')


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("Crops texture based on csv.")
        print("Usage: cropping.py <input csv>")
        print('')

    # one arg
    if len(sys.argv) == 2:
        inFile = sys.argv[1]
        crop(inFile)

    # #left, upper, right, lower

    # looped_once = False
    # counter = 0

    # # rewrite with pandas?
    # # crop images
    # for row in df:
    #     if looped_once == False:
    #         coords1 = [float(row['X']), float(row['Y']),
    #                 float(row['U']), float(row['V'])]
    #         print("Coords 1:", coords1)
    #         looped_once = True

    #     elif looped_once == True:
    #         coords2 = [float(row['X']), float(row['Y']),
    #                 float(row['U']), float(row['V'])]
    #         print("Coords 2:", coords2)

    #         uvcoords = [coords1[2], coords1[3], coords2[2], coords2[3]]

    #         print("UV Coords:", uvcoords)

    #         counter = counter + 1
    #         looped_once = False

    #         cropped = im.crop(uvcoords)

    #         filename = f'{crops_dir}Sekiguchi{counter}.png'
    #         cropped.save(filename)
    #         print(f"Cropped and saved {filename}")

    #         # test
    #         # print(f"Processed: {filename}")
    #         print('')

    # return cropped
