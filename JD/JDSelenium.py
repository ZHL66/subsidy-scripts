from anyio import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

options = Options()
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
# options.add_argument("--headless")  # 无头模式可选

# Windows 默认在: C:/Users/你的用户名/AppData/Local/Google/Chrome/User Data
options.add_argument(r'--user-data-dir=C://Users//lenovo//AppData//Local//Google//Chrome//User Data')

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://item.jd.com")
print(driver.title)                   # 获取页面标题
print(driver.current_url)             # 获取当前 URL
input("按回车键后关闭浏览器...")  # 等你手动按回车才退出
driver.quit()


