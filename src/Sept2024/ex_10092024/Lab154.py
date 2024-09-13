#try,except and finally
#file

import os
try:
    full_path = os.getcwd()
    full_path_file = full_path + "/example.txt"
    print(full_path_file)

    file = open(full_path_file, 'r')
    print(file.open())
except Exception as fnfe:
    print("FilenotfoundError. Please fix the path or create a file")
finally:
    try:
        file.close()
    except NameError as ne:
        print(ne)