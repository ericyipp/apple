from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.apple.com/shop/product/MWP22AM/A/airpods-pro')

import time
time.sleep(2)

atcButton = driver.find_element_by_xpath('//*[@id="add-to-cart"]')
atcButton.click()

checkoutButton = driver.find_element_by_xpath('//*[@id="shoppingCart.actions.checkout"]')
checkoutButton.click()

time.sleep(0.5)

guestCheckout = driver.find_element_by_xpath('//*[@id="signIn.guestLogin.guestLogin"]')
guestCheckout.click()

time.sleep(0.5)

shipping = driver.find_element_by_xpath('//*[@id="rs-checkout-continue-button-bottom"]')
shipping.click()

time.sleep(1)

firstname = driver.find_element_by_xpath('//*[@id="recon-0-97"]')
firstname.send_keys('John')

lastname = driver.find_element_by_xpath('//*[@id="recon-0-96"]')
lastname.send_keys('Smith')

streetadress = driver.find_element_by_xpath('//*[@id="recon-0-100"]')
streetadress.send_keys('12345 Street')

zipcodeclear = driver.find_element_by_xpath('//*[@id="recon-0-109"]').clear()

zipcode = driver.find_element_by_xpath('//*[@id="recon-0-109"]')
zipcode.send_keys('12345')


email = driver.find_element_by_xpath('//*[@id="recon-0-84"]')
email.send_keys('hi@email.com')

phonenumber = driver.find_element_by_xpath('//*[@id="recon-0-85"]')
phonenumber.send_keys('1234567890)

time.sleep(1)

payment = driver.find_element_by_xpath('//*[@id="addressVerification"]')
payment.click()

time.sleep(1.5)

ccinfo = driver.find_element_by_xpath('//*[@id="checkout.billing.billingOptions.options.0-selector"]/label')
ccinfo.click()

time.sleep(1)

ccnumber = driver.find_element_by_xpath('//*[@id="recon-0-182"]')
ccnumber.send_keys('4111111111111111')

ccEXP = driver.find_element_by_xpath('//*[@id="recon-0-181"]')
ccEXP.send_keys('1223')

CVV = driver.find_element_by_xpath('//*[@id="recon-0-179"]')
CVV.send_keys('123')

review = driver.find_element_by_xpath('//*[@id="rs-checkout-continue-button-bottom"]')
review.click()

time.sleep(1.5)

placeorder = driver.find_element_by_xpath('/html/body/div[2]/div[4]/div/div[5]/div[1]/div[1]/div/div/div[2]/div[5]/div/div/div/div[1]/button')
placeorder.click()