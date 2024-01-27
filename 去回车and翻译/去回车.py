def getText():
    txt = open("1.txt","r",encoding="UTF-8").read()
    for char in '''\n—''':
        txt = txt.replace(char," ")
    txt = txt.replace('-',"")
    return txt

org = getText()
after = open("2.txt","w")
after.write(org)
after.close()
print("transfer done~")
