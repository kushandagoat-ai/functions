def add(p, q):
    return p + q
def subtract(p, q):
    return p-q
def multiply(p, q):
    return p*q
def divide(p,q):
    return p/q
print("Select which one you want")
print("Option A: add")
print("Option b: subtract")
print("Option c multiply")
print("Option d divide")
choice = input("Enter your choice (a/b/c/d/)")
num_1 = int(input("which number you want for first one?"))
num_2 = int(input("The second one?"))
if choice == 'a':
    print(num_1, "+", num_2, "=", add(num_1, num_2))
elif choice == 'b':
    print(num_1, "-", num_2, '=', subtract(num_1, num_2))
elif choice == 'c':
    print(num_1, "*", num_2, "=", multiply(num_1, num_2))
elif choice == 'd':
    print(num_1, "/", num_2, "=", divide(num_1, num_2))
    
else: 
    print("This is an invalid choice")
