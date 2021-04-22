from bs4 import BeautifulSoup
import requests
urllist = input("Enter Your Url of online Khabar'English':")
naming = input ("Enter your Naming Convaction:")

url = BeautifulSoup(urllist,'html.parser')
response = requests.get(url)
data = response.text
soup = BeautifulSoup(data,'lxml')
link = soup.find_all("a")
linklist = []
for links in link:
    a=links.get("href")
    if "https" in a:
        if "category" in a:
            continue
        else:
            if "/english.onlinekhabar.com/" in a:
               # print(a)
                linklist.append(a)
            else:
                continue
                
g=int(input("Enter the number you want to start with:"))
for k in linklist:
    url2 = BeautifulSoup(k,'html.parser')
    response2 = requests.get(url2)
    data2 = response2.text
    soup = BeautifulSoup(data2,'lxml')
    link2= soup.find_all("p",text=True)
    for link4 in link2:
        a = link4.get_text()
        if "|" in a:
            continue
        else:
            if "Your email address will not be published." in a:
                continue
            else:
                b = str(g)+naming+".txt"
                file = open(b,'a')
                file.write(a)
                file.close()

    print("\n")
    g=g+1
    