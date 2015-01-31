fin = open("code", "r")
filestr = fin.read().replace("<", "&lt;").replace(">", "&gt;").replace("\t", "&nbsp;&nbsp;&nbsp;&nbsp;").replace("\n", "\n<br>");
fin.close()
fout = open("code", "w")
fout.write(filestr);
fout.close()
