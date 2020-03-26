from bs4 import BeautifulSoup
import requests
from datetime import datetime
import numpy as np
import pandas as pd
import os

url = "https://www.who.int/emergencies/diseases/novel-coronavirus-2019/situation-reports"

response = requests.get(url)

soup = BeautifulSoup(response.content, "lxml")

raw_list = []
date_num = len("/docs/default-source/coronaviruse/situation-reports/")
report_num = len("/docs/default-source/coronaviruse/situation-reports/20200228-sitrep-")

t = soup.find_all("a")
for i in t:
  if "coronaviruse" in i.get('href'):
    b = i.get('href')
    raw_list.append(b)

raw_set = set(raw_list)
report_list = []

try:
  os.mkdir(path = os.environ['HOME'] + "/Downloads/covid_situation_reports")
except:
  pass

l = os.listdir("/Users/phaniksv/Downloads/covid_situation_reports")

dir_path = os.environ['HOME'] + "/Downloads/covid_situation_reports/"

for i in raw_set:
  d = "situation_report_" + i[report_num:report_num+2].replace("-", "") + "_" + i[date_num:date_num+8]
  r = requests.get("https://www.who.int" + i)
  with open(dir_path + d + ".pdf", 'wb') as f:
    if f not in l:
      f.write(r.content)

print("WHO Covid situation reports are available in Downloads >> covid_situation_reports folder")





