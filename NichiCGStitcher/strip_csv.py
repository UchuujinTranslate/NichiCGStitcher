import pandas as pd
import sys

# inFile = "Sekiguchi1.csv"
# outFile = "cleaned.csv"


# inFile is path to csv file
# outFile is path to output csv file
def strip_csv(inFile, outFile="cleaned.csv"):
    print(f"Cleaning {inFile} and outputting as {outFile}.")

    # open csv
    print(f"Opening {inFile}")
    df = pd.read_csv(inFile, header=1)
    print(df)
    print('')

    # remove extra columns
    print("Removing extra columns...")
    keep_col = ['X', 'Y', 'U', 'V', 'img']
    df = df[keep_col]
    print(df)
    print('')

    # drop rows after the first row with x y etc headers
    print("Removing rows with headers...")
    df = df[df.X != 'X']
    print(df)
    print('')

    # drop rows with NaN values
    print("Removing rows with empty values...")
    df = df.dropna(thresh=4)
    print(df)
    print('')

    # convert all to int
    print("Converting all coordinates to integers...")
    # df = df.apply(pd.to_numeric, downcast='integer')
    df['X'] = pd.to_numeric(df['X'], downcast='integer')
    df['Y'] = pd.to_numeric(df['Y'], downcast='integer')
    df['U'] = pd.to_numeric(df['U'], downcast='integer')
    df['V'] = pd.to_numeric(df['V'], downcast='integer')
    print(df)
    print('')

    df.to_csv(outFile, index=False)
    print(f"Outputted to {outFile}")
    print('')

    return outFile


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("Cleans up a csv file from a coordinates spreadsheet.")
        print("Usage: strip_csv.py <input csv> [output csv]")
        print('')

    # one arg
    if len(sys.argv) == 2:
        inFile = sys.argv[1]
        strip_csv(inFile)

    # two args
    if len(sys.argv) >= 3:
        inFile = sys.argv[1]
        outFile = sys.argv[2]
        strip_csv(inFile, outFile)
