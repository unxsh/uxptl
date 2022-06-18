from shutil import move
from assets.asset import serv_name, serv_disc, serv_usr, serv_dir, serv_exec, serv_restart, serv_gen, serv_move, serv_act


def gen_service() -> None:

    print(serv_name)
    service_name: str = input(":")
    print(" example: cpupower")
    print()

    print(serv_disc)
    service_disc: str = input(":")
    print()

    print(serv_usr)
    service_usr: str = input(":")
    print()

    print(serv_dir)
    service_dir: str = input(":")
    print()

    print(serv_exec)
    service_exec: str = input(":")
    print()

    print(serv_restart)
    service_restart: str = input(":")
    print()

    print()
    print(serv_gen)
    print()

    print()
    print(serv_move)
    print(" 1) \033[32mYes\033[37m")
    print(" 0) \033[31mNo\033[37m")
    service_move: int = int(input(":"))

    print()
    print(serv_act)
    print(" 1) \033[32mYes\033[37m")
    print(" 0) \033[31mNo\033[37m")
    service_act: int = int(input(":"))
