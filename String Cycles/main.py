global edge
global used 
global in_order

def cycle(arr, word_b, n):  
  for n in range(len(arr)): 
    word_a = arr[n]
    if word_b == word_a:
      pass
    
    if word_b[-1] == word_a[0]:
      if edge[arr.index(word_b)] == '':
        edge[arr.index(word_b)] = arr.index(word_a) 
        in_order.append(arr[n])
        word_b = arr[arr.index(word_a)]

        if '' in edge:              
          return cycle(arr, word_b, n+1)
        break

def is_cycle(arr):
  return "NO!" if arr.__contains__('') else "YES!"
  
arr = ['abc','hij','khl','cde','jba','efg','ghk','ljh']
arr1 = ['ba', 'ab', 'xy','yx'] 
arr2 = ["soup", "hey", "yes", "push"]

word_b = arr[0]
edge = [''] * len(arr) # [ , , , ]
in_order = []
counter = 0
cycle(arr, word_b, counter)
print(arr, is_cycle(edge))
print(in_order)

# Keep everything above this

# # Test array Delete everything after this later
# word_b = arr1[0]
# counter = 0
# edge = [''] * len(arr1) # [ , , , ]
# cycle(arr1, word_b,counter)
# print(arr1, is_cycle(edge))

# word_b = arr2[0]
# counter = 0
# edge = [''] * len(arr2) # [ , , , ]
# cycle(arr2, word_b,counter)
# print(arr2, is_cycle(edge))



