lines = int(input("how many lines in the code ?"))
f = open("monFichierScratch.py","w+")
tab = 0

for i in range(0,lines):
    toWrite = input("line "+str(i+1)+" ? ")
    if 'if' in toWrite or 'else' in toWrite or 'for' in toWrite or 'while' in toWrite or 'elif' in toWrite:
        f.write("\n"+tab*"\t" + toWrite)
        tab = tab+1
    elif 'endOfLoop' == toWrite:
        tab = tab-1
    elif tab > 0:
        f.write("\n"+tab*"\t"+toWrite)
    else:
        f.write("\n"+toWrite)

f.close()

import monFichierScratch

