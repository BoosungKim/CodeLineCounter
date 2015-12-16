import os


def count_lines_in_file(path, filename):
    valid_code_line = 0

    file_url = path + '\\' + filename
    input_file = open(file_url, mode="r")

    for line in input_file.readlines():
        if len(line) > 1:
            valid_code_line += 1

    return valid_code_line

gonna_counted_extensions = ["cpp", "h"]


def scan_dir(path):
    ret_code_line = 0

    dirs = [x for x in os.scandir(path) if x.is_dir()]
    files = [x for x in os.scandir(path) if not x.is_dir()]

    # extensions_in_files = set(map(lambda x: x.name.split('.')[-1], files))

    # Calculate # of file lines
    for each_file in files:
        extension = each_file.name.split('.')[-1]
        if extension in gonna_counted_extensions:
            ret_code_line += count_lines_in_file(path, each_file.name)
            # print(filename + " : %d" % count_lines_in_file(path, filename))

    # Recursively calculate each directory
    for each_dir in dirs:
        next_path_name = path + '\\' + each_dir.name
        ret_code_line += scan_dir(next_path_name)

    return ret_code_line


if __name__ == '__main__':
    sample_path = r"C:\Users\kbs0214\Desktop\새 폴더"
    # sample_filename = r"CAE_mesh.cpp"
    # print(count_lines_in_file(sample_path, sample_filename))
    print(scan_dir(sample_path))


