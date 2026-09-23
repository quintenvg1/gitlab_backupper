targetserver = "git@gitlab.local:user/"
import os
os.chdir("clones")
projects = os.listdir()
for project in projects:
    #print(project)
    link = targetserver + str(project)
    print(link)
    os.chdir(str(project))
    os.system("git push --mirror "+ str(link))
    #print(os.system("pwd"))
    os.chdir("../")
