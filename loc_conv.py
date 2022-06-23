import os
import pandas as pd

raw = input('Enter full path of .csv file: ')

def scrape():
    df = pd.read_csv(raw, sep=',', quotechar='"', engine='python')
    dflib = pd.read_csv("C:/Users/aap82/Desktop/Felix/Sheep/Scripts/LOC_library.csv", sep=',', quotechar='"', engine='python')
    for i, rowValue in df['gene'].iteritems():
        temp = rowValue
        if (temp.startswith('LOC', 0, 3)):
            convert = temp
            for index, row in dflib.iterrows():
                if (row['loc'] == temp):
                    if (row['gene'] == 'name'):
                        convert = row['note']
                    else:
                        convert = row['gene']
                    break
            df['gene'].replace(temp, convert, inplace=True)
    df.to_csv(raw, encoding='utf-8', quotechar='"', index=False, quoting=3)

if (os.path.isfile(raw)):
    print('File found. Running script...')
    scrape()
    print('Conversion finished.')
else:
    print('File not found. Please check that the path and/or file extension was entered correctly.')