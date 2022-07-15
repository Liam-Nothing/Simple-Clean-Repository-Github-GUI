import os
# import shutil

link = input("Link : ")
directory = link.split("/")[-1]
# passw = input("Password path : ")

os.system('cmd /k "git clone --mirror ' + link + ' & exit"')
os.system('cmd /k "bfg-1.14.0.jar --replace-text passwords.txt  ' + directory + ' & exit"')
os.chdir(directory + ".bfg-report")
os.system('cmd /k "git push --force & exit"')
# os.chdir("..")
# shutil.rmtree(os.curdir + "\\" + directory)
# shutil.rmtree(os.curdir + "\\" + directory + ".bfg-report")