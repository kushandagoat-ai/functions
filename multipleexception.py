try:
    num1, num2 = eval(input("enter two numbers, seperated by comma:"))
    result = num1/num2
    print("the result is", result)
except ZeroDivisionError:
    print("division by zero is error!")
except SyntaxError:
    print("Comma is missing, ENter numbers seperated bt comma Like this: 1,2")

except:
    print("wrong input")

else: 
    print("No esceptions")

finally: 
    print("This will execute no matter what")