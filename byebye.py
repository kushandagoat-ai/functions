
Valid = False
while not Valid:
        try: 
            n = int(input("Enter a number:"))
            while n%2 == 0:

                print("Bye bye")
            valid=True
        except ValueError:
             print("This is not Valid") 