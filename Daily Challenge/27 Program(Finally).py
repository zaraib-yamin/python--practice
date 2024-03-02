def func1():
  try:
    l = [1,2,3,4,5,78,5,45,34,7,57,3,4]
    i = int(input(("Enter the number :")))
    print(l[i])
    return 1
  except :
    print("Some error occurred")
    return 0
  finally :
    print("I am always Executed")
x = func1()
print(x)
    