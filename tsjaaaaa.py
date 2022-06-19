from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

PATH = ("/Users/alvin/Desktop/chromedriver101")
driver = webdriver.Chrome(PATH)
driver.get("https://tsj.tw/")

blow = driver.find_element_by_id("click")
blow_c = driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[4]/div[2]/h4[1]')
p_c = driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[4]/div[2]/h4[2]')
www = driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[4]/div[1]/button[3]')

items = []
items.append(driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[4]/td[5]/button[1]/i'))
items.append(driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[3]/td[5]/button[1]/i'))
items.append(driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[2]/td[5]/button[1]'))

prices = []
prices.append(driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[4]/td[4]'))
prices.append(driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[3]/td[4]'))
prices.append(driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[2]/td[4]'))


for i in range (10000):
    actions = ActionChains(driver)
    actions.click(blow)
    actions.perform()
    c = int(p_c.text.replace('您目前擁有','').replace('技術點', ''))
    for j in range(3):
        price = int(prices[j].text.replace('技術點', ''))
        if c >= price:
            buy_actions = ActionChains(driver)
            buy_actions.move_to_element(items[j])
            buy_actions.click()
            buy_actions.perform()
            break