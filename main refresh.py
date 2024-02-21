print("Welcome to my calculator project! "
      "You can ask it ant type of equation you like and it will try output an answer")


num1 = int(input("Enter your first number that you would like to use"))
num2 = int(input("Now enter the second number you would like to use"))

method = input("What type of calculation are you trying to carry out?"
               "(Use either Addition, Subtraction, Multiplication or Division)"
               " Use capital letters ")
print("Your final answer is:")
if method == "Addition":
    print(num1 + num2)
elif method == "Subtraction":
    print(num1 - num2)
elif method == "Multiplication":
    print(num1*num2)
elif method == "Division":
    print(num1/num2)


#very simple little calculator. Good task for anyone who is new to python.
#Havent done any python in a while so i thought this would be a nice task to start of with.