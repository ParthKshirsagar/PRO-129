import csv

dataset_1 = []
dataset_2 = []

with open('dataset_1_modified.csv', 'r') as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        dataset_1.append(row)

header_1 = dataset_1[0]
stars_data_1 = dataset_1[1:]

with open('dataset_2.csv', 'r') as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        dataset_2.append(row)


header_2 = dataset_2[0]
stars_data_2 = dataset_2[1:]

headers = header_1 + header_2
stars_data = []

for index, data_row in enumerate(stars_data_1):
    stars_data.append(stars_data_1[index])

with open('final.csv', 'a+') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(stars_data)