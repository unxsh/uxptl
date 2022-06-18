def arg_pars(args: list) -> int:

    flags: tuple = (
        "-g", "--gen",
        "-m", "--move",
        "-s", "--activate",
        "-v", "--version"
    )

    if len(args) == 1:
        return 0

    elif args[1] in flags[0:2]:
        return 1

    elif args[1] in flags[2:4]:
        return 2

    elif args[1] in flags[4:6]:
        return 3

    elif args[1] in flags[6:8]:
        return 4

    else:
        return 0
