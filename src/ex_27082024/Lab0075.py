# my_shopping_list = ["Bread", "Butter", "Milk"]
# print(my_shopping_list[0])
# print(len(my_shopping_list))
#
# def bring_more_food(my_list):
#     more_item = input("Enter the item: \n")
#     # my_list.append(more_item)
#     # my_list.remove(more_item)
#     my_list.insert(0, more_item)
#     # my_list.append("Cheese")
#     return my_list
#
# l = bring_more_food(my_shopping_list)
# print(l)

# def my_decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called")
#         print("Dashcash", "Guard", "Helmet", "Blower")
#         func()
#         print("Something is happening after the function is called")
#         print("Secure driving")
#
#     return wrapper()
#
#     # my_decorator(func)
# def drive_bike():
#         print("I am driving")
#
# drive_bike()

# def drive_scooty():
#     print("Normal_driving")
# drive_scooty()

def add_before_and_after_ui_testcase():
    def wrapper():
        print("Before running ui testcase")
        print("start the browser")
        print("Ending the running ui testcase")
        print("quit the browser")
    return wrapper()

def test_ui():
    print("I will test the ui")

test_ui()
add_before_and_after_ui_testcase(func)




