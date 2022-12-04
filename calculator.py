firstnum = input("Enter your first number : ")
operator = input("Enter operator (+, -, *, /, %,**,//) : ")
secondnum = input("Enter your second number : ")
first = int(firstnum)
second = int(secondnum)

if operator == "+":
  print("The sum is :", first + second)

elif operator == "-":
  print("The subtraction is :", first - second)

elif operator == "*":
  print("The multiplication is :", first * second)

elif operator == "/":
  print("The division is :", first / second)

elif operator == "%":
  print("The percentage is :", first % second)
elif operator =="**":
  print("The exponential is : ",first**second) 
elif operator =="//":
    print("Tha answer is : ",first//second)

else:
  print("Invalid Input")
