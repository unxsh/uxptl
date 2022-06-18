version: str = "0.1"
greeting: str = """
     _------------------------_-----_-_
    |  _   _  __  __  _ __   | |_  | | |
    | | | | | \ \/ / | '_ \  | __| | | |
    | | |_| |  >  <  | |_) | | |_  | | |
    |  \__,_| /_/\_\ | .__/   \__| |_| |
    |                |_|               |
     `--------------------------------`
"""
helpmsg: str = """   _--------------------------------------_
  | uxptl - systemd service file generator |
   `--------------------------------------`
  _------------------------------------------------------------_
 | argv                     | description                       |
 |--------------------------|-----------------------------------|
 | -g, --gen                | generate new serive file          |
 | -h, --help               | print this massage                |
 | -v, --version            | print program version             |
  `------------------------------------------------------------`
                                          _--------------------_
                                         | by @unxsh            |
                                         | maintainer: @ssleert |
                                         | ssleert@gmail.com    |
                                          `--------------------`
"""
serv_name: str = """     _------------_
    | service name |
     `------------`"""
serv_disc: str = """     _-------------------_
    | service description |
     `-------------------`"""
serv_usr: str = """     _------------_
    | service user |
     `------------`"""
serv_dir: str = """     _-------------------_
    | service working dir |
     `-------------------`"""
serv_exec: str = """     _------------_
    | service exec |
     `------------`"""
serv_restart: str = """     _---------------------_
    | service must restart? |
     `---------------------`"""
serv_gen: str = """\033[32m      _-----------------_
     | service generated |
      `-----------------`\033[37m"""
serv_move: str = """     _----------------------------_
    | move service in systemd dir? |
     `----------------------------`"""
serv_act: str = """     _-----------------_
    | activate service? |
     `-----------------`"""
