from pass_gen import *
from restart import restart
from introduction import header
from copy import ask_copy


header("PassGenerator")

swapper = True
while swapper:
    password_finished()
    print("=" * 40)
    print("Your password is:", ''.join(password))
    print("=" * 40)
    ask_copy()
    swapper = restart()
