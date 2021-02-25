import ruamel.yaml
import pandas as pd

    # filename
# Coords (standardized/original)
    # Contributor
# Convert csv file
# Sprite size
# Special parts and variants
# Variations of sprite can be defined in this file
    # Character name and original texture
    # Config version in case standard changes


def flist(x):
    retval = ruamel.yaml.comments.CommentedSeq(x)
    retval.fa.set_flow_style()  # fa -> format attribute
    return retval


texture = "2742_1.png"           # Original python extracted texture
contributor = "colebob9"         # Whoever made the yaml file
character_name = "Sekiguchi"     # Simply the name of the character in question, nothing else


filename = 'coords/Sekiguchi2.csv'

df = pd.read_csv(filename)

# sort 

coords = df.T.to_dict()

print(coords)



# coords = {line_count: flist(row)}
# coords = {1: coords_1}

data = [
        {'info':
            {'character_name': character_name,
             'texture': texture,
             'contributor': contributor,
             'config_ver': 1
             }
         },
        {'coords':
            {'standard_coords': coords,

             'special_parts':
                {
                    'eye_1': {'X': 1, 'Y': 1, 'U': 1, 'V': 1}}
             }
         },
        {'variations':
            {
                'blushing_1': ['define eye, mouth, etc pieces here'],
                'smile_1': ['eye_1', 'mouth_1']

             }
         }
]

print("Dictionary:")
print(data)

yaml = ruamel.yaml.YAML()

with open('testyaml.yml', 'w') as f:
    yaml.dump(data, f)
