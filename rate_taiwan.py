from selenium import webdriver
#from bs4 import BeautifulSoup


driver=webdriver.Chrome(executable_path="./chromedriver.exe") #("c:/Users/user/chromedriver.exe")
driver.get("https://www.taiwanlife.com/Rate/Public")

list1=[driver.find_element_by_id('page-selection').text]
long=len(list1[0])-11

list1=[driver.find_element_by_id('page-selection').text]
long=len(list1[0])-11

print(driver.find_element_by_id('content').text)
for i in range(2,long):   
    i=str(i)    
    driver.find_element_by_link_text(i).click()
    print(driver.find_element_by_id('content').text)
#list1=[driver.find_element_by_id('page-selection').text]
#long=len(list1[0])-11
#
#print(driver.find_element_by_id('content').text)
#for i in range(2,long):   
#    i=str(i)    
#    driver.find_element_by_link_text(i).click()
#    print(driver.find_element_by_id('content').text)
    


#bs=BeautifulSoup(driver.page_source,"html.parser")
#
#tds=bs.find_all("td")
#
#for td in tds:
#    
#    print(td.contents[0])

#pyinstaller -F rate_taiwan.py

driver.close()