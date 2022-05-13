# from select import select
# import time

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import Select

# def test_selenium():
#     base_url = "http://127.0.0.1:8000/"

#     options = webdriver.ChromeOptions()
#     options.add_argument('--ignore-certificate-errors')
#     options.add_argument('--incognito')
#     options.add_argument('--headless')
#     driver = webdriver.Chrome("c:/chromedriver/chromedriver", chrome_options=options)

#     driver.get(base_url)
#     time.sleep(1)

#     input_element = driver.find_element(by=By.ID, value="form-input")
#     input_element.send_keys("Où est la tour eiffel ?")
    
#     form = driver.find_element(by=By.ID, value="search-form")
#     form.submit()

#     time.sleep(2)
#     answer_div = driver.find_element(by=By.ID, value="answer")
#     assert "La tour Eiffel" in answer_div.get_attribute('innerHTML')
