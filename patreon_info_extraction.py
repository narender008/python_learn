import csv

with open("patreon.csv", "r") as data_file:

    data = csv.DictReader(data_file)
    next(data)
    for row in data:
        if row['FirstName'] == 'No Reward':
            break
        print(row['FirstName'], row['LastName'])


# import csv
#
# html_output = ''
# names = []
#
# with open('patreon.csv', 'r') as data_file:
#     csv_data = csv.DictReader(data_file)
#
#     # We don't want first line of bad data
#     next(csv_data)
#
#     for row in csv_data:
#         print(row['FirstName'], row['LastName'])
    # for line in csv_data:
    #     if line['FirstName'] == 'No Reward':
    #         break
    #     names.append(f"{line['FirstName']} {line['LastName']}")

# html_output += f'<p>There are currently {len(names)} public contributors. #Thank You!</p>'
#
# html_output += '\n<ul>'
#
# for name in names:
#     html_output += f'\n\t<li>{name}</li>'
#
# html_output += '\n</ul>'
#
# print(html_output)
