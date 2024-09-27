# Capstone Design I

## How To Start
### Create Virtual Environment
시작에 앞서 Windows Powershell 또는 Bash 창에서 해당 프로젝트 폴더에 잘 들어왔는지 체크한다.
```shell
# Windows
py -m venv venv
. venv/Scripts/activate
pip3 install -r requirements.txt
py bootstrap.py

# MacOS
python3 -m venv venv
. venv/bin/activate
pip3 install -r requirements.txt
python3 bootstrap.py
```