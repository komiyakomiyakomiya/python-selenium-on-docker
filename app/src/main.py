import os
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from utils.driver_option import setting


options = setting()
driver = webdriver.Remote(
    command_executor=os.environ["CHROME_CONTAINER_URL"],
    options=options,
)

driver.get("https://www.time-j.net/worldtime/country/jp")
driver.implicitly_wait(5)

print(driver.find_element_by_xpath("/html/body/div/div[6]/div[1]/div/p[5]").text)
driver.quit()
