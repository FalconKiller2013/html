import os
import platform
def shutdown():
    confirm = input("Are you sure you want to shut down the computer? (yes/no): ").strip().lower()
    if confirm == "yes":
        current_os = platform.system()
        if current_os == "Windows":
            os.system("shutdown /s /t 1")
        elif current_os == "Linux" or current_os == "Darwin":
            os.system("sudo shutdown now")
        else:
            print("Unsupported operating system.")
    else:
        print("Shutdown canceled.")
shutdown()