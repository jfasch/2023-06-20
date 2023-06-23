import csv

def read_csv_noheader(filename):
    f = open(filename, encoding='cp1252')
    rdr = csv.reader(f, delimiter=';', quotechar='"')

    for id, firstname, lastname, birth in rdr:
        u = {
            'id': int(id),
            'firstname': firstname,
            'lastname': lastname,
            'birth': birth,
            }
        yield u
        

def read_csv_header(filename):
    f = open(filename, encoding='cp1252')
    rdr = csv.DictReader(f, delimiter=';', quotechar='"')

    for record in rdr:
        id = record['ID']
        firstname = record['First name']
        lastname = record['Last name']
        birth = record['Date of Birth']

        u = {
            'id': int(id),
            'firstname': firstname,
            'lastname': lastname,
            'birth': birth,
            }

        yield u

def format_user(user):
    return f"ID:{user['id']}, Firstname:{user['firstname']}, Lastname:{user['lastname']}, Date of birth: {user['birth']}"
