# import numpy as np
import pandas as pd

def column_names(dataframe):
    '''
    Output:

    Index(['Ship to Party Name', 'NORM_ShiptoPartyName2',
        'NORM_CleansedEndCustomerName2', 'NORM_ShiptoPartyName',
        'NORM_CleansedEndCustomerName', 'Colour', 'Concat',
        'Check Ship to Party Name vs Cleansed End Customer Name',
        'Ship-To Address 1', 'Ship-To Address 2', 'Store Name/City',
        'Ship to State Code', 'Ship to Postal Code', 'Ship to Country Code',
        'Cleansed End Customer Name', 'Zyme Assigned End Customer ID',
        'Sales Units', 'LineID', 'Sales USD', 'Priority',
        'Potential Duplication ID 1', 'Duplication Type 1',
        'Potential Duplication ID 2', 'Duplication Type 2',
        'Potential Duplication ID 3', 'Duplication Type 3'],
        dtype='object')
    '''
    print(dataframe.columns)

def zyme_id_col_type():
    truid_df = pd.read_csv('data/audio.csv', na_values=['', '0'])
    print(truid_df['Zyme Assigned End Customer ID'].dtypes)

def main():
    trueid_df = pd.read_csv('data/audio.csv', na_values=['', '0'])
    trueid_df = trueid_df.astype({'Zyme Assigned End Customer ID': str})
    # column_names(trueid_df)
    # Interesting columns:
    int_cols = [
        'Ship to Party Name',
        'Cleansed End Customer Name',
        'Zyme Assigned End Customer ID'
    ]
    intdf = trueid_df[int_cols]
    # print(intdf.columns)
    print(intdf) # .head(5))
    intdf.to_csv('data/3cs.csv', index=False)

if __name__ == "__main__":
    # zyme_id_col_type()
    main()
