import os

full_path_file = os.path.join("/Users/nitingpa/PycharmProjects/PyATB4XLearning/src/Sept2024/ex_10092024/Pra", "pramod.txt")

file = open(full_path_file, 'r')
content = file.read()
print(content)