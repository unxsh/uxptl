
<h1 align="center">
  🦾 UXPTL - systemd service file generator 🦾
</h1>

```





                   _--------------------------------------------------------------------------_
                  |                                                                            |
                  |                _------------------------_-----_-_                          |
                  |               |  _   _  __  __  _ __   | |_  | | |                         |
                  |               | | | | | \ \/ / | '_ \  | __| | | |                         |
                  |               | | |_| |  >  <  | |_) | | |_  | | |                         |
                  |               |  \__,_| /_/\_\ | .__/   \__| |_| |                         |
                  |               |                |_|               |                         |
                  |                `--------------------------------`                          |
                  |                                                                            |
                  |          _--------------------------------------_                          |
                  |         | uxptl - systemd service file generator |                         |
                  |          `--------------------------------------`                          |
                  |       _------------------------------------------------------------_       |
                  |      | argv                     | description                       |      |
                  |      |--------------------------|-----------------------------------|      |
                  |      | -g, --gen                | generate new serive file          |      |
                  |      | -h, --help               | print this massage                |      |
                  |      | -v, --version            | print program version             |      |
                  |       `------------------------------------------------------------`       |
                  |                                               _--------------------_       |
                  |                                              | by @unxsh            |      |
                  |                                              | maintainer: @ssleert |      |
                  |                                              | ssleert@gmail.com    |      |
                  |                                               `--------------------`       |
                  |                                                                            |
                   `--------------------------------------------------------------------------`





```
<h1 align="center">
🧙‍♂️ another useless utility by sfome 🧙‍♂️
</h1>
<h3 align="center">
 🌈 thx wegtx for idea 🌈
</h3>

<br>



# ❓ How to `BUILD` & `INSTALL` ❓

### 1) preparing
```fish
git clone https://github.com/unxsh/uxptl.git
cd uxptl/
```
### 2) installing dependencies 📦
### dep list
```
nuitka
python >= 3.8
```
- why *`nuitka`*? 🦭
- cuz it's simpliest python compiler
```fish
python -m pip install nuitka
```
### 3) Building or installing 💠
### 3.1) `building` 🏗️
```fish
./build.py build
```
#### After the build, you will get a *`binary`* file in the *`build/`* directory

### 3.2) `installing` ⛓️
```fish
./build.py install
```
#### After installation you will get a *`binary`* file in the `PATH` env variable




<br>
<br>

<h1 align="center">
    🌳 file architecture 🌳
</h1>

```
.
├── assets
│   ├── asset.py
│   └── __init__.py
├── build.py
├── flags.py
├── funcs.py
├── README.md
└── uxptl.py

1 directory, 7 files
```
