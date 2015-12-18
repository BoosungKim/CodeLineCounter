__author__ = 'kbs0214'

import os
import time


def get_all_extensions(path):
    ret_extensions_list = []

    for each_object in os.scandir(path):
        if each_object.is_dir():
            sibling_path_str = path+'\\'+each_object.name
            ret_extensions_list.extend(get_all_extensions(sibling_path_str))
        else:
            extension_name_str = each_object.name.split('.')[-1]
            ret_extensions_list.append(extension_name_str)

    return list(set(ret_extensions_list))

if __name__ == '__main__':
    start_time = time.time()
    path_name_str = r"D:\MIDAS\CAED trunk"
    all_extensions_list = sorted(get_all_extensions(path_name_str))
    print("# of extensions : %d" % len(all_extensions_list))

    for i in range(len(all_extensions_list)):
        if (i+1) % 10 == 0:
            print()
        else:
            print(all_extensions_list[i], end=' / ')

    print("Elapsed time : %.2f" % (time.time() - start_time))
