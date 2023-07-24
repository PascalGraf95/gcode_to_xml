import re
import click
import argparse
import os
import numpy as np


def main():
    new_gcode = prune_gcode("test_woman.gcode")
    xml_code = convert_to_xml(new_gcode)

    with open(os.path.join("xml", "test_woman3.XML"), 'w') as xml_file:
        xml_file.writelines(xml_code)


def prune_gcode(filename):
    state = 0
    new_gcode = []
    with open(os.path.join("gcode", filename), 'r') as f_gcode:
        # read all lines in a list
        lines = f_gcode.readlines()
        for line in lines:
            if state == 0 and ";MESH" in line:
                state = 1
                continue
            elif state == 1:
                if ("G1" in line and "X" in line) or ("G0" in line and "X" in line):
                    new_gcode.append(line)
                elif "Custom End G-code" in line or "LAYER" in line: # or "MESH" in line:
                    break
    return new_gcode


def extract_gcode_information(gcode):
    keys = [None, None, None, None]
    for idx, (key, sub) in enumerate(zip(keys, ["X", "Y", "Z", "E"])):
        pos = str.find(gcode, sub)
        if pos >= 0:
            empty_pos = [m.start() for m in re.finditer(" ", gcode) if m.start() > pos]
            slash_pos = [m.start() for m in re.finditer("\n", gcode) if m.start() > pos]
            if len(empty_pos):
                keys[idx] = float(gcode[pos+1:empty_pos[0]])
            else:
                keys[idx] = float(gcode[pos+1:slash_pos[0]])
    return keys


def map_to_range(x, old_min, old_max, new_min, new_max):
    return new_min + ((new_max - new_min) / (old_max - old_min)) * (x - old_min)


def calculate_max_scaling_factor(old_min, old_max, new_min, new_max):
    return (new_max - new_min) / (old_max - old_min)


def get_min_max_values(gcode):
    min_x, max_x, min_y, max_y = np.inf, -np.inf, np.inf, -np.inf
    new_min_x, new_max_x, new_min_y, new_max_y = 200, 480, -150, 150
    for idx, line in enumerate(gcode):
        x, y, z, e = extract_gcode_information(line)
        if x and y:
            if x < min_x:
                min_x = x
            if x > max_x:
                max_x = x
            if y < min_y:
                min_y = y
            if y > max_y:
                max_y = y
    print("XMIN/MAX: {:.1f}/{:.1f}, YMIN/MAX: {:.1f}/{:.1f}".format(min_x, max_x, min_y, max_y))
    x_scaling = calculate_max_scaling_factor(min_x, max_x, new_min_x, new_max_x)
    y_scaling = calculate_max_scaling_factor(min_y, max_y, new_min_y, new_max_y)
    print("XSCALING: {:.2f}, YSCALING: {:.2f}".format(x_scaling, y_scaling))

    if x_scaling <= y_scaling:
        scaling_ratio = x_scaling / y_scaling
        updated_min_y = new_min_y + (1 - scaling_ratio) * (new_max_y - new_min_y) * 0.5
        updated_max_y = new_max_y - (1 - scaling_ratio) * (new_max_y - new_min_y) * 0.5
        updated_min_x, updated_max_x = new_min_x, new_max_x
    else:
        scaling_ratio = y_scaling / x_scaling
        updated_min_x = new_min_x + (1 - scaling_ratio) * (new_max_x - new_min_x) * 0.5
        updated_max_x = new_max_x - (1 - scaling_ratio) * (new_max_x - new_min_x) * 0.5
        updated_min_y, updated_max_y = new_min_y, new_max_y
    return min_x, max_x, min_y, max_y, updated_min_x, updated_max_x, updated_min_y, updated_max_y


def convert_to_xml(gcode):
    min_x, max_x, min_y, max_y, updated_min_x, updated_max_x, updated_min_y, updated_max_y = get_min_max_values(gcode)

    xml_code ="<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<Program>\n<Header />\n"
    previous_e, previous_x, previous_y, previous_z = None, None, None, None
    idx = 0
    for line_idx, line in enumerate(gcode):
        x, y, z, e = extract_gcode_information(line)

        if x and y:
            x = map_to_range(x, min_x, max_x, updated_min_x, updated_max_x)
            y = map_to_range(y, min_y, max_y, updated_min_y, updated_max_y)

            if not e or e == previous_e:
                if previous_x and previous_y and previous_e:
                    xml_line = \
"""<Linear AbortCondition="False" Nr="{:d}" Source="Numerical" vel="1500" acc="50" smooth="0" x="{:.3f}" y="{:.3f}" z="{:.3f}" a="180" b="0" c="180" Descr=""/>\n""".format(
                            idx + 1, previous_x, previous_y, 100)
                    xml_code += xml_line
                    idx += 1
                if line_idx < len(gcode)-1:
                    next_line = gcode[line_idx+1]
                    next_x, next_y, next_z, next_e = extract_gcode_information(next_line)
                    if next_e:
                        xml_line = \
"""<Linear AbortCondition="False" Nr="{:d}" Source="Numerical" vel="1500" acc="50" smooth="0" x="{:.3f}" y="{:.3f}" z="{:.3f}" a="180" b="0" c="180" Descr=""/>\n""".format(
                                idx + 1, x, y, 100)
                        xml_code += xml_line
                        idx += 1

                        xml_line = \
"""<Linear AbortCondition="False" Nr="{:d}" Source="Numerical" vel="1500" acc="50" smooth="0.01" x="{:.3f}" y="{:.3f}" z="{:.3f}" a="180" b="0" c="180" Descr=""/>\n""".format(
                                idx + 1, x, y, 50)
                        xml_code += xml_line
                        idx += 1
            else:
                xml_line =\
"""<Linear AbortCondition="False" Nr="{:d}" Source="Numerical" vel="1500" acc="50" smooth="0.01" x="{:.3f}" y="{:.3f}" z="{:.3f}" a="180" b="0" c="180" Descr=""/>\n""".format(
    idx+1, x, y, 50)
                xml_code += xml_line
                idx += 1
        previous_e, previous_x, previous_y, previous_z = e, x, y, z
    xml_code += """</Program>"""

    return xml_code







if __name__ == '__main__':
    main()