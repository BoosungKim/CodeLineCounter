import os
import time
import locale
import sys

gonna_counted_extensions = ["cpp", "h", "hpp"]


def count_lines_in_file(path, filename):
    valid_code_line = 0

    file_url = path + '\\' + filename
    input_file = open(file_url, mode="rt", encoding="utf-8", errors="ignore")

    try:
        for line in input_file.readlines():
            if len(line) > 1:
                valid_code_line += 1
    except UnicodeDecodeError as e:
        print(filename, e)

    return valid_code_line


def scan_dir_for_count_loc(path):
    ret_code_line = 0

    dirs = [x for x in os.scandir(path) if x.is_dir()]
    files = [x for x in os.scandir(path) if not x.is_dir()]

    # Calculate # of file lines
    for each_file in files:
        extension = each_file.name.split('.')[-1]
        if extension in gonna_counted_extensions:
            ret_code_line += count_lines_in_file(path, each_file.name)

    # Recursively calculate each directory
    for each_dir in dirs:
        next_path_name = path + '\\' + each_dir.name
        ret_code_line += scan_dir_for_count_loc(next_path_name)

    return ret_code_line


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage => \CodeLineCounter.py path1 path2 ...")
    else:
        total_loc_int = 0
        start_time = time.time()

        for i in range(1, len(sys.argv)):
            path_name_str = sys.argv[i]
            loc_int = scan_dir_for_count_loc(path_name_str)
            print(path_name_str, " : ", loc_int)
            total_loc_int += loc_int

        locale.setlocale(locale.LC_ALL, "")
        print("Total LOC : " + locale.format("%d", total_loc_int, grouping=True))
        print("Elapsed time : %.2f" % (time.time() - start_time))