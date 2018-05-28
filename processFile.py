#
#  Read the file to extract data
#
#

import csv

def parse_lines(line_reader):
    for line in line_reader:
        if (len(line) == 4):
            yield line


def get_data_from_comma_separated_file(filename : str):
    with open(filename, 'r') as f:
       reader = csv.reader(f, dialect="excel-tab")
       your_list = list(reader)
    data = [[float(long), float(lat), float(age)] for long, lat, _, age in your_list[1:]]
    # print(your_list)
    return data


def get_data_from_tab_separated_file(filename : str):
    with open('file.csv', 'r') as f:
        reader = csv.reader(f, dialect="excel-tab")
        lines = [[long, lat, age] for long, lat, _, age in parse_lines(reader)]
        header_lines = lines[0]
        lines = [[float(long), float(lat), float(age)] for long, lat, age in lines[1:]]
    return header_lines, lines

#
# header, data = get_data_from_tab_separated_file('file.csv')
#
#
# x = [x for x, y, age in data]
# y = [y for x, y, age in data]
# age = [age for x, y, age in data]
#
#
# print(data)
# print(x)
# print(y)
# print(age)
#
# min_x, max_x = min(x), max(x)
# min_y, max_y = min(y), max(y)
# min_age, max_age = min(age), max(age)
#
# print(min_x, max_x)
# print(min_y, max_y)
# print(min_age, max_age)
#

