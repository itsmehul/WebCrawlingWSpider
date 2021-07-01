from scrape import getDocumentNumberDetails
from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/document")
def crawlFreeSearchigrService(rblDocType:int, ddldistrictfordoc:int, ddlSROName:int, ddlYearForDoc:int, txtDocumentNo:int):
    return getDocumentNumberDetails(rblDocType, ddldistrictfordoc, ddlSROName, ddlYearForDoc, txtDocumentNo)
    # print(res)
    # return 'yo'
