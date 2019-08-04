# -*- coding: utf-8 -*-
from pythainlp.util import collate
import glob
import re
files = [f for f in glob.glob("./dict/*.txt", recursive=True)]
word_all=[]
def isThai(chr):
    for i in chr:
        cVal = ord(i)
        if(cVal >= 3584 and cVal <= 3711):
            pass
        elif i==" " or i==".": # ข้อยกเว้น
            pass
        else:
            return False
    return True
def clean(word):
    if (len(word)>1 
        and isThai(word)
        and "\t" not in word
        and ".." not in word
        and word.startswith("์") == False
        and word.isdecimal() == False 
        and word.isnumeric() == False
        and word.isspace() == False 
        and word.isdigit() == False
        and re.search(r'[^0-9a-zA-Z|^\d+?\.\d+?$]',word)):
        return True
    return False
for i in files:
    with open(i,"r",encoding="utf-8-sig", errors='ignore') as f:
        word_all.extend([j.strip().replace("[","").replace("]","") for j in f.readlines()])
word_all = collate([i for i in list(set(word_all)) if clean(i)])
print(len(word_all))
with open("wordlist.txt","w",encoding="utf-8") as f:
    f.write("\n".join(word_all))