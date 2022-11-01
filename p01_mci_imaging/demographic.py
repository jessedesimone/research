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
    return pd.read_excel(fh, sheet_name="Amy_neg_only")

if __name__ == '__main__':
    path = file_path()
    df = data_reader()

#cleaning
df = df.rename(columns={"Quest_Dx__0.16_cutoff_":"Quest_Dx"}, errors='raise')
df = df.rename(columns={"A?42_40_Status":"AB42_40"}, errors='raise')

#value_counts
'''
26 PreMCI Clinical; can we remove?
This leaves 63 with MCI (demographic txt file shows 82)
5 Normal with HR AB42/40 - how do we handle?
Across eMCI and Late MCI, 22 HR and 41 low risk; sizeable difference in samples

'''
df['UF_Diagnosis'].value_counts()
pd.crosstab(df.UF_Diagnosis, df.Quest_Dx)
pd.crosstab(df.UF_Diagnosis, df.AMYLPET_Quest)
pd.crosstab(df.Quest_Dx, df.AB42_40)
pd.crosstab([df['UF_Diagnosis'], df['Quest_Dx']], df['AB42_40'])
pd.crosstab([df['UF_Diagnosis'], df['Quest_Dx']], df['AMYLPET_Quest'])
pd.crosstab([df['UF_Diagnosis'], df['AB42_40']], df['AMYLPET_Quest'])




