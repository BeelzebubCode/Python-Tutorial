import os
import platform

def shutdown():
    if platform.system() == "Windows":
        os.system("shutdown /s /t 1")
    elif platform.system() == "Linux" or platform.system() == "Darwin":  # Darwin สำหรับ macOS
        os.system("shutdown -h now")
    else:
        print("Unsupported OS")

def restart():
    if platform.system() == "Windows":
        os.system("shutdown /r /t 1")
    elif platform.system() == "Linux" or platform.system() == "Darwin":
        os.system("shutdown -r now")
    else:
        print("Unsupported OS")

option = input("Enter s to shut down and r to restart: ").lower()
if option == "s":
    shutdown()
elif option == "r":
    restart()
else:
    print(f"{option} not in the options")