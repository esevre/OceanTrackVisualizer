#
#  Read the file to extract data
#
#

import csv


def remove_newlines(line: str):
    return line.rstrip('\n')


def remove_trailing_tabs(line: str):
    return line.rstrip('\t')


def parse_lines(line_reader):
    for line in line_reader:
        if (len(line) == 4):
            yield line


def read_csv(filename : str):
    f = open(filename, 'r')
    contents = f.readlines()
    results = []
    for i, line in enumerate(contents):
        temp_line = remove_newlines(line)
        temp_line = remove_trailing_tabs(temp_line)
        results.append(temp_line.split('\t'))
    return results


def read_specified_data(filename : str):
    results = read_csv(filename)
    results = [[long, lat, age] for long, lat, _, age in parse_lines(results)]
    header_line = results[0]
    lines = [[float(long), float(lat), float(age)] for long, lat, age in results[1:]]
    return header_line, lines


# def get_data_from_comma_separated_file(filename : str):
#     with open(filename, 'r') as f:
#        reader = csv.reader(f, dialect="excel-tab")
#        your_list = list(reader)
#     data = [[float(long), float(lat), float(age)] for long, lat, _, age in your_list[1:]]
#     return data


# todo: fix problem with variable file name!!!!
# something is wrong with csv.reader
# def get_data_from_tab_separated_file(filename : str):
#     with open(filename, 'r') as f:
#         reader = csv.reader(f, dialect="excel-tab")
#         lines = [[long, lat, age] for long, lat, _, age in parse_lines(reader)]
#         header_lines = lines[0]
#         lines = [[float(long), float(lat), float(age)] for long, lat, age in lines[1:]]
#     return header_lines, lines

