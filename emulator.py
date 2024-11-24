######### PYTHON CODE #########


def start():
    init = True
    return run(init)

#Global variables and iterables
inputs = [None] * 4
gatevalues = [None] * 4
outputs = [None] * 4


def run(init):
    global inputs, gatevalues, outputs
    while init:
        #Exception handling for invalid inputs
        try:

            #Capturing user inputs
            print(f'\n\nHello there, enter the value required below to proceed\n\n')
            A1 = int(input(f'Enter the first binary digit for A1: \n'))
            A0 = int(input(f'Enter the second binary digit for A0: \n'))
            B1 = int(input(f'Enter the third binary digit for B1: \n'))
            B0 = int(input(f'Enter the second binary digit for B0: \n'))

            #Validating the inputs as binary digits
            if ((A1 not in [0, 1]) or (A0 not in [0, 1]) or (B1 not in [0, 1]) or (B0 not in [0, 1])):
                print(f'\n\n#########\nInvalid binary digit inputs {A1, A0, B1, B0}. Try again\n#########')
                continue

            #Calling gate functions
            U1(A0, B1)
            U2(A1, B0)
            U4(A1, B1)
            U5(A0, B0)

            #Storing inputs
            inputs[0] = A1
            inputs[1] = A0
            inputs[2] = B1
            inputs[3] = B0

            # #Calling dependent gate functions
            U3(gatevalues[0], gatevalues[1])
            U7(gatevalues[3], gatevalues[2])
            U6(gatevalues[3], gatevalues[2])
            U8(gatevalues[0], gatevalues[1])

            #Calling outcomes
            outcomes()

            #Looping on completion
            init = loop()
            
        #Reaction to invalid inputs
        except ValueError:
            print(f'\n\n#########\nInvalid binary digit inputs {A1, A0, B1, B0}. Try again\n#########')
            continue

######### Independent gates #########

#U1 - AND gate
def U1(A0, B1):
    if A0 == 1 and B1 == 1:
        valueU1 = 1
        gatevalues[0] = valueU1
    else:
        valueU1 = 0
        gatevalues[0] = valueU1

#U2 - AND gate
def U2(A1, B0):
    if A1 == 1 and B0 == 1:
        valueU2 = 1
        gatevalues[1] = valueU2
    else:
        valueU2 = 0
        gatevalues[1] = valueU2

#U4 - AND gate
def U4(A1, B1):
    if A1 == 1 and B1 == 1:
        valueU4 = 1
        gatevalues[2] = valueU4
    else:
        valueU4 = 0
        gatevalues[2] = valueU4


######### Dependent gates #########

#U3 - AND gate
def U3(valueU1, valueU2):
    if (valueU1 and valueU2) == 1:
        valueU3 = 1
        gatevalues[3] = valueU3
    else:
        valueU3 = 0
        gatevalues[3] = valueU3


######### Outcome determinant gates #########

#U5 - AND gate
def U5(A0, B0):
    if A0 == 1 and B0 == 1:
        valueU5 = 1
        outputs[0] = valueU5
    else:
        valueU5 = 0
        outputs[0] = valueU5

#U8 - XOR gate
def U8(valueU1, valueU2):
    if ((valueU1 == 0) and (valueU2 == 0)):
        valueU8 = 0
        outputs[1] = valueU8
    elif((valueU1  == 1) and (valueU2 == 0)):
        valueU8 = 1
        outputs[1] = valueU8
    elif((valueU1 == 0) and (valueU2 == 1)):
        valueU8 = 1
        outputs[1] = valueU8
    elif((valueU1 == 1) and (valueU2 == 1)):
        valueU8 = 0
        outputs[1] = valueU8

#U7 - XOR gate
def U7(valueU3, valueU4):
    if ((valueU3 == 0) or (valueU4 == 0)):
        valueU7 = 0
        outputs[2] = valueU7
    elif ((valueU3 == 1) and (valueU4 == 0)):
        valueU7 = 1
        outputs[2] = valueU7
    elif ((valueU3 == 0) and (valueU4 == 1)):
        valueU7 = 1
        outputs[2] = valueU7
    elif ((valueU3 == 1) and (valueU4 == 1)):
        valueU7 = 0
        outputs[2] = valueU7

#U6 - AND gate
def U6(valueU3, valueU4):
    if (valueU3 and valueU4) == 1:
        valueU6 = 1
        outputs[3] = valueU6
    else:
        valueU6 = 0
        outputs[3] = valueU6

#Solution
def outcomes():
    print('For your entries:\n')
    print(inputs)
    print(f'\nThe truth table for your inputs is:\n')
    print(outputs)

    return loop()

#Loop on completion
def loop():
    loop = str(input(f'\n#########\nEnter new values? (y/n): ')).upper().strip()

    if loop == 'N':
        return False
    else:
        return True

    
#Start the program
start()