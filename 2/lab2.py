
# print("\n----------------- t1: ----------------    ")
# def in_range(num, start, end):
#     return start <= num <= end    #return num >= start and num <= end

# print(in_range(2,1,4))
# print(in_range(-2,1,4))

# print("\n----------------- t2: ----------------    ")
# list1 = ['a','b','c']
# list2 = [1,2,3]
# def dict_to_lists(d):
#  keys = list(d.keys())
#  values = list(d.values())
#  return keys, values
# k, v = dict_to_lists({'a': 1, 'b': 2, 'c': 3})   # return 2 values  
# print(k) # ['a', 'b', 'c']
# print(v) # [1, 2, 3]
# dictionary =dict(zip(list1,list2))
# print(dictionary)

# print("\n----------------- t3: ----------------    ")
# def fun3_1():
#     my_list=[]
#     for i in range(1, 31):
#         my_list.append(i*2)
#     print(my_list)
    
# def fun3_2():
#    my_list2= [x*2 for x in range(1, 31)]
#    print(my_list2)
       
# fun3_1()
# fun3_2()

# print("\n----------------- t4: ----------------    ")
# test_list= [3, 6, 4, 0, 8] 
# print(test_list)
# test_list.pop()
# print(test_list)
# test_list.insert(3,'R')
# print(test_list)
# num= int(input(f"enter an number from {test_list}:"))
# print(f"you choosed :{num}")
# if num in test_list:
#     test_list.remove(num)
#     print(test_list)
# else:
#     print("number out of list ! ")
    
 
print("\n----------------- t5: ----------------    ")
dict1 = {
    "name": "Ali",
    "age": 22
}

dict2 = {
    "city": "Cairo",
    "job": "Engineer"
}

dict1.update(dict2)

print(dict1)
#or
print({**dict1, **dict2})