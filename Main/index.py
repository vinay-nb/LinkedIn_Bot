import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys




options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(chrome_options=options)

#enter the link 
driver.get("https://www.linkedin.com/")

# hitting signin 
signin = driver.find_element_by_xpath("/html/body/nav/a[3]")
signin.click()

#waits for some time 
driver.implicitly_wait(40)

username = driver.find_element_by_xpath('//*[@id="username"]')
# enter phone/email
username.send_keys("")

password = driver.find_element_by_xpath('//*[@id="password"]')
# enter password
password.send_keys("")

#waits for some time 
driver.implicitly_wait(30)

# sigin button click
sign_in = driver.find_element_by_xpath('//*[@id="app__container"]/main/div[2]/form/div[3]/button')
sign_in.click()

#waits for some time 
driver.implicitly_wait(30)


# to close default popup of message box
messagec = driver.find_element_by_class_name("msg-overlay-bubble-header")
messagec.click()

# go to mynetwork tab
driver.get("https://www.linkedin.com/mynetwork/")

# waits for some time
driver.implicitly_wait(30)

# scroll to mynetwork
driver.execute_script("window.scrollTo(0,500)")

# click on profile
connect = driver.find_element_by_class_name("discover-entity-type-card__info-container")
connect.click()

driver.implicitly_wait(10)

# click connect button after opening profile
connecthit = driver.find_element_by_xpath('/html/body/div[7]/div[3]/div/div/div/div/div[2]/main/div[1]/section/div[2]/div[1]/div[2]/div/div/span[1]/div/button')
connecthit.click()

# add note button click
addNote = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[1]')
addNote.click()

# adding a note
note = driver.find_element_by_name('message')
# write you custome message
note.send_keys("")

# hitting done button
done = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]')
done.click()

driver.implicitly_wait(20)
driver.quit()
