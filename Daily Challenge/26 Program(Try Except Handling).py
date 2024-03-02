a = input("Enter the number you want to multiplication :")
print(f"Multiplication table of {a} is : ")
try:
  for i in range (1,21):
    print(f"{int(a)} x {i} = {int(a)*i}")
except:
  print("Invalid input!")
print("Continue the Code")