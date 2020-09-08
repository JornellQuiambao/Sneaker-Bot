from config import keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from datetime import datetime, time

def getURL(model,size):

	url_base_size = 580
	base_size = 6.5
	url_size = (size - base_size) * 20 + url_base_size
	URL = 'https://www.adidas.com/us/' + str(model) + '.html?forceSelSize=' + str(model) + '_' + str(int(url_size))
	print(URL)
	return URL

def order(url,keys):

	driver = webdriver.Chrome('./chromedriver')

	# driver.get('https://www.adidas.com/us/account-login')
	# driver.find_element_by_xpath('//*[@id="login-email"]').send_keys(keys['email'])
	# driver.find_element_by_xpath('//*[@id="login-password"]').send_keys(keys['password'])
	# sleep(0.8)
	# driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div[3]/div[1]/form/div[6]/button').click()
	# while True:
	# 	if (driver.current_url == 'https://www.adidas.com/us/my-account'):
	# 		break
	
	driver.get(url)
	# driver.execute_script("window.scrollTo(0, document.body.scrollHeight)") 
	# sleep(0.2)
	element = WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div/div/div/div/div[3]/div[2]/div[2]/section/div[3]/button')))
	driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div[3]/div[2]/div[2]/section/div[3]/button').click()
	# sleep(3)
	element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME,"gl-modal__main-content")))
	driver.find_element_by_xpath('//*[@id="modal-root"]/div/div/div/div[2]/div/section/div[3]/a[2]/span').click()

	# sleep(3)
	element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME,"gl-input__field")))
	driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div[2]/div/main/form/div/div[1]/div/div[1]/div/div/div[1]/input').send_keys(keys['first name'])
	driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div[2]/div/main/form/div/div[1]/div/div[2]/div/div/div/input').send_keys(keys['last name'])
	driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div[2]/div/main/form/div/div[1]/div/div[3]/div/div/div[1]/input').send_keys(keys['street'])
	driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div[2]/div/main/form/div/div[1]/div/div[5]/div/div/div/input').send_keys(keys['city'])
	driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div[2]/div/main/form/div/div[1]/div/div[6]/span/div/div/select/option[9]').click()
	driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div[2]/div/main/form/div/div[1]/div/div[7]/div/div/div/input').send_keys(keys['zip'])
	driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div[2]/div/main/form/div/div[4]/div/div[1]/div/div/div[1]/input').send_keys(keys['phone'])
	driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div[2]/div/main/form/div/div[4]/div/div[2]/div/div/div[1]/input').send_keys(keys['email'])
	driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div[2]/div/main/div[7]/div/div/div/label/input').click()
	driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div[2]/div/main/div[9]/button').click()

	# sleep(30)
	element = WebDriverWait(driver, 40).until(EC.presence_of_element_located((By.CLASS_NAME,"payment-method-details___3YIQP")))
	sleep(3)
	# driver.find_element_by_xpath('//*[@id="card_281255480896"]/form/div[7]/div/button').click()
	driver.find_element_by_xpath('/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/main[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/div[2]/div[2]/iframe[1]').send_keys(keys['card number'])
	# driver.find_element_by_xpath('/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/main[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/div[5]/div[2]/input[1]').send_keys(keys['name'])
	driver.find_element_by_xpath('/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/main[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/div[4]/div[2]/input[1]').send_keys(keys['card date'])
	driver.find_element_by_xpath('/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/main[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/div[6]/div[2]/iframe[1]').send_keys(keys['card cvv'])

	# ~~~~~ Sumbit ~~~~~~
	# driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div[2]/div/main/button').click()
	while True:
		sleep(0.5)

def check_time(start_time):

	current_time = datetime.now().time()
	while(current_time < start_time):
		print(current_time)
		current_time = datetime.now().time()




if __name__ == '__main__':

	print(datetime.now().time())
	# check_time(time(7,0))
	order(getURL(keys['model'], keys['size']), keys)
	







# driver.find_element_by_xpath('').click()