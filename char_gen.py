import random


# Lowwercase letters gen
def gen_0():
    rand_num = chr(random.randint(97, 122))
    return rand_num


# Uppercase letters gen
def gen_1():
    rand_num = chr(random.randint(65, 90))
    return rand_num


# Numbers gen
def gen_2():
    rand_num = chr(random.randint(48, 57))
    return rand_num


# Special characters gen
def gen_3():
    rand_num = chr(random.randint(35, 41))
    return rand_num
