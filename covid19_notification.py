from plyer import notification
import requests
from bs4 import BeautifulSoup
import time
def notifyMe(title, message):
    notification.notify(
        title=title,
        message=message,
        app_icon='C:/Users/Shubham/Downloads/icons.ico',
        timeout=15
    )

def getData(url):
    r = requests.get(url)
    return r.text

if __name__ == '__main__':
    
    while True:
        # notifyMe("Shubham", "Let's stop the spread of this Virus!!")
        myHtmlData = getData('https://www.mohfw.gov.in/')

        soup = BeautifulSoup(myHtmlData, 'html.parser')
        # print(soup.prettify())
        myDataStr = ''
        for tr in soup.find_all('table'):
            myDataStr += tr.get_text()
        # myDataStr = myDataStr[1:]
        itemList = myDataStr.split('\n\n')
        states = ['Bihar', 'Delhi', 'Maharashtra']
        for item in itemList[3:38]:
            item = item[1:]
            dataList = item.split('\n')
            # print(dataList)
            if dataList[1] in states:
                print(dataList)
                nTitle = 'Cases of Covid-19'
                nText = f"State: {dataList[1]} \nActv: {dataList[2]} \nRcvrd: {dataList[3]} & Dcsd: {dataList[4]} \nCnfrmd: {dataList[5]}"
                notifyMe(nTitle, nText)
                time.sleep(5)
        time.sleep(100)
