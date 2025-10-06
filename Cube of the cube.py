def cube(number):
    return number*number*number
def div_by_three(number):
    if number %3==0:
        return cube(number)
    else:
        return False
print(div_by_three(27))