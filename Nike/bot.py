from config import keys
from selenium import webdriver
import time

def order(k):

	driver = webdriver.Chrome('./chromedriver')

	driver.get(k['url'])

	# in stock
	driver.find_element_by_xpath('//*[@id="root"]/div/div/div[1]/div/div[3]/div[1]/header/div/div/div/div[1]/div[2]/div/nav/ul/li[2]/a/div').click()
	time.sleep(1.5)
	# find shoe
	driver.find_element_by_xpath('//*[@id="root"]/div/div/div[1]/div/div[3]/div[2]/div/section[1]/figure[1]/div/div/a').click()
	time.sleep(0.5)
	driver.execute_script("window.scrollTo(0, 1080)") 
	# find size
	driver.find_element_by_xpath('//*[@id="root"]/div/div/div[1]/div/div[3]/div[2]/div/section[1]/div[2]/aside/div/div[2]/div/div[2]/ul/li[7]').click()
	time.sleep(1)
	# add to cart
	driver.find_element_by_xpath('//*[@id="root"]/div/div/div[1]/div/div[3]/div[2]/div/section[1]/div[2]/aside/div/div[2]/div/div[2]/div/button').click()
	time.sleep(1)
	# goto cart
	driver.find_element_by_xpath('//*[@id="root"]/div/div/div[1]/div/header/div[1]/section/ul/li[3]/a').click()
	time.sleep(30)

if __name__ == '__main__':

	order(keys)