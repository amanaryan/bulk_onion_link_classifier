import requests
import json
from bs4 import BeautifulSoup
import csv

#Change the name of the inputfile as required
domain_list = "list.txt"

#Change the name of the output file as required
output_file = "output.csv"

#Change the port of the socks proxy as stated in the TOR borwser's configuration
proxies = {
    'http': 'socks5h://127.0.0.1:9150',
    'https': 'socks5h://127.0.0.1:9150'
}


with open(output_file,'a+') as out:
    with open(domain_list,'r') as thelist:
        for item in thelist:
            try:
                r  = requests.get(item,proxies=proxies)
                soup = BeautifulSoup(r.text,"html.parser")
                t = soup.find('title')
                #Feel free to add more lines here to extract more information from the response
                print "%s, TITLE: %s"%(item.strip(),t.text)
                writer = csv.writer(out)
                data = [item.strip(),t.text]
                writer.writerow(data)
            except Exception as e:
                pass
