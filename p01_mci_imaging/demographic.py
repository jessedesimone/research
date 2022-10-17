'''
File to examine demographic data
'''

#import packages
import os
import pandas as pd

#data reader
pd.set_option('display.max_columns', None)
def file_path():
    #fpath = input('\nEnter <path/to/infiles>: ')
    fpath = '/Users/jessedesimone/DeSimone_Github/Research/p01_mci_imaging/infiles'
    print('\nPath to input files: ', fpath)
    print('\nFiles in Directory:')
    print(os.listdir(fpath))
    return(fpath)

def data_reader():
    fname = input('\nEnter file name : ')
    fh = os.path.join(path, fname)
    return pd.read_csv(fh)

if __name__ == '__main__':
    path = file_path()
    df = data_reader()

#cleaning
df = df.rename(columns={"Quest_Dx__0.16_cutoff_":"Quest_Dx"}, errors='raise')
df = df.rename(columns={"A?42_40_Status":"AB42_40"}, errors='raise')


#value_counts
df['UF_Diagnosis'].value_counts()

#crosstab
'''
5 normal classified as high risk; only 21 of 80 MCI classified as high risk
Quest_Dx corresponds with AB42_40 (i.e., positive=high risk across all groups)
5 positive PET contained within this group (2 normal, 2 preMCI, 1 eMCI)
'''
pd.crosstab(df.UF_Diagnosis, df.Quest_Dx)
pd.crosstab(df.Quest_Dx, df.AB42_40)
pd.crosstab([df['UF_Diagnosis'], df['Quest_Dx']], df['AB42_40'])
pd.crosstab([df['UF_Diagnosis'], df['Quest_Dx']], df['AMYLPET_Quest'])
pd.crosstab([df['UF_Diagnosis'], df['AB42_40']], df['AMYLPET_Quest'])




