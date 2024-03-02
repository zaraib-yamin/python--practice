def average(*numbers):
  sum = 0
  for i in numbers :
    sum = sum + i 
    #print("Average is:",sum/len(numbers))
  return(sum/len(numbers))
#average(5,6,7,1)
c = average(5,6,7,1)
print(c)