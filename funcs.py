from assets.asset import serv_name, serv_disc, serv_usr, serv_dir, serv_exec, serv_restart, serv_gen, serv_move, serv_act
from os import system as sh


def gen_service() -> None:

    def yn() -> None:
        print(" 1) \033[32mYes\033[37m")
        print(" 0) \033[31mNo\033[37m")

    print(serv_name)
    print(" example: cpupower")
    service_name: str = input(":")
    print()

    print(serv_disc)
    service_disc: str = input(":")
    print()

    print(serv_usr)
    print(" example: root")
    service_usr: str = input(":")
    print()

    print(serv_dir)
    print(" example: /")
    service_dir: str = input(":")
    print()

    print(serv_exec)
    service_exec: str = input(":")
    print()

    print(serv_restart)
    yn()
    service_restart: int = int(input(":"))
    print()

    if service_restart:
        serv: str = f"[Unit]\nDescription={service_disc}\n\n[Service]\nUser={service_usr}\nWorkingDirectory={service_dir}\nExecStart={service_exec}\nRestart=always\n\n[Install]\nWantedBy=multi-user.target"
        with open(f"{service_name}.service", "w") as f:
            f.write(serv)

    else:
        serv_null: str = f"[Unit]\nDescription={service_disc}\n\n[Service]\nUser={service_usr}\nWorkingDirectory={service_dir}\nExecStart={service_exec}\n\n[Install]\nWantedBy=multi-user.target"
        with open(f"{service_name}.service", "w") as f:
            f.write(serv_null)

    print()
    print(serv_gen)
    print()

    print()
    print(serv_move)
    yn()
    service_move: int = int(input(":"))

    if service_move:
        sh(f"sudo mv {service_name}.service /etc/systemd/system/")

        print()
        print(serv_act)
        yn()
        service_act: int = int(input(":"))

        if service_act:
            sh(f"sudo systemctl enable --now {service_name}")
            print("\033c")

        else:
            pass
            print("\033c")

    else:
        pass
        print("\033c")
