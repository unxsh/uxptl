def arg_pars(args: list) -> int:

    flags: tuple = (
        "-g", "--gen",
        "-v", "--version"
    )

    if len(args) == 1:
        return 0

    elif args[1] in flags[0:2]:
        return 1

    elif args[1] in flags[2:4]:
        return 2

    else:
        return 0
