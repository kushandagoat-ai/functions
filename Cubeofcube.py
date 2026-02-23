def cube(Number):
    return Number*Number*Number
def by_three(Number):
    if Number %3 ==0:
        return cube(Number)
    else:
        return False
print(by_three(9))
print(by_three(4))