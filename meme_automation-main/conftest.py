import pytest
from pages import Pages
from settings import *
from appium import webdriver
from selenium.webdriver import Chrome, Firefox, Edge, Safari
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="class")
def phone_driver():
    capabilities = {
        "platformName": (CONFIG[platform]["platformName"]),
        "platformVersion": (CONFIG[platform]["platformVersion"]),
        "deviceName": (CONFIG[platform]["deviceName"]),
        "automationName": (CONFIG[platform]["automationName"]),
        "appPackage": (CONFIG[platform]["appPackage"]),
        "app": (CONFIG[platform]["app"]),
        "noReset": (CONFIG[platform]["noReset"]),
        "fullReset": (CONFIG[platform]["fullReset"]),
    }
    url = "http://127.0.0.1:4723/wd/hub"
    driver = webdriver.Remote(url, capabilities)
    yield driver
    driver.quit()


@pytest.fixture(scope="class")
def chrome_driver():
    s = Service(executable_path=f"/opt/homebrew/bin/chromedriver")
    options = Options()
    options.add_argument("--window-size=1920x1080")
    options.add_argument("--verbose")
    driver = Chrome(service=s, options=options)
    yield driver
    driver.quit()


@pytest.fixture(scope="class")
def safari_driver():
    s = Service(executable_path=f"/opt/homebrew/bin/safaridriver")
    options = Options()
    options.add_argument("--window-size=1920x1080")
    options.add_argument("--verbose")
    driver = Safari(service=s, options=options)
    yield driver
    driver.quit()


@pytest.fixture(scope="class")
def chrome_driver():
    s = Service(executable_path=f"/opt/homebrew/bin/chromedriver")
    options = Options()
    options.add_argument("--window-size=1920x1080")
    options.add_argument("--verbose")
    driver = Chrome(service=s, options=options)
    yield driver
    driver.quit()


@pytest.fixture(scope="class")
def edge_driver():
    s = Service(executable_path=f"/opt/homebrew/bin/chromedriver")
    options = Options()
    options.add_argument("--window-size=1920x1080")
    options.add_argument("--verbose")
    driver = Edge(service=s, options=options)
    yield driver
    driver.quit()


@pytest.fixture(scope="class")
def firefox_driver():
    s = Service(executable_path=f"/opt/homebrew/bin/firefoxdriver")
    options = Options()
    options.add_argument("--window-size=1920x1080")
    options.add_argument("--verbose")
    driver = Firefox(service=s, options=options)
    driver.get("https://www.stakeland.com/")
    yield driver
    driver.quit()


@pytest.fixture(scope="class", autouse=True)
def pages(phone_driver, firefox_driver, safari_driver, chrome_driver):
    def read_yaml_file(filepath):
        with open(filepath, "r") as file:
            return yaml.safe_load(file)

    config = read_yaml_file("config.yaml")
    platform_value = config["platform"]
    if platform_value in ["android", "ios"]:
        driver = phone_driver
    elif platform_value == "safari":
        driver = safari_driver
    elif platform_value == "firefox":
        driver = firefox_driver
    elif platform_value == "edge":
        driver = edge_driver
    elif platform_value == "chrome":
        driver = chrome_driver
    pages = Pages(driver)
    return pages
