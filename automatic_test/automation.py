from selenium import webdriver

chrome_browser = webdriver.Chrome('./automatic_test/chromedriver')
# chrome_browser.maximize_window()
chrome_browser.get(
    'https://www.seleniumeasy.com/test/basic-first-form-demo.html')

assert 'Selenium Easy Demo' in chrome_browser.title
button = chrome_browser.find_element_by_class_name("btn-default")
input_user_message = chrome_browser.find_element_by_id("user-message")
output_message = chrome_browser.find_element_by_id("display")
print(button)
input_user_message.clear()
input_user_message.send_keys('1111')
button.click()
user_button2 = chrome_browser.find_element_by_css_selector('#get-input > .btn')
print('-------', user_button2)

assert '1111' in output_message.text
# assert 'Show Message' in chrome_browser.page_source

chrome_browser.quit()
