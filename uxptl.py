from sys import argv
from assets.asset import greeting, helpmsg, version
from flags import arg_pars
from funcs import gen_service


def main() -> None:
    args: int = arg_pars(argv)

    if args == 1:
        print(greeting)
        gen_service()

    elif args == 2:
        print("\n", "uxptl -", version, "\n")

    else:
        print(greeting)
        print(helpmsg)


if __name__ == "__main__":
    main()
