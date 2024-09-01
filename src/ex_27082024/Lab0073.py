# from msilib import make_id
#
#
# def make_pizza(*toppings):
#     for topin in toppings:
#         print(topin)
#
# print("programme started")
# amith = make_pizza("tomato", "mushroom", "ginger")
# dhirr = make_pizza("garlic", "ginger")
# yukthi = make_pizza("carrot", "onion", "cheese")
# print("programme ended")

# r = min(1,2,3,4,5,6)
# print(r)

def make_pizza(*toppings, base):
    print(toppings, base)
    
amith = make_pizza("mushroom", "garlic", "ginger", base="thin crust")