#module
import os
import ctypes
import sys
#fuction
def get_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def main():
    os.system("net stop Hamachi2Svc && net start Hamachi2Svc")
    input("")
    exit(0)


if get_admin():
    main()
else :
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
