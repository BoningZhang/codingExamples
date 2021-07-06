# !!! Number here is number of leetcode problem

# 1
# i. enumerate()
for i, num in enumerate(nums):
    print(i, num)


# 15
# i. sorted(), sort()
arr = [1, 3, 2]
sorted[arr] # return a sorted array
arr.sort()  # arr is sorted
# There is no sort() method for string
"132".sort()    # AttributeError: 'str' object has no attribute 'sort'

sorted("132")   # ["1", "2", "3"]
# so in order to sort string
"".join(sorted("132"))

# 17
# i. add to array
arr = [1, 2, 3]
arr.append(4)

# ii. add to set
test = set([1, 2, 3])
test.add(4)

# 20
# i. remove element from list, list.pop(index), index=-1 by default
arr = [1, 2, 3]
arr.pop()   # remove the last element
arr.pop(0)  # remove the first element

# ii. remove element from set
test = set([1, 2, 3])
test.remove(1)
test.remove(4)  # 4 is not in test, raise valueError
test.discard(4) # nothing to do, no Exception


# 39
# i. list is copy by reference
arrs = []
arr = [1, 2, 3]

arrs.append(arr[:])

import copy
arrs.append(copy.deepcopy(arr))


# 43
# i. range() to generate 5 to 0
range(5, -1, -1)
# not
range(5, 0, -1)


# 47
# i. create an array with n elements
arr = [False]*n

# 50
# i. recursion in class method, need to add self
class Solution:
    def myPow(self, x: float, n: int) -> float:
        return self.myPow()
#
