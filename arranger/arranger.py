#takes a function with a number, an operand (+/-), and another number and returns it in an arithmetically arranged format


def arranger(functions):
    first = []
    operators = []
    second = []
    solns = []
    top,middle,lines,bottom = str(),str(),str(),str()
    iterations = len(functions)
    countup=0
    for item in functions:
        components = item.split()
#assigning values
        no1 = components[0]
        operand = components[1]
        no2 = components[2]
#Ensuring only 4 digit addition/subtraction takes place
        if len(no1) > 4 or len(no2) > 4:
            print('Numbers must be less than 4 digits')
            continue
#determining solutions. if the operand isn't a + or a -, the function prints out an error message and continues with the rest of the expressions
        soln = None
        if str(operand) == '+':
            soln = int(no1) + int(no2)
        elif str(operand) == '-':
            soln = int(no1) -  int(no2)
        else:
            print('Not a valid operand')
            continue
        distance = max(len(no1), len(no2)) + 2
#adding the components to lists
        first.append(no1)
        operators.append(operand)
        second.append(no2)
        solns.append(soln)
#Add every component to a string in order with spaces inbetween using a while loop
        countdown=iterations-1
        while countdown > (iterations-2):
            top,bottom = top + str(first[countup]).rjust(distance) + '  ', bottom + str(solns[countup]).rjust(distance) + '  '
            middle = middle + str(operators[countup]) + str(second[countup]).rjust(distance-1) + '  '
            lines = lines + ('-' * distance) + '  '
            countdown=countdown - 1
            countup+= 1      
    print(top.rstrip())
    print(middle.rstrip())
    print(lines.rstrip())
    print(bottom.rstrip())

