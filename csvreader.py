import csv
import csvreader

headers = 'ship to party name,cleansed end customer name,zyme assigned end customer id'

def main():
    rd = csv.reader('data/3cslc.csv', dialect='excel')
    print(rd)

if __name__ == "__main__":
    main()
