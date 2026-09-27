import time
import pytest
from pages.population_page import PopulationPage

import pytest

@pytest.mark.parametrize("iterations", [5, 10, 20])
def test_population_live(setup, iterations):
    driver = setup
    page = PopulationPage(driver)
    page.open()

    for _ in range(iterations):
        population = page.get_population()
        print("Current Population:", population)
        time.sleep(2)

