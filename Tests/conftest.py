from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest


@pytest.fixture()
def init_driver(request):
    web_driver = webdriver.Chrome(ChromeDriverManager().install())
    request.cls.driver = web_driver
    web_driver.get("http://localhost:8000/")
    web_driver.maximize_window()

    yield
    web_driver.quit()
