#A simple command line text editor

#coding=utf-8
from sys import argv

script, filename = argv
iterms = []
target = open(filename, 'r+')

try :
    for read_iterm in target.readlines():
        iterms.append(read_iterm)
        print(read_iterm)
    while True:
        iterm = str(input(end = ''))
        if iterm == "":
            break
        iterms.append(iterm + '\n')
        #The end of line
    #write file
    for iterm in iterms:
        target.writelines(iterm)
    print("Save done")
    target.close()
except Exception as e:
    print(e)
