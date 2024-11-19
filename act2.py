def OddOccuring(arr):
  res = 0
  for element in arr:   #when numbers are same xor returns zero else 1
    res = res ^ element  #when the number is xor with zero we get number only
    #print("result= ",res)
  return res

arr = []
n = int(input("Enter array size:"))
while(n):
  num = int(input("Enter number:"))
  arr.append(num)
  n-=1

print("OddOccuring number is",OddOccuring(arr))