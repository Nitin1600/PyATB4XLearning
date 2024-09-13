# import Lab172_1
#
# Lab172_1.greet("Alice")
#
# person = Lab172_1.Person("Bob")
# person.introduce()

# import numpy as np
#
# arr = np.array([1,2,3,4,5])
# print(arr)


# import Lab172_1.module1
# from Lab172_1.module2 import some_function
#
# my_package.module1.function1()
# some_function()

# import Lab172_1
#
# response =Lab172_1.get('https://www.sd.live/become')
# print(response.status_code)

# from collections import Counter
# cnt = Counter()
# for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
#     cnt[word] += 1
# print(cnt)

from collections import OrderedDict
d = OrderedDict()
d['a'] = 'A'
d['b'] = 'B'
d['c'] = 'C'
for key, value in d.items():
    print(key, value)
