import requests
from bs4 import BeautifulSoup
import re
import wget
import os
import shutil
import numpy as np
#make variables
p='.csv'
#requests.get(Website)
result=requests.get("https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_daily_reports")
src=result.content
#web scraping
soup=BeautifulSoup(src,"lxml")
name_csv=soup.find_all("a",{"class":"js-navigation-open Link--primary"})
name_csv_list=[name_csv[i].text for i in range(len(name_csv))]
name_csv_final=[i for i in name_csv_list if p in i]
#make variables
save_folder_Worksheet=R'C:\Users\Lenovo\Desktop\CSV'
Archiving=('.rar','.zip')
Worksheet=('.csv')
Images=('.png','.jpg')
name=['CSV']
#create folder
name_folder= np.array(name)
for y in name_folder :
      if not os.path.exists(f'{y}') :
            os.mkdir(fR'C:\Users\Lenovo\Desktop\{y}')
#download file in github           
for x in range (len(name_csv_final)):
      #print(x,name_csv_final[x])
      if not os.path.isfile(fR'C:\Users\Lenovo\Desktop\CSV\{name_csv_final[x]}'):
                  download_data_Worksheet=wget.download(f'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/{name_csv_final[x]}',save_folder_Worksheet)
                  print(f'download_file_{name_csv_final[x]},{x}')
      else :
            print(f'read_file_{name_csv_final[x]},{x}')
