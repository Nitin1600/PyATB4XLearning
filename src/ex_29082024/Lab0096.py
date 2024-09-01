# cities = ("London", "Paris", "Los_angeles", "Tokyo")
# print("Paris" in cities)
# print("New_Delhi" in cities)

t = (12,34,56)
# t.append(12)
# print(t)
# my_list =list(t)
# my_list.append(12)
# t = tuple(my_list)
# print(t)
t = t + (4,)
print(t)

# ENV_API_URLS = tuple(["ab.com/get", "xyz.com/post"])
# print(ENV_API_URLS)

list_of_unique_items = {1,2,3,4,4,5,5}
print(list_of_unique_items)

list1 = [45.2, 33, 33, 45, 21]
set1 = set(list1)
print(set1)

t = ("The", "for", "The")
print(t)
print(set(t))

set1 = {1,2,3,4}
set2 = {1,2,3,8}
# set2 = {3,4,5,6}
# my_set = set1.union(set2)
# print(my_set)
# my_set1 = set1.intersection(set2)
# print(my_set1)
# my_set3 = set1.difference(set2)
# print(my_set3)
# my_set4 = set2.difference(set1)
# print(my_set4)
my_set5 = set2.issubset(set1)
print(my_set5)
my_set6 = set1.issubset(set2)
print(my_set6)

print("------------------")
print("------------------")

set1 = set(["The", "for", "The"])
set1.add("Pramod")
set1.add("Pramod")
print(len(set1))
print(set1)
# print(set1[0])

# for i in set1:
#     print(i)

student_infor = {
    "name" : "Amith",
    "age"  :  67,
    "address" : "KA"
}

# student_infor2 = {
#     "name" : "Harish",
#     "age"  :  67,
#     "address" : "KA"
# }
print(student_infor)
print(student_infor["name"])
print(student_infor["age"])
print(student_infor["address"])
student_infor["age"] = 100
# print(student_infor)

student_infor3 = dict(name="Pramod", age=68, address="KA")
print(student_infor3)

student_infor4 = {
    "name" : "Nihal",
    "age" : 22,
    "address" : {
        "home_address" : "Bgk",
        "office_address" : "Blr"
    }
}
student_infor5 = {
    "name" : "Ashok",
    "age" : 70,
    "address" : {
        "home_address" : "Vpr",
        "office_address" : "ND"
    }
}

student_list = [student_infor4, student_infor5]
print(student_list)