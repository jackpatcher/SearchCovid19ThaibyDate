#COVID-19 Search Data by Code Am
import requests,json,time

searchDate = '04/12/2021';
rp = json.loads(requests.get('https://covid19.th-stat.com/api/open/timeline').text)

for i in range(len(rp['Data'])) :
    find = rp['Data'][i]
    if(find['Date'] == searchDate ):
        print(find['NewConfirmed'])

time.sleep(5)
