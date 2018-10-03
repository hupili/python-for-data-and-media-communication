import requests
import csv

api_url = 'https://earthquake.usgs.gov/fdsnws/event/1/'
api_method = 'query?'
api_method_2 = 'count?'
api_format = 'format=geojson'
api_starttime = '1918-02-21'
api_endtime = '2018-02-21'
api_minlatitude = '21.821'
api_minlongitude = '119.971'
api_maxlatitude = '25.384'
api_maxlongitude = '122.014'
#设置格式、时间、地区经纬度参数

url = api_url + api_method + api_format + '&' + 'starttime=' + api_starttime + '&' + 'endtime=' + api_endtime + '&' + 'minlatitude=' + api_minlatitude + '&' + 'maxlatitude=' + api_maxlatitude +  '&' +'minlongitude=' + api_minlongitude + '&' + 'maxlongitude=' + api_maxlongitude
#准备使用query功能
url_2 = api_url + api_method_2 + api_format + '&' + 'starttime=' + api_starttime + '&' + 'endtime=' + api_endtime + '&' + 'minlatitude=' + api_minlatitude + '&' + 'maxlatitude=' + api_maxlatitude +  '&' +'minlongitude=' + api_minlongitude + '&' + 'maxlongitude=' + api_maxlongitude
#准备使用count功能
#print(url)

response = requests.get(url)
response_2 = requests.get(url_2)

data = response.json()
count = response_2.json()
print(count) #输出count结果

#print(data)

place = []
mag = []
time = []
for i in range(0,len(data['features'])):
    mag.append(data['features'][i]['properties']['mag'])
    place.append(data['features'][i]['properties']['place'])
    time.append(data['features'][i]['properties']['time'])
#从json格式中提取所需信息

with open('taiwan_earthquake.csv','w',newline='') as f:
    writer = csv.writer(f)
    header = ['place','mag','time']
    writer.writerow(header)
    writer.writerows(zip(place,mag,time))
#将query的结果导入csv
 
