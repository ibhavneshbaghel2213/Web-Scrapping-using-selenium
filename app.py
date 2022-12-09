import json
from selenium import webdriver
from selenium.webdriver.common.by import By

site_url = "https://www.iomfsa.im/enforcement/disqualified-directors/"


def data_extractor_from_driver(list_of_driver):
    '''
    This is the function for Extracting data from remote selenium drivers
    '''
    content_of_the_sites = []
    for i in range(len(list_of_driver)):
        list_of_driver[i].click()
        j = i+1
        content_of_the_sites.append(client.find_element(by=By.XPATH, value=f"/html/body/div[3]/div/div/section[{j}]/div").text)
    return content_of_the_sites





def feature_selector(content_of_site) :
    '''
    This is the function for transforming the raw data into structured data
    '''
    l = []
    for i in range(len(content_of_site)):
        r = []
        for k in content_of_site[i].split("\n"):
            if "Name" in k.split(":"):
                r.extend(k.split(":"))
            elif "Address (at date of disqualification)" in k.split(":"):
                r.extend(k.split(":"))
            elif "Date of Birth" in k.split(":"):
                r.extend(k.split(":"))
            elif "Period of Disqualification" in k.split(":"):
                r.extend(k.split(":"))
            elif "Dates of Disqualification" in k.split(":"):
                r.extend(k.split(":"))
        l.append(r)
    return l



def list_to_dict(k) :
    dic = []
    for m in k:
        x= {}
        for n in range(len(m)-1):
            if n%2==0:
                x.update({m[n]:m[n+1]})
        dic.append(x)
    return dic




def Json_file_maker(result):
    with open("disqualified_directors.json","w") as f:
        json.dump(result,f)




try:
    client = webdriver.Chrome()
    client.get(site_url)
    content = client.find_elements(by=By.XPATH, value="//*[@class='accordion-item']")
    content_of_site = data_extractor_from_driver(content)
    features = feature_selector(content_of_site)
    result = list_to_dict(features)
    Json_file_maker(result)
except Exception as E:
    print(E)
finally:
    client.close()













        












