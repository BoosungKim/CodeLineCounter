import os


def count_lines_in_file(path, filename):
    valid_code_line = 0

    file_url = path + '\\' + filename
    input_file = open(file_url, mode="r")

    for line in input_file.readlines():
        if len(line) > 1:
            valid_code_line += 1

    return valid_code_line

counted_extensions = ["cpp", "h"]


def scan_dir(path):
    ret_code_line = 0

    dirs = [x for x in os.scandir(path) if x.is_dir()]
    files = [x for x in os.scandir(path) if not x.is_dir()]

    # extensions_in_files = set(map(lambda x: x.name.split('.')[-1], files))

    # file 은 line count 바로 하자
    for file in files:
        filename = file.name
        extension = filename.split('.')[-1]
        if extension in counted_extensions:
            ret_code_line += count_lines_in_file(path, filename)
            # print(filename + " : %d" % count_lines_in_file(path, filename))

    # directory 는 recursive 하게 계산 하자
    for dir in dirs:
        # todo :
        pass
    pass



sample_path = r"D:\MIDAS\CAED trunk\src\CAED_db"
sample_filename = r"CAE_mesh.cpp"

# print(count_lines_in_file(sample_path, sample_filename))
print(scan_dir(sample_path))
