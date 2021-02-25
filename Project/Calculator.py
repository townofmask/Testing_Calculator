from Calc import calculatim

operands = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ',', '.')
znaki = ('+', '-', '*', '/','(', ')')

class Calculator:
    def calculate(self, s):
        buffer = ''
        sign = 1
        s = s.replace(' ', '')
        s = s.replace(',', '.')
        s = s.replace('(-', '(0-')                                              
        s = s.replace('(((', '(1*(1*(') 
        s = s.replace('((', '(1*(')
        s = s.replace(')-(', ')-1*(')    
        stack_num = []
        stack_znaki = []
        metod = 1
        minus = 0
        
        if s[0] in operands and s[1] == '-' and s[2] == '(':
            if len(s) >= 2:
                s = s[:0] + '0' + s[0:]
                minus = 1
        
        for element in s:
            if element in operands:
                if sign == -1:
                    element = int(element) * int(sign)
                    element = str(element)
                    sign = 1
                    if buffer == '':
                        buffer = element
                    else: 
                        buffer += element
                elif buffer == '':
                    buffer = element
                else:
                    buffer += element
                
                
            elif element in znaki:
                metod = 1
                if element == '-':
                    if minus != 1:
                        sign = -1
                        element = "+"
                    minus = 0
                if element == ')':
                    metod = 2
                    if buffer != '':
                        stack_num.append(buffer)
                    buffer = ''
                    znak = ''
                    while znak != '(':
                        znak = stack_znaki.pop()
                        if znak == '(':
                            break
                        a, b = stack_num.pop(), stack_num.pop()
                        a, b = float(b), float(a)
                        result = calculatim(znak,a,b) 
                        stack_num.append(result)
                    metod = 1
                else:            
                    stack_znaki.append(element)
                    if buffer != '':
                        stack_num.append(buffer)
                        buffer = ''
        
        if metod == 1:
            if buffer != '':
                stack_num.append(buffer)
                buffer = ''
            while stack_znaki != []:
                a, b = stack_num.pop(), stack_num.pop()
                znak = stack_znaki.pop()
                a, b = float(b), float(a)
                result = calculatim(znak,a,b)
                stack_num.append(result)
        result = stack_num.pop()
        return result

def str_check(user_input):
    ch = ""
    zn = 0
    oper = 0
    invalid_check = 0
    brackets_check = 0
    stack_check = []

    for m in user_input:
        if m not in znaki and m not in operands:
            invalid_check = 1
    
    if user_input == " ":
        invalid_check = 1

    if user_input == "":
        invalid_check = 1

    if user_input[len(user_input)-1] in ['+', '-', '*', '/'] or user_input[len(user_input)-1] == '(':
            invalid_check = 1
    
    if user_input[0] in ['+', '-', '*', '/'] and len(user_input) == 1:
        invalid_check = 1

    if invalid_check != 1:
        if user_input[0] == '-' and (user_input[1] in operands or user_input[1] == '('):
            if len(user_input) >= 2:
                user_input = user_input[:0] + '0' + user_input[0:]

    for m in user_input:
        if m == '(':
            continue
        elif m == ')':
            continue
        if m in operands:
            oper += 1
        if oper == 0:
            invalid_check = 1

    if m in operands:
        for m in user_input:
            if m == '(':
                continue
            elif m == ')':
                continue
            if m in znaki:
                zn = 1
                break
        if zn != 1:
            invalid_check = 1

    for m in user_input:
        if m == '(':
            brackets_check += 1
        elif m == ')':
            brackets_check -= 1
    if brackets_check < 0:
        invalid_check = 1
    elif brackets_check > 0:
        invalid_check = 1

    for m in user_input:
        if m == '(':
            stack_check.append(m)
        elif m == ')':
            stack_check.append(m)
        elif m in operands:
            stack_check = []
            break
        elif m in ['+', '-', '*', '/']:
            stack_check = []
            break
    if stack_check == ['(', ')']:
            stack_check = []
            invalid_check = 1

    if invalid_check == 1:
        print('Invalid expression!')

    if invalid_check != 1:        
        print(user_input + ' = ...Launching')
        output = calc.calculate(user_input)
        print(output)

print("Launching...")
calc = Calculator()
user_input = ""
while user_input not in ["exit"]:
    user_input = input("> ")
    if user_input == 'exit':
        break
    str_check(user_input)
print("Closing...")
