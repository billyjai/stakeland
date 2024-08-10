from pages.stakeland_home_page import StakeLandHomePage


class Pages:
    def __init__(self, driver):
        self._driver = driver
        self.stakeland_home_page = StakeLandHomePage
