
import csv
import pprint as pp
from collections import Counter
import json

refcount = 1

def mk_part(key, vals):
    global refcount
    c = Counter(vals)
    m = {}
    m['id'] = refcount
    m['name'] = key
    refs = []
    refcount += 1
    for i in c.items():
        # print(i)
        refs.append( {
            'id': i[0],
            'count': i[1]
        })
        # m[i[0]] = i[1]
    m['refs'] = refs
    return m
    # return [list(i) for i in c.items()]

def main():
    with open('audio.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        res = {}
        for row in reader:
            # Cleansed End Customer Name,Zyme Assigned End Customer ID
            # print(row['Cleansed End Customer Name'], row['Zyme Assigned End Customer ID'])
            zymeids = res.get(row['Cleansed End Customer Name'], [])
            if row['Zyme Assigned End Customer ID'] != '':
                zymeids.append(row['Zyme Assigned End Customer ID'])
                res[row['Cleansed End Customer Name']] = zymeids

        # pp.pprint(res)

        # for k in res:
        #     vs = set(res[k])
        #     if len(vs) > 1:
        #         print(k, res[k])

        # print('=='*40)

        outmap = []
        for k in res:
            vs = set(res[k])
            if len(vs) > 1:
                outmap.append(mk_part(k, res[k]))
                # print(k, vs, len(res[k]))
                # c = Counter(res[k])
                # print(c.items(), '\n')

        print(json.dumps({"ids": outmap}, indent=True))

        # with open('company-zymeids.csv', 'w') as outfile:
        #     writer = csv.writer(outfile)
        #     writer.writerows(sorted(output))

if __name__ == "__main__":
    main()