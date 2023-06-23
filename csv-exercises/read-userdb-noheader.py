import sys

import user_csv

user_records = user_csv.read_csv_noheader(sys.argv[1])
for user in user_records:
    print(user_csv.format_user(user))
