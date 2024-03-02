a = int(input("Enter the Value between 2 and 10 :"))
if (a<2 or a>10):
  raise ValueError("Value should be between 2 and 10")