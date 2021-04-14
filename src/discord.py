from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
options = Options()
options.add_argument("--log-level=3")
options.add_argument(
    r"user-data-dir=C:\Users\owenw\AppData\Local\Google\Chrome\User Data\Profile 1"
)
options.add_argument("start-maximized")
driver = webdriver.Chrome(
    executable_path=r"C:\Users\owenw\vscode\chromedriver.exe", options=options)
driver.get("https://discord.com/app")
driver.maximize_window()