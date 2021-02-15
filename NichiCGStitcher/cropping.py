import csv
from PIL import Image

coords_dir = "coords/"
crops_dir = "cropped/"


def crop(coords_csv):
    with open(coords_csv, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
    
    inImage = csv_reader['img'][0]

    #Create an Image Object from an Image
    im = Image.open(inImage)

    #Display actual image
    #im.show()

    #left, upper, right, lower

    looped_once = False
    counter = 0

    # rewrite with pandas?
    # crop images
    for row in csv_reader:
        if looped_once == False:
            coords1 = [float(row['X']), float(row['Y']),
                    float(row['U']), float(row['V'])]
            print("Coords 1:", coords1)
            looped_once = True

        elif looped_once == True:
            coords2 = [float(row['X']), float(row['Y']),
                    float(row['U']), float(row['V'])]
            print("Coords 2:", coords2)

            uvcoords = [coords1[2], coords1[3], coords2[2], coords2[3]]

            print("UV Coords:", uvcoords)

            counter = counter + 1
            looped_once = False

            cropped = im.crop(uvcoords)

            filename = f'{crops_dir}Sekiguchi{counter}.png'
            cropped.save(filename)
            print(f"Cropped and saved {filename}")

            # test
            # print(f"Processed: {filename}")
            print('')

    return cropped
