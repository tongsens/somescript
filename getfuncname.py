__author__ = 'Administrator'

import os,sys
import re
pdb_list = []
pat_name = re.compile(r'\w{4,30}')
func_list = []

def getpdb(path):
    try:
        file = os.listdir(path)
    except:
        print "there is no path", path
        return
    for fe in file:
        pat = os.path.join(path, fe)
        if "pdb" in fe:
            pdb_list.append(pat)
        if os.path.isdir(pat):
            getpdb(pat)

def getfuncname(filepath, keyword):
    with open(filepath, 'rb') as fp:
        buf = fp.read()
    res = pat_name.findall(buf)
    if res:
        for func_name in res:
            if keyword in func_name:
                if func_name not in func_list:
                    func_list.append(func_name)


if __name__ == "__main__":
    if len(sys.argv)!=3:
        print "usage: getfuncname.py filepath keyword"
        exit()
    filepath = sys.argv[1]
    keyword = sys.argv[2]
    getpdb(filepath)
    for file in pdb_list:
        getfuncname(file, keyword)
        #os.system("pause")
    for func_name in func_list:
        print func_name
