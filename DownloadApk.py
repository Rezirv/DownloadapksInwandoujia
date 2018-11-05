import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
Topath="/home/rezirv/桌面/downloadapks/"
if __name__=='__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) ' 'Chrome/51.0.2704.63 Safari/537.36'
    }
    apk=requests.get('https://www.wandoujia.com/top/app',headers=headers)
    soup=BeautifulSoup(apk.content.decode('utf-8'),'lxml')
    for each_apk in soup.find_all('li',class_='card'):
        myapk=each_apk.find('a',class_='i-source install-btn ')
        if(myapk['href']!=None):
            apk_src=myapk['href']
            apk_name=myapk['data-app-pname']
            apkname=myapk['data-app-name']
            apkpath=Topath+apk_name+".apk"
            urlretrieve(apk_src,apkpath)
            print("下载"+apkname+"完成")
