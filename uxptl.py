from os import system as sh
from sys import argv
from assets.asset import greeting, helpmsg
from flags import arg_pars
from funcs import gen_service

print(greeting)

args: int = arg_pars(argv)

if args == 1:
    gen_service()

elif args == 2:
    print("-m", "--move")

elif args == 3:
    print("-s", "--activate")

elif args == 4:
    print("-v", "--version")

else:
    print(helpmsg)
