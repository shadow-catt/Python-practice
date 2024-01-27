from selenium import webdriver
import time
def getText():
    txt = open("1.txt","r",encoding='UTF-8').read()
    for char in '''\n ''':
        txt = txt.replace(char, " ")
    txt = txt.replace('-', "")
    return txt
org = getText()
driver=webdriver.Chrome()
driver.get("https://translate.google.cn/")
English=driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div/div/div[1]/textarea")
English.send_keys(org)
time.sleep(6)
China=driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/div[3]/div[1]/div[1]/div[2]/div[3]/div[1]/div[2]/div/span[1]")
org=China.text
after = open("2.txt", "a",encoding='UTF-8')
m=0
for i in org:
    m+=1
    if(m%60==0):
        after.write('\n'+i)
    else:
        after.write(i)
after.close()
driver.close()
print("transfer done~")
