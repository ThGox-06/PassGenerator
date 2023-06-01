from char_gen import *


# Setting limits
password = []


def pass_gen_0():
    password.append(gen_0())


def pass_gen_1():
    password.append(gen_1())


def pass_gen_2():
    password.append(gen_2())


def pass_gen_3():
    password.append(gen_3())


def password_finished():
    password.clear()
    for i in range(4):
        pass_gen_0()
        pass_gen_1()
        pass_gen_2()
        pass_gen_3()
