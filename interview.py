# Function that takes string as input.
# Output to be int/float/string depending if the string can be converted to float or integer type
def q2(item):
    try:
        return type(int(item))
    except:
        try:
            return type(float(item))
        except:
            return type(item)


def q3():
    abc = ['dog', 'Fido', 10]
    return '{} the {} is {} years old'.format(abc[1], abc[0], abc[2])

# method that takes 3 numbers as input and finds the minimum of the three
# without using the built- in min function
def q4(a, b, c):
   l = sorted([a, b, c])
   return l[0]


def q5(left_operand, right_operand, operator):
    return eval(str(left_operand + operator + right_operand))
