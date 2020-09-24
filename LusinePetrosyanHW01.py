allowed_operations={"*","-", "+", "/"}
history = []
while(True):
    print('input x and y (type M to take from History) or input H for history or input Q to quit')
    input1 = input()
    if input1 == 'H':
        if len(history) == 0:
            print('no data in history')
        else:
            for val in history:
                print(val)
    elif input1 == 'Q':
        break
    else:
        input2 = input()
        
        if (input1.isdigit() or input1 == 'M') and (input2.isdigit() or input2 == 'M'):                
            len_history = len(history)
            if input1 == 'M':
                if len_history == 0:
                    x = 0
                else:
                    x = history[len_history - 1]
            else:
                x = int(input1)
            
            if input2 == 'M':
                if len_history == 0:
                    y = 0
                else:   
                    y = history[len_history - 1]
            else:
                y = int(input2)

            print('input operation')
            op = input()
            if op in allowed_operations:
                if op == "*":
                    result = x*y
                elif op == "-":
                    result = x-y
                elif op == "+":
                    result = x+y
                else:
                    result = x/y
                history.append(result)
                print(result)                 
            else:
                print ('unknown operation')
        else:
            print("wrong input")