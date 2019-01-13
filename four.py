import pandas as pd
import numpy as np
import json

headers = 'ship to party name,cleansed end customer name,zyme assigned end customer id'

def main():
    column_names = headers.split(',')
    print(column_names)
    df = pd.read_csv('data/3cslc.csv')

    # two_cols = df[[ column_names[0], column_names[1] ]]
    # two_cols.to_csv('data/two-cols.csv', index=False)

    party_names_all = df [column_names[0]].unique()
    party_names = list(filter(lambda r: not r is np.nan, party_names_all))
    tc_norm_float = df [column_names[1]].unique()
    tc_norm_float2 = filter(lambda r: not r is np.nan, tc_norm_float)
    tc_norm = list(map(str, tc_norm_float2))

    # print(type(party_names))
    # print(type(tc_norm))

    outmap = {
        'parties': party_names,
        'clean_names': tc_norm
    }
    with open('data/party-and-names.json', 'w') as f:
        f.write(json.dumps(outmap, indent=2))

    # with open('data/cleannames.json', 'w') as f:
    #     f.write(json.dumps(tc_norm, indent=2))


if __name__ == "__main__":
    main()
