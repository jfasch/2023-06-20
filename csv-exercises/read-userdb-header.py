import sys
import csv
import pprint

f = open(sys.argv[1], encoding='cp1252')
rdr = csv.DictReader(f, delimiter=';', quotechar='"')

for record in rdr:
    id = record['ID']
    firstname = record['First name']
    lastname = record['Last name']
    birth = record['Date of Birth']

    print(f'ID:{id}, Firstname:{firstname}, Lastname:{lastname}, Date of birth: {birth}')

