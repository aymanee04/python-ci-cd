from selenium import webdriver
from selenium.webdriver.common.by import By


def test_home_page():
    driver = webdriver.Chrome()

    try:
        driver.get("http://localhost:5000")

        title = driver.find_element(By.ID, "title")

        assert title.text == "Python CI/CD Demo"

    finally:
        driver.quit()


def test_hello_button():
    driver = webdriver.Chrome()

    try:
        driver.get("http://localhost:5000")

        button = driver.find_element(By.ID, "hello-button")
        button.click()

        result = driver.find_element(By.ID, "result")

        assert result.text == "Hello from Selenium!"

    finally:
        driver.quit()