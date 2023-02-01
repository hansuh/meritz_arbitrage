import urllib
from urllib.request import urlopen
import re
import requests
import time
import datetime
import pytz

# Insuarance merger schedule
# 2023-02-01 end of trading + 2 days
# 2023-02-23 issuance of new shares

# Securities merger schedule
# 2023-04-05 end of trading + 2 days
# 2023-04-25 issuance of new shares

# This version of the file is for monitoring after Feb 2023 until (after the merger of insuarance)
# python3.8 /home/hankyulsuh/meritz-pyanywhere-feb2023.py
# Meritz discounts monitoring3

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
meritzSecurities="008560"

exch_rate_sec=0.1607327

thrshld_min=0.048
thrshld_max=0.081

def getDiscountRates(price_hol,price_sec):

    disc_rate_sec = 1 - price_sec/price_hol/exch_rate_sec

    return (disc_rate_sec,)

def send_email_alert(subject,text):
    print("Set your email API", flush=True)
    return
#     return requests.post(
#         "https://api.mailgun.net/.../",
#         auth=("api", "YOUR-API-KEY"),
#         data={"from": "YOUR-API-SERVICE",
#             "to": "RECIEPENT@EMAIL.COM",
#             "subject": subject,
#             "text": text})

#send_email_alert("[Meritz]test","This is a test message at " + str(datetime.datetime.now(pytz.timezone('Asia/Seoul'))))
prev_time = None
while(True):
    current_time = datetime.datetime.now(pytz.timezone('Asia/Seoul'))
    if current_time.weekday()<5 and current_time.hour>=9 and current_time.hour<16 :

        #Fetch data and calculate discount rates
        price_hol=getPrice(meritzHoldings)
        price_sec=getPrice(meritzSecurities)

        (disc_rate_sec,)=getDiscountRates(price_hol,price_sec)

        #Print out the data
        text=""
        text+="======="+str(datetime.datetime.now(pytz.timezone('Asia/Seoul')))+"=======\n"
        text+="["+str(int(price_hol))+","+"NoIns"+","+str(int(price_sec))+"]\n"
        text+="disc_rate_sec=%.4f" % (100*disc_rate_sec) + "%"
        print(text, flush=True)

        #See if the drs are out of the thresholds
        title="[Meritz]"

        if disc_rate_sec<thrshld_min:
            title+="SEC EXPENSIVE "
        elif disc_rate_sec>thrshld_max:
            title+="SEC CHEAP "

        #If true, send an email alert and sleep an hour. If not check it again after a min.
        if len(title)>8:
            #Send an email alert if previous alert was sent more than an hour ago
            if (prev_time is None) or (current_time-prev_time).total_seconds()>3600:
                prev_time=current_time
                send_email_alert(title,"This is an arbitrage trading alert.\n"+text)
                print("Alert sent out!", flush=True)
        
        #Sleep for a min
        time.sleep(60)

    else:
        #Run it until this year
        # if current_time.year>2022:
        #     print(current_time,"\tHappy New Year!", flush=True)
        #     break

        if current_time.year!=2023 or current_time.month<2 or current_time.month>=4:
            print(current_time,"\tBye bye!", flush=True)
            break

        #If the market hour is done wait until the next 9am
        wtime=((9-current_time.hour)%24)*3600-current_time.minute*60
        if(wtime<0):
            wtime+=24*3600
        elif(wtime<60):
            wtime+=60
        print(current_time,"\tWaiting for the next 9am - %.4f hours" % (wtime/3600), flush=True)

        time.sleep(wtime)
