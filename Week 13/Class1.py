'''

value = input ("Welcome to the menu. options are listed below:  \n\t 1. Roll \n\t 2.Sweep \n\t 3.Scroll \n Type the number of your choice and press enter.")

print ("The value you input is:", value)
print (f'it is of type {type(value)}.')

while True:
    if value.isdigit() == True:    # .isdigigt ()
        value = int(value)
        break  #on correct value dataype : exit the loop      
    else:
        value=input("invalid input, please provide an integer:")  #ask for a new value


print ("The converted is:", value)
print (f'it is of type {type(value)}.')



value = input("Welcome to the menu. Options are listed below:",
              "\n\t 1. Roll \n\t 2. Sweep \n\t 3. Scroll \n Type the",
              "number of your choice and press Enter.") #\n - newline; \t - tab

'''

value = input('''Welcome to the menu. Options are listed below:,
              \t 1.Roll
              \t 2. Sweep
              \t 3. Scroll
              Type the number of your choice and press Enter.''') #\n - newline; \t - tab

#print("The value you input is:", value)
#print(f'it is of type {type(value)}.')

def func1(val):
    return val**val
def func2(val):
    return val**val
def func3(val):
    return val**val

while True:
    if value.isdigit() == True: # .isdigit() 
        value=input("invalid input, please provide an integer:") #ask for a new value
        if value > 3 and value <1:  #if value is outside of or range
            value = input ("Please input a number between 1 and 3.")
            continue   #skip rest of loop, start from isdgigt() check again
        else:
            break  #on correct value datatype: exist the loop
    else:
        value=input("Invalid input, please provide an integer:")  #ask for a new value


#print("The converted is:", value)
#print(f'it is of type {type(value)}.')

#compare numeric value to choices available, perform assicoated function or sequence.
if value == 1:
    print(func1(value))
elif value == 2:
    print(func2(value))
elif value == 3:
    print(func3(value))

if value > 3 or value <1:  #if value is outside of or range
    value = input ("Please input a number between 1 and 3.")
