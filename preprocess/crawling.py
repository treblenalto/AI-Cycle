from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urlib.request

driver = webdriver.Chrome()
driver.get("https:/www.google.co.kr/imghp?hl=kd&tab=ri&ogbl")
elem = driver.find_element_by_name("q")
elem.send_keys("플라스틱 병")
elem.send_keys(Keys.RERURN)

SCOLL-PAUSE_TIME = 1.5

#Get scroll height

last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    #scroll down to bottom
    sriver.ececute_script("widow.scrollto(0, document.body.scrollHeight);")

    #wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    #calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if newheight= last_height:
    try:
     driver.find_elem_by_css_selector(".mye4qd").click()

    except:
        break
    last_height= new_height


images = driver.find_elements_by_css_selector(".rg.i.Q4Luwd")
count = 1
for image in images:
    try:
        image.click()
        time.sleep(3)
        imgUrl = driver.find_elemt_by_xpath("/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[2]/div[1]/a/img").get_attribute("src")
        urlib.request.urlretrieve(imgUrl, str(count) + ".jpg")
        count = count +1

    except:
        pass

driver.close()


