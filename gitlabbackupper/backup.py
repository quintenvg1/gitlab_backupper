import os
os.system("/bin/bash collectslugs.sh")
f = open("projectslugs.txt", 'r')
#this makes sure there will always remain at least one backup on the system.
print("zipping clones directory")
os.system("zip -r clones.zip clones/")
print("clearing clones directory")
os.system("rm -rf clones/*")
print("changing directory to clones")
os.chdir("clones")
print("making backups")
for line in f:
    #line = (line.split(" ")[5].replace(",","").replace('"',"").replace('\n',''))
    os.system("git clone --mirror "+ str(line))
    os.chdir(".")
print("backup created")
