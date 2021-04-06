from selenium import webdriver

driver = webdriver.Chrome("C:/Users/vadim/Downloads/chromedriver")
driver.get("https://www.wikipedia.org")

search_field = driver.find_element_by_id("searchInput")
search_button = driver.find_element_by_xpath("//form[@id = 'search-form']/fieldset/button")

search_field.send_keys("Scorpions")
search_button.click()

assert "Scorpions" in driver.title
assert "Scorpions group" in driver.title

driver.quit()
