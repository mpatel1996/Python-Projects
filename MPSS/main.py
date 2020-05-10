import random

# get sum of an array 
def getSubSum(a, length):
  arr = []
  currSum = a[length-1]

  n = len(a)
  subSum(a, length, currSum, n, arr)
  
  for i in range(len(arr)):
    arr[i] = round(arr[i], 2)

  # print(arr)
  # return the sum of the array as SL/SR
  return arr

# recursive function to add all numbers in array
def subSum(a, length, currSum, currIndex, arr):
  
  if currIndex == length: 
    arr.append(currSum)
    return subSum(a, length, currSum, currIndex -1 , arr)
  if currIndex < length and currIndex > 0:
    currSum = a[currIndex-1] + currSum
    arr.append(currSum)  
    return subSum(a, length, currSum, currIndex -1 , arr)

def Quicksort_MPSS(alist, start, end, ascending):
  if end - start > 1:
    p = partition(alist, start, end, ascending)
    Quicksort_MPSS(alist, start, p, ascending)
    Quicksort_MPSS(alist, p + 1, end, ascending)

def partition(alist, start, end, ascending):
  pivot = alist[start]
  i = start + 1
  j = end - 1
 
  while True:
    if ascending:
      while (i <= j and alist[i] <= pivot):
        i = i + 1
      while (i <= j and alist[j] >= pivot):
        j = j - 1
    else:
      while (i <= j and alist[i] >= pivot):
        i = i + 1
      while (i <= j and alist[j] <= pivot):
        j = j - 1
    if i <= j:
      alist[i], alist[j] = alist[j], alist[i]
    else:
      alist[start], alist[j] = alist[j], alist[start]
      return j

def Rand(start, end, num):
  a = []
  for j in range(num):
    b=round(random.uniform(start,end), 1)    
    while b in a:
      b=round(random.uniform(start,end), 1)
    a.append(b)
  return a

def split_arry(a):
  half = len(a)//2
  return a[:half], a[half:]

# adds SL and SR together and returns MPSS 
def sumItUp(SL, SR):  
  i = 0 # SL
  j = 0 # SR
  smin = float('inf')
 
  for x in range(len(SL)):
    s = SL[i] + SR[j]   
    if s <= 0:
      i+=1
    elif s < smin:
      smin = s
      j+=1
    elif s > smin:
      j+=1
    if (i == len(SL) or j == len(SR)) and s <= 0:
      smin = SR[0]

  return smin

if __name__ == "__main__":
  for x in range(5):
    print("Test #: ", x)
    # n = int(input("please enter postive integer n:"))
    n = 6
    a = Rand(-20, 20, n)
    # a =  [2, -3, 1, 4, -6, 10, -12, 5.2, 3.6,-8]
    al, ar = split_arry(a) 

    SL = getSubSum(al, len(al))
    SR = getSubSum(ar, len(ar))

    Quicksort_MPSS(SL, 0, len(SL), ascending=True)
    Quicksort_MPSS(SR, 0, len(SR), ascending=False)

    print("Left array: ", al)
    print("Right array: ", ar)

    print("Left sum: ", SL)
    print("Right sum: ", SR)

    MPSS = round(sumItUp(SL, SR), 2)

    if MPSS < 0:
      print('No such number, both array are negative')
    else:
      print("MPSS: ", MPSS)













