from modules import *

options = Options()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(executable_path=r'C:\chromedriver.exe', options=options)

driver.get("https:\\www.google.com")

url = driver.command_executor._url        #"http://127.0.0.1:60622/hub"
session_id = driver.session_id            #'4e167f26-dc1d-4f51-a207-f761eaf73c31'

print(url)
print(session_id)