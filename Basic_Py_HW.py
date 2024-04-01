# Rockwell Wright

import os
from pathlib import Path




#Part 1

#part 1
working_directory = os.getcwd()
print(working_directory)

#part 2
working_directory2 = Path.cwd()
print(working_directory2)

#Part 3
working_directory2 = Path(working_directory)
print(working_directory2)

#Part 4
home_directory = Path.home()
print(home_directory)

#Part 5
home_directory2 = os.path.expanduser("~")
print(home_directory2)


#-----------------------------------------------------------------------------------------------------------------------

#Part 2

#Part 1
sample_vlans = [2, 22, 55, 3, 1, 2, 55, 89, 1, 2, 3, 9, 22, 4, 3, 1, 2, 55, 9, 11]
fixed = set(sample_vlans)
print(fixed)

#Part 2
sorted(fixed)
print(fixed)

#Part 3
fixed_2 = []
for i in fixed:
    i = str(i)
    fixed_2.append(i)
print(fixed_2)

#Part 4
fixed_3 = ','.join(fixed_2)
print(fixed_3)

#Part 5
fixed_4 = fixed_3 + ' switchport trunk allowed vlan'
print(fixed_4)

#-----------------------------------------------------------------------------------------------------------------------

#Part 3

celsius_temp = float(input("Please input temperature in Celsius:"))

def celsius_to_fahrenheit(celsius_temp):
    if celsius_temp < 0:
        return("Temperatures may not fall below absolute zero")
    else:
        fahrenheit = (celsius_temp * (9/5)) + 32
        return (fahrenheit)

fahrenheit = celsius_to_fahrenheit(celsius_temp)

print(fahrenheit)


#-----------------------------------------------------------------------------------------------------------------------


#Part 4


import sys
address = str(input("Please input an IPv4 address: "))

def ipv4_to_binary(address):
    octect = address.split(sep='.')

    for i in octect:
        try:
            octect_value = int(i)
        except ValueError:
            raise ValueError("Your octect contains a non numeric octect and will present further errors")

    first, second, third, fourth = int(octect[0]), int(octect[1]), int(octect [2]), int(octect[3])
    octects = int(octect[0]), int(octect[1]), int(octect [2]), int(octect[3])
    for i in octects:
        if i < 0 or i > 256:
            raise(ValueError("IPv4 adress octet should be between 0 and 255, one of your octets is out of range"))


    if len(octect) !=4:
        print(ValueError("You need four octects for a valid IP address, your IP address is not valid and will not display correctly below"))
    return first,second,third,fourth

first,second,third,fourth = ipv4_to_binary(address)


first = bin(first)
second = bin(second)
third = bin(third)
fourth = bin(fourth)

first = first[2:]
second = second[2:]
third = third[2:]
fourth = fourth[2:]

print("Your octet entered in binary format is", first,second,third,fourth)


#-----------------------------------------------------------------------------------------------------------------------

#Part 5

import random

def random_ephemeral_port(seed_value=None, lower_bound=49152, upper_bound=65535):
    
    random_number = random.randint(lower_bound, upper_bound)
    
    if random_number < 49152:
        print(ValueError("Value out of range",random_number))

    elif random_number > 65535:
        print(ValueError("Value out of range",random_number))

    else:
        return random_number

random_number = random_ephemeral_port()
print("Random value of", random_number)
