from globalValues import CONSTANTS, HEADERS
import requests
from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

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


def finalSubmissionRequest(
    rblDocType,
    ddldistrictfordoc,
    ddlSROName,
    ddlYearForDoc,
    txtDocumentNo,
    TextBox1,
    viewstate,
    eventvalidation,
):

    # data = {
    #     "ScriptManager1": "UpMain|btnSearchDoc",
    #     "rblDocType": rblDocType,
    #     "ddldistrictfordoc": ddldistrictfordoc,
    #     "ddlSROName": ddlSROName,
    #     "ddlYearForDoc": ddlYearForDoc,
    #     "txtDocumentNo": txtDocumentNo,
    #     "TextBox1": TextBox1,
    #     "HiddenField1": "",
    #     "FS_PropertyNumber": "",
    #     "FS_IGR_FLAG": "",
    #     "__EVENTTARGET": "",
    #     "__EVENTARGUMENT": "",
    #     "__LASTFOCUS": "",
    #     "__VIEWSTATE": viewstate,
    #     "__VIEWSTATEGENERATOR": "BE9F1233",
    #     "__EVENTVALIDATION": eventvalidation,
    #     "__ASYNCPOST": "true",
    #     "btnSearchDoc": "\u0936\u094B\u0927 / Search",
    # }
    data = {
    'ScriptManager1': 'UpMain|btnSearchDoc',
    'rblDocType': '3',
    'ddldistrictfordoc': '2',
    'ddlSROName': '22',
    'ddlYearForDoc': '2021',
    'txtDocumentNo': '1',
    'TextBox1': 'BCD2AA',
    'HiddenField1': '',
    'FS_PropertyNumber': '',
    'FS_IGR_FLAG': '',
    '__EVENTTARGET': '',
    '__EVENTARGUMENT': '',
    '__LASTFOCUS': '',
    '__VIEWSTATE': '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',
    '__VIEWSTATEGENERATOR': 'BE9F1233',
    '__EVENTVALIDATION': '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',
    '__ASYNCPOST': 'true',
    'btnSearchDoc': '\u0936\u094B\u0927 / Search'
    }

    rsp= requests.post(
        "https://freesearchigrservice.maharashtra.gov.in/",
        headers=headers, cookies=cookies,
        data=data,
        verify=False,
    )

    return rsp