from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def create_driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")

    return webdriver.Chrome(options=options)


def test_home_page():
    driver = create_driver()

    try:
        driver.get("http://localhost:5000")

        title = driver.find_element(By.ID, "title")

        assert title.text == "Python CI/CD Demo"

    finally:
        driver.quit()


def test_hello_button():
    driver = create_driver()

    try:
        driver.get("http://localhost:5000")

        button = driver.find_element(By.ID, "hello-button")
        button.click()

        result = driver.find_element(By.ID, "result")

        assert result.text == "Hello from Selenium!"

    finally:
        driver.quit()