# # # # student_names=["first_name","second_name","third_value"]
# # # # print(len(student_names))
# # # # print(student_names[0])
# # # # print(student_names[0:2])

# # # abc=["Hash",23,1.3,"Include",True]
# # # efg=["hello","People","Community"]
# # # # Methods
# # # # abc.append(False)
# # # # for x in abc:
# # # #     print (x)

# # # # print (len(abc))

# # # # # Remove by value
# # # # abc.remove(23)
# # # # print(abc)

# # # # remove by index
# # # # abc.pop(0)
# # # # print(abc)
# # # # abc.insert(0,"python community")
# # # # print(abc)

# # # final_list=abc+efg
# # # # print(final_list)
# # # num_list=[912,67,9,45690,234]
# # # num_list.sort()
# # # # print(num_list)

# # # num_list.reverse()
# # # print(num_list)
# # # print(num_list.index(234))

# # # #extend lists
# # # #list 1, list2  --> list1.extend(list2)

# # str="Hash"
# # print(str[0])

# #Tuple

# # fam_aadhar=(12345,5645,9845,577234)
# # fam_aadhar[0]=989484

# # list1=[]
# # print(list)

# tup1=(12345,)
# print(tup1)

#nodifying data value in a tuple
veg=("Avocado","Zucini","Spinach","Tomato","Potato")
veg1=list(veg)
veg1[0]="Asp"
veg=tuple(veg1)
print(veg)