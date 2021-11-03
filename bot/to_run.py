from modules import *

url = "http://127.0.0.1:64379"
session_id = "9771c164cce1367d2af1df2f4bd800e4"

driver = webdriver.Remote(command_executor=url,desired_capabilities={})
driver.session_id = session_id

driver.get("https://opensea.io/")