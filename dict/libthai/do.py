import glob
listfileall=list(glob.glob("./*.txt"))
def readfile(path):
 with open(path,"r",encoding="utf-8-sig") as f:
  return [i.strip() for i in f.readlines()]
listword=[]
for j in listfileall:
 listword.extend(readfile(j))

new=list(set(listword))
print(len(new))
del listword
with open("libthai.txt","w",encoding="utf-8") as f:
 f.write('\n'.join(new))