# browser_name = input("Enter the name of the browser: \n")
# # browser_name =browser_name.upper()
# match browser_name:
#     case "firefox":
#         print("Execute the firefox code")
#     case "chrome":
#         print("Execute the chrome code")
#     case "edge":
#         print("Execute the edge code")
#     case "safari":
#         print("Execute the safari code")
#     case _:
#         print("Browser not found!")

user_type = input("Enter the user type,admin,manager,guest\n")
match user_type:
    case "admin" | "manager":
        print("Hello Sir")
    case "guest":
        print("Hello Guest")
    case _:
        print("Hello, There!")