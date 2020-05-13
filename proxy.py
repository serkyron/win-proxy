import _winreg as winreg
import ctypes
import sys
import platform

system = platform.system()

if system != "Windows":
    raise Exception("OS type not supported")

INTERNET_SETTINGS = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
    r'Software\Microsoft\Windows\CurrentVersion\Internet Settings',
    0, winreg.KEY_ALL_ACCESS)

def set_key(name, value):
    _, reg_type = winreg.QueryValueEx(INTERNET_SETTINGS, name)
    winreg.SetValueEx(INTERNET_SETTINGS, name, 0, reg_type, value)

if sys.argv[1] == "off":
	set_key('ProxyEnable', 0)
else:
	set_key('ProxyEnable', 1)
	set_key('ProxyServer', sys.argv[2])

INTERNET_OPTION_REFRESH = 37
INTERNET_OPTION_SETTINGS_CHANGED = 39

internet_set_option = ctypes.windll.Wininet.InternetSetOptionW

internet_set_option(0, INTERNET_OPTION_REFRESH, 0, 0)
internet_set_option(0, INTERNET_OPTION_SETTINGS_CHANGED, 0, 0)