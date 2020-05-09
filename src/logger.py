import csv


def create_file(file_name, headers):
    with open(file_name, 'w') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()


def write_file(file_name, headers, row):
    with open(file_name, 'a') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writerow(row)
