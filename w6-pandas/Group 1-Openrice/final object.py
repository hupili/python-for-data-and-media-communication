
# coding: utf-8

# In[ ]:


import requests
import bs4
import csv


# In[ ]:


from bs4 import BeautifulSoup


# In[1]:


def clean(x):
    return x.text.strip()

def get_the_page(url):
    r = requests.get(url,headers={'user-agent':'Mozilla/5.0'})
    mypage = BeautifulSoup(r.text)
    title = mypage.find_all('h2')
    
    like=mypage.find_all('span',attrs={'class':'score score-big highlight'})
    
    locations=mypage.find_all('div',attrs={'class':'icon-info address'})
    location=[]
    for itemm in locations:
        location.append(itemm.find_all('a'))

    price = []
    myprices = mypage.find_all('div',attrs={'class': 'icon-info icon-info-food-price'})
    for i in myprices:
        price.append(i.find('span'))

    countries_materials=mypage.find_all("ul",attrs={'class':'pois-categoryui-list'})
    country_material=[]
    for item in countries_materials:
        country_material.append(item.find_all('li'))

    country=[]
    material=[]
    for items in country_material:
        country.append(items[0])
        if len(items)>1:
            material.append(items[1])
        else:
            material.append(items[0])   

    page_content=[]    
    for number in range(0,len(title)):
        page_content.append([clean(title[number]),clean(location[number][0]),clean(price[number]),clean(country[number]),clean(material[number]),clean(like[number])])
        
    return page_content


# In[ ]:


url_page1='https://www.openrice.com/zh/hongkong/restaurants?Seat=2&BookingDate=2018-02-22&TimeSlot=23%3A30'
page1=get_the_page(url_page1)
page1



# In[ ]:


page_next=[]
for q in range(1,17):
    page_number=str(q+1)
    url_next=url_page1 + "&page=" + page_number
    page_next.extend(get_the_page(url_next))
    
page_all=page1+page_next
page_all


# In[ ]:


with open('daisy.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',',
                            #quotechar='"', quoting=csv.QUOTE_MINIMAL)
                            quotechar='"')
    spamwriter.writerows(page_all)
    
    


# In[ ]:




