# _*_ coding=utf-8 _*_
import requests
import csv


#执行API调用并储存相应
url = 'https://api.douban.com/v2/movie/in_theaters'
r = requests.get(url)

# print("Status code:",r.status_code)

#将API响应存储在一个变量中
response_dicts = r.json()

# #处理结果
# print(response_dicts.keys())

# #获取跟subjects有关的信息
# print("Total subjects:",response_dicts['subjects'])

#获取subjects中信息
repo_dicts = response_dicts['subjects']
# print("subjects returned:",len(repo_dicts))

#获取第一个subjects信息
# repo_dict = repo_dicts[0]
# print("\nKeys:",len(repo_dict))
# for key in sorted(repo_dict.keys()):
#     print(key)
title = []
collect_count = []
genres = []
id = []
original_title = []
rating = []
subtype = []
year = []

for repo_dict in repo_dicts:
    title.append(repo_dict['title'])
    collect_count.append(repo_dict['collect_count'])
    genres.append(repo_dict['genres'])
    id.append(repo_dict['id'])
    original_title.append(repo_dict['original_title'])
    rating.append(repo_dict['rating'])
    subtype.append(repo_dict['subtype'])
    year.append(repo_dict['year'])

with open('douban.csv','w') as f:
	writer = csv.writer(f)
	writer.writerows(zip(title,collect_count,genres,id,original_title,rating,subtype,year))
