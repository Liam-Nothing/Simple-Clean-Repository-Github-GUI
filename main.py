import os

link = input("Link : ")
directory = link.split("/")[-1]
# passw = input("Password path : ")

os.system('cmd /k "git clone --mirror ' + link + ' & exit"')
os.system('cmd /k "bfg-1.14.0.jar --replace-text passwords.txt  ' + directory + ' & exit"')
os.rmdir(directory)