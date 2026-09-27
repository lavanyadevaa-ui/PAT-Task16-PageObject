from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PopulationPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.theworldcounts.com/challenges/planet-earth/state-of-the-planet/world-population-clock-live"
        self.population_xpath = "//div[@class='counter-ticker is-size-2-mobile']"

    def get_population(self):
        element = WebDriverWait(self.driver, 30).until(
        EC.visibility_of_element_located((By.XPATH, self.population_xpath))
        )
        return element.text

    def open(self):
        self.driver.get(self.url)

