import random

def humidity() :
    value = random.randint( 50,100)
    return value
def temperature() :
    value1 = random.randint(0,50)
    return value1


def write_to_file(values,filename):
    with open('data.txt', 'w') as file:
        for value in values :


            file.write(str(value)+ "\n")

def turn_on_AC():
    return 1
