import csv

# with open("data.csv", "r") as csv_file:
#     csv_reader = csv.reader(csv_file)
#
#     with open("new_csv.csv", "w") as new_file:
#
#         csv_writer = csv.writer(new_file, delimiter="-")
#
#         for line in csv_reader:
#             print(csv_writer.writerow(line))

# with open("data.csv", "r") as csv_file:
#     csv_reader = csv.DictReader(csv_file)
#
#     for line in csv_reader:
#         print(line)

with open("data.csv", "r") as file_csv:

    csv_reader = csv.reader(file_csv)

    with open("new_csv.csv", "w") as write_csv:

        csv_writer = csv.writer(write_csv, delimiter="-")
        next(csv_wr)

        for line in csv_reader:

            new = csv_writer.writerow(line)
