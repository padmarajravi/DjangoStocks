import csv
from datetime import date,timedelta
import urllib
import django
import os
import pandas as pd
import io
import time
import requests

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoexp.settings")
django.setup()

from djangostocks.models import Stocks,Company

class Downloader:

    def download(self):
        details               = {}
        details['end_date']   = date.today()
        details['start_date'] = date.today().__sub__(timedelta(days=2))
        with open("/home/ravi/Downloads/EQUITY_L.csv") as stockCsv:
            stockList = csv.reader(stockCsv)
            next(stockList,None) # Skipping the header
            for row in stockList:
                time.sleep(1)
                details['stock']=str(row[0]).replace("-","_")
                url = "https://www.quandl.com/api/v3/datasets/NSE/{stock}.csv?start_date={start_date}&end_date={end_date}&api_key=QsqQbjfywXuJyWd5HpAs".format(**details)
                print url
                try:
                    response = urllib.urlopen(url)
                    priceList = csv.reader(response.read().decode('utf-8').splitlines())
                    next(priceList,None)
                    company,created = Company.objects.get_or_create(full_name=details['stock'])
                    for row in priceList:
                        priceForDate= Stocks.objects.filter(company=company,date=row[0]).count()
                        if(priceForDate==0):
                            Stocks.objects.create(company=company,date=row[0],open=row[1],high=row[2],low=row[3],close=row[5],trade_value=row[7],trade_volume=row[6])
                except Exception as e :
                    print company.full_name+":"+str(e)



        print "Download complete"




def main():
    downloader = Downloader()
    downloader.download()


if __name__ == '__main__': main()


