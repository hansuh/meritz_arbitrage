import urllib
from urllib.request import urlopen
#import numpy as np
#import pandas as pd
#import json
#from bs4 import BeautifulSoup
import re
import requests
import time
import datetime
import pytz
import sys

def getHtmlFile(url,opts,verbose = 0,encoding="utf8"):
    urladdress = url + '?' + urllib.parse.urlencode(opts)
    if(verbose):
        print(urladdress)
    urlstream = urlopen(urladdress)
    htmlfile = urlstream.read().decode(encoding)
    urlstream.close()
    return htmlfile

def getNaverFinance(code,encoding="euc-kr"):
    url = 'https://finance.naver.com/item/main.naver'
    opts = {
         'code':code,
    }
    htmlfile = getHtmlFile(url,opts,encoding=encoding)
    return htmlfile

def getPrice(code):
    htmlfile=getNaverFinance(code)
    #df_list = pd.read_html(htmlfile)
    #df = df_list[1][1:]
    #df.columns = df_list[1].iloc[0]

    #matches = re.findall(r'<div id="middle" class="new_totalinfo">(.+?)</dl>', htmlfile, flags=re.DOTALL)
    matches2 = re.findall(r'현재가(.+?)전일', htmlfile, flags=re.DOTALL)
    return float(matches2[0].replace(',',''))

meritzHoldings="138040"
meritzInsuarances="000060"
meritzSecurities="008560"

exch_rate_ins=1.2657378
exch_rate_sec=0.1607327

thrshld_min=0.028
thrshld_max=0.081

def getDiscountRates():
    price_hol=getPrice(meritzHoldings)
    price_ins=getPrice(meritzInsuarances)
    price_sec=getPrice(meritzSecurities)

    disc_rate_ins = 1 - price_ins/price_hol/exch_rate_ins
    disc_rate_sec = 1 - price_sec/price_hol/exch_rate_sec

    return [disc_rate_ins,disc_rate_sec]

########## Main ##########
if len(sys.argv) < 2:
    argv1=1000
else:
    argv1 = sys.argv[1]
if type(argv1) is not int:
    argv1 = int(argv1)

print("exchange rate for insuarance is " + str(exch_rate_ins))
print("exchange rate for securities is " + str(exch_rate_sec))
print("Running for " + str(argv1) + " times")
print("[insuarance,securities]")
for i in range(argv1):
    #print("discount rates at " + str(datetime.datetime.now(pytz.timezone('Asia/Seoul'))))
    print(getDiscountRates())
    time.sleep(10)