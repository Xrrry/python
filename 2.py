import re
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By #按照什么方式查找，By.ID,By.CSS_SELECTOR
from selenium.webdriver.common.keys import Keys #键盘按键操作
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait #等待页面加载某些元素
driver=webdriver.Chrome()
try:
    driver.get('https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/first0')
    input_tag = driver.find_element_by_xpath('//*[@id="mt_5"]/div[1]/div[3]/input')
    input_tag2 = driver.find_element_by_xpath('//*[@id="mt_5"]/div[2]/div[3]/input')
    input_tag.send_keys('20172430526') #python2中输入中文错误，字符串前加个u
    input_tag2.send_keys('02213577')
    input_tag.send_keys(Keys.ENTER) #输入回车
    wait = WebDriverWait(driver, 5)
    wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[3]/div[2]')))

    page = driver.page_source
    url = re.findall('<iframe name="zzj_top_6s" id="zzj_top_6s" src="([\s\S]*?)" marginwidth="0" marginheight="0"', page)[0]
    print(url)
    driver.get(url)
    click_tag = driver.find_element_by_xpath('//*[@id="bak_0"]/div[13]/div[3]/div[4]')
    click_tag.click()
    wait2 = WebDriverWait(driver, 5)
    wait2.until(EC.presence_of_element_located((By.XPATH, '//*[@id="bak_0"]')))
    select = Select(driver.find_element_by_xpath('//*[@id="bak_0"]/div[8]/select'))
    submit = driver.find_element_by_xpath('//*[@id="bak_0"]/div[13]/div[4]')
    select.select_by_index(0)
    submit.click()
    wait3 = WebDriverWait(driver, 5)
    wait3.until(EC.presence_of_element_located((By.XPATH, '//*[@id="bak_0"]/div[2]/div[2]/div[2]/div[2]')))
    page1 = driver.page_source
    message = re.findall('<img src="/images/bs_02.png" style="width:25px;height:7px;border:0px">([\s\S]*?)</div><div style="width:10px;height:100%;float:right;"></div></div>', page1)[0]
    print(driver.page_source)  # 打印出页面源代码
    print(driver.current_url)  # 获取打开网址的url
    print(driver.get_cookies())   #cookies
    print(message)
finally:
    pass