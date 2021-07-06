# !!! Number here is number of leetcode problem

# 1
# i. append to dictioinary
test = {}
test["key"] = "val"

# However if "key" is not in the dictionary, then we cannot refer to it on the right side of =
val = test["key1"] # this will raise keyError Exception

# ii. no add/push/append function for dictionary


# 49
# i. dictionary.items()
for key, val in dict.items():
    print(key, val)

for key in dict.keys():
    print(key)

print dict.values()


#
