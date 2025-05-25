import sys
from gc import freeze
from time import sleep
import pytest
# import uc
from pyexpat.errors import messages
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
from selenium.webdriver.support.select import Select


@pytest.fixture
def driver():
    # Setup undetected Chrome driver
    options = uc.ChromeOptions()
    options.add_argument('--start-maximized')
    driver = uc.Chrome(options=options)
    driver.maximize_window()
    driver.get('https://www.skyscanner.co.il/')
    yield driver
    driver.quit()

## Hotel Search with valid details
def test_1(driver):
    sleep(15)
    Hotel_tab= driver.find_element(By.XPATH,"//span[text()='Hotels']")
    Hotel_tab.click()
    # sleep(30)
    destination = driver.find_element(By.ID,'destination-autosuggest')
    destination.send_keys('Paris')
    sleep(3)
    Check_in = driver.find_element(By.XPATH, "//input[@id='checkin']")
    Check_in.click()
    sleep(3)
    checkin = driver.find_element(By.XPATH, "//span[text() = '20']")
    checkin.click()
    sleep(3)
    Check_out= driver.find_element(By.XPATH, "//input[@id ='checkout']")
    Check_out.click()
    sleep(3)
    checkout= driver.find_element(By.XPATH,"//span[text() = '26']")
    checkout.click()
    sleep(3)
    Room_Adult= driver.find_element(By.XPATH,"//input[@id='guests-rooms']")
    Room_Adult.click()
    sleep(3)
    Adults = driver.find_element(By.XPATH,"//input[@id='adults']")
    Adults.clear()
    Adults.send_keys('4')
    sleep(3)
    Rooms= driver.find_element(By.XPATH,"//input[@id='rooms']")
    Rooms.clear()
    Rooms.send_keys('2')
    sleep(3)
    BTN_Done = driver.find_element(By.XPATH,"//span[text()='Done']")
    BTN_Done.click()
    sleep(2)
    btn_search= driver.find_element(By.CLASS_NAME,'BpkButton_bpk-button__ZGRmN.BpkButton_bpk-button--large__ZmE2M.bpk-button--submit.ExpandableLayout_ExpandableLayout__cta__OWY1Z')
    btn_search.click()
    sleep(10)
    results = driver.find_elements(By.XPATH,"//div[@class='HotelCardsListChunk_HotelCardsListChunk__card__O2gi3 HotelCardsListChunk_HotelCardsListChunk__card--newLayout__DTkR9 HotelCardsListChunk_Animation__zkf0j']")
    assert len(results) > 0, "No hotel results were found."