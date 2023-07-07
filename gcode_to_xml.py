import re
import click
import argparse


def main():



def parse_gcode(filename):

    with open(filename, 'r') as f_gcode:
        # read all lines in a list
        lines = f_gcode.readlines()
        for line in lines:
            # check if string present on a current line
            if line.find(word) != -1:
                print(word, 'string exists in file')
                print('Line Number:', lines.index(line))
                print('Line:', line)
        return value

    print(get_filament_value('test.gcode'))




if __name__ == '__main__':
    main()