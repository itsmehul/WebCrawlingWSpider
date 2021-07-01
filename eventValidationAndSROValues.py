
from globalValues import CONSTANTS, ROOT_URL
from bs4 import BeautifulSoup
import requests
from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

def getEVENTVALIDATION():
    cookies = {
        'ASP.NET_SessionId': 'App2~3frbx3hprevdp2r1qpyilwvh',
    }

    headers = {
        'Connection': 'keep-alive',
        'sec-ch-ua': '" Not;A Brand";v="99", "Microsoft Edge";v="91", "Chromium";v="91"',
        'Cache-Control': 'no-cache',
        'X-Requested-With': 'XMLHttpRequest',
        'X-MicrosoftAjax': 'Delta=true',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36 Edg/91.0.864.59',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Accept': '*/*',
        'Origin': 'https://freesearchigrservice.maharashtra.gov.in',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://freesearchigrservice.maharashtra.gov.in/',
        'Accept-Language': 'en-IN,en;q=0.9,hi;q=0.8,en-US;q=0.7',
    }

    data = {
    'ScriptManager1': 'UpMain|ddldistrictfordoc',
    '__EVENTTARGET': 'ddldistrictfordoc',
    '__EVENTARGUMENT': '',
    '__LASTFOCUS': '',
    '__VIEWSTATE': CONSTANTS['__VIEWSTATE'],
    '__VIEWSTATEGENERATOR': 'BE9F1233',
    '__EVENTVALIDATION': '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',
    'ddldistrictfordoc': '3',
    'ddlSROName': '----Select SRO ------',
    'ddlYearForDoc': '0',
    'txtDocumentNo': '',
    'TextBox1': '',
    'HiddenField1': '',
    'FS_PropertyNumber': '',
    'FS_IGR_FLAG': '',
    '__ASYNCPOST': 'true'
    }
    
    res = requests.post('https://freesearchigrservice.maharashtra.gov.in/', headers=headers, cookies=cookies, data=data, verify=False)
    soup = BeautifulSoup(res.text, "html.parser")
    # allSROValues = soup.find_all(id="ddldistrictfordoc")
    captchaQuery = soup.find_all(id="imgCaptcha1")[0]['src']
    
    allSROOptions=[]
    select_tag = soup.find("select")
    options = select_tag.find_all("option")
    for option in options:
        allSROOptions.append(option['value'])
    
    decodedRes = res.content.decode()
    indexOfEventVal = decodedRes.index('__EVENTVALIDATION');
    firstIndexOfValue = indexOfEventVal+18
    lastIndexOfValue = decodedRes.index('asyncPostBackControlIDs')-3
    EVENTVALIDATIONVALUE = decodedRes[firstIndexOfValue:lastIndexOfValue]
    
    indexOfEventVal2 = decodedRes.index('__VIEWSTATE');
    firstIndexOfValue2 = indexOfEventVal2+12
    lastIndexOfValue2 = decodedRes.index('__VIEWSTATEGENERATOR')-15
    VIEWSTATE = decodedRes[firstIndexOfValue2:lastIndexOfValue2]

    return {
        '__VIEWSTATE':VIEWSTATE,
        '__EVENTVALIDATION':EVENTVALIDATIONVALUE,
        'options':allSROOptions,
        'captchaUrl': f'{ROOT_URL}{captchaQuery}'
    }
    