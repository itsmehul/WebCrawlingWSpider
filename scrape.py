from bs4 import BeautifulSoup
import requests
from urllib3.exceptions import InsecureRequestWarning
import pytesseract
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

headers = {
             'user-agent': 'Mozilla/5.0 (Windows NT x.y; Win64; x64; rv:10.0) Gecko/20100101 Firefox/10.0'
}

cookies = {
    'ASP.NET_SessionId': 'App2~3frbx3hprevdp2r1qpyilwvh',
}


def getDocumentNumberDetails(rblDocType, ddldistrictfordoc, ddlSROName, ddlYearForDoc, txtDocumentNo):
     with requests.Session() as s:
          url = "https://freesearchigrservice.maharashtra.gov.in/"
          r = s.get(url, headers=headers, verify=False)
          firstTab = BeautifulSoup(r.text, "html.parser")
          
          viewState = firstTab.find_all(id="__VIEWSTATE")[0]['value']
          eventValidation = firstTab.find_all(id="__EVENTVALIDATION")[0]['value']
     
          data = {
               '__EVENTTARGET': 'mnuSearchType',
               '__EVENTARGUMENT': '3',
               '__LASTFOCUS': '',
               '__VIEWSTATEGENERATOR': 'BE9F1233',
               'ddlFromYear': '2021',
               'ddlDistrict': '---Select District----',
               'txtAreaName': '',
               'ddlareaname': '-----Select Area----',
               'txtAttributeValue': '',
               'txtImg': '',
               'FS_PropertyNumber': '',
               'FS_IGR_FLAG': ''
          }
          
          r2 = s.post(url,headers=headers, data={**data, '__VIEWSTATE':viewState,'__EVENTVALIDATION':eventValidation}, cookies=cookies)
          
          secondTab = BeautifulSoup(r2.text, "html.parser")
          
          viewState = secondTab.find_all(id="__VIEWSTATE")[0]['value']
          eventValidation = secondTab.find_all(id="__EVENTVALIDATION")[0]['value']
          
          captchaQuery = secondTab.find_all(id="imgCaptcha1")[0]['src']
          captchaUrl= f'{url}{captchaQuery}'
          
          r3 = s.get(captchaUrl, headers=headers, cookies=cookies)

          with open("test.png", "wb") as f:
               f.write(r3.content)

          captchaText = pytesseract.image_to_string(
               r"/Users/mrgawde/Documents/Projects/ScrappyTest/test.png"
          )
          
          data = {
               'ScriptManager1': 'UpMain|ddldistrictfordoc',
               '__EVENTTARGET': 'ddldistrictfordoc',
               '__EVENTARGUMENT': '',
               '__LASTFOCUS': '',
               '__VIEWSTATE': viewState,
               '__VIEWSTATEGENERATOR': 'BE9F1233',
               '__EVENTVALIDATION': eventValidation,
               'ddldistrictfordoc': ddldistrictfordoc,
               'ddlSROName': '0',
               'ddlYearForDoc': '0',
               'txtDocumentNo': '',
               'TextBox1': '',
               'HiddenField1': '',
               'FS_PropertyNumber': '',
               'FS_IGR_FLAG': '',
               '__ASYNCPOST': 'true'
          }
          
          r4 = s.post(url, headers=headers, cookies=cookies, data=data)
          firstDistrictSoup = BeautifulSoup(r4.text, "html.parser")
          
          allSROOptions=[]
          select_tag = firstDistrictSoup.find_all("select")[1]
          
          options = select_tag.find_all("option")
          for option in options:
               allSROOptions.append(option['value'])

          decodedRes = r4.content.decode()
          indexOfEventVal = decodedRes.index('__EVENTVALIDATION');
          firstIndexOfValue = indexOfEventVal+18
          lastIndexOfValue = decodedRes.index('asyncPostBackControlIDs')-3
          eventValidation = decodedRes[firstIndexOfValue:lastIndexOfValue]

          indexOfEventVal2 = decodedRes.index('__VIEWSTATE');
          firstIndexOfValue2 = indexOfEventVal2+12
          lastIndexOfValue2 = decodedRes.index('__VIEWSTATEGENERATOR')-15
          viewState = decodedRes[firstIndexOfValue2:lastIndexOfValue2]
          
          data = {
               'ScriptManager1': 'UpMain|btnSearchDoc',
               'rblDocType': rblDocType,
               'ddldistrictfordoc': ddldistrictfordoc,
               'ddlSROName': ddlSROName,
               'ddlYearForDoc': ddlYearForDoc,
               'txtDocumentNo': txtDocumentNo,
               'TextBox1': captchaText[0:6],
               'HiddenField1': '',
               'FS_PropertyNumber': '',
               'FS_IGR_FLAG': '',
               '__EVENTTARGET': '',
               '__EVENTARGUMENT': '',
               '__LASTFOCUS': '',
               '__VIEWSTATE': viewState,
               '__VIEWSTATEGENERATOR': 'BE9F1233',
               '__EVENTVALIDATION': eventValidation,
               '__ASYNCPOST': 'true',
               'btnSearchDoc': '\u0936\u094B\u0927 / Search'
          }

          r5= s.post(
               url,
               headers=headers, cookies=cookies,
               data=data,
          )
          finalView = BeautifulSoup(r5.text, "html.parser")
          resultTable = finalView.find_all(id="RegistrationGrid")[0]
          tableHeaders = resultTable.find_all("th")
          tableData = resultTable.find_all("td")
          tableHeaderTexts = []
          for data in tableHeaders:
               tableHeaderTexts.append(data.text)
          
          tableDataTexts = []
          for data in tableData:
               tableDataTexts.append(data.text)
               
          tableHeaderTexts.pop()
          
          record={}
          for th, td in zip(tableHeaderTexts, tableDataTexts):
               record={**record,th:td}
          
          return record
          # return resultTable