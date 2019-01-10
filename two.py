import pandas as pd
import numpy as np

import difflib

headers = 'ship to party name,cleansed end customer name,zyme assigned end customer id'

def main():
    column_names = headers.split(',')
    print(column_names)
    df = pd.read_csv('data/3cslc.csv')

    # two_cols = df[[ column_names[0], column_names[1] ]]
    # two_cols.to_csv('data/two-cols.csv', index=False)

    # m, n = 0, 0
    # party_names = []
    # tc_norm = []    # Non-null values of cleansed customer names.
    # for i in range(len(two_cols)):
    #     if not two_cols.iloc[i][1] is np.nan and (not two_cols.iloc[i][1] in tc_norm):
    #         tc_norm.append(str(two_cols.iloc[i][1]))
    #         m += 1
    #         if m % 1000 == 0:
    #             print('>', two_cols.iloc[i][1])
    #     if not str(two_cols.iloc[i][0]) in party_names:
    #         party_names.append(str(two_cols.iloc[i][0]))
    #         n += 1
    #         if n % 1000 == 0:
    #             print('#', two_cols.iloc[i][0])

    party_names_all = df [column_names[0]].unique()
    party_names = filter(lambda r: not r is np.nan, party_names_all)
    tc_norm_float = df [column_names[1]].unique()
    tc_norm_float2 = filter(lambda r: not r is np.nan, tc_norm_float)
    tc_norm = map(str, tc_norm_float2)

    print(len(list(party_names)), len(list(tc_norm)))

    # for clean_name in tc_norm:
    #     res = difflib.get_close_matches(clean_name, party_names)
    #     print(clean_name)
    #     print(res)
    #     print()

    # two_cols.to_json('data/two-cols.json')

    # with open('data/two-cols.csv', 'w') as f:
    #     for c,d in two_cols:
    #         f.write(str(c), str(d))
    #         f.write('\n')


    # c2_floats = df[column_names[1]].unique()
    # # b = c2_floats[[ column_names[0], column_names[1] ]]
    # c2_strs = sorted(map(str, c2_floats))
    # with open('data/uniq-cn.csv', 'w') as f:
    #     for c in c2_strs:
    #         f.write(str(c))
    #         f.write('\n')

    # no_name_recs = df[df[column_names[1]].isnull()]
    # a = no_name_recs[column_names[0]]
    # a.to_csv('data/party-with-no-ecn.csv', index=False)
    # # print('no_name_recs:', len(no_name_recs))

if __name__ == "__main__":
    main()
