from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_experimental_option('prefs', {
"plugins.always_open_pdf_externally" : True,
"download.prompt_for_download": False, #To auto download the file
})

driver = webdriver.Chrome(options=options)
driver.get('https://www.isuzu-tis.com/')
time.sleep(2)

dmax_list = []
for data in driver.find_elements(By.XPATH,'//div[@class="row"]//a[@title=""][@class="col-md-3 chil-menu-content__item"]')[0:5] :
    dmax_list.append(data.get_attribute('href'))

for dmax in dmax_list :
    driver.get(dmax)
    driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[1]/div/div/div/div/div[1]/div/ul/li[2]').click() #Select type of D-max
    time.sleep(3)
    
    driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[1]/div/div/div/div/div[1]/div/ul/li[2]/div[2]').click()
    time.sleep(1)
    
    driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div/div/div/section[3]/div/div/div/div[2]/div/div/div/div[2]/div[4]/div/div[2]/a').click() #Download PDF
    time.sleep(3)