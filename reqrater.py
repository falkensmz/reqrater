# very simple python script to automate the process of creating and installing requirement files for python scripts
# written by falkensmz : https://github.com/falkensmz
import os

choice = input("Are you in the same file directory as the python script?(y/N) > ")
if choice == 'y' or choice == 'Y':
    print("Creating the requirements file ... ")
    os.system("pip3 freeze > requirements.txt")
    print("Installing the requirements on your system ... ")
    os.system("pip3 install -r requirements.txt")
    print("[+] Successfully installed the requirements on your system ")
elif choice == 'n' or choice == 'N':
    file_path = input("Enter the file path directory > ")
    print("Attempting to navigate to the file directory ... ")
    try:
        os.chdir(file_path)
        print("Creating requirements file ... ")
        os.system("pip3 freeze > requirements.txt")
        print("Installing the requirements on your system ... ")
        os.system("pip3 install -r requirements.txt")
        print("[+] Successfully installed the requirements on your system ")
    except Exception as e:
        print(f"Error: {e}")
else:
    print("[-] Invalid answer")
