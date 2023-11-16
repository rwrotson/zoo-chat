import re
from typing import List, Dict, Tuple
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from parser.consts import PAGE_URL, INPUTS_XPATHS, SUBMIT_BUTTON_XPATH, TOTEM_BUTTON_XPATH

class Parser:
    __instance = None
    
    def __new__(cls, *args, **kwargs): # Singleton pattern
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, inputs_data: Tuple[Dict]) -> None:
        self._driver = self.initialize_driver()
        self.load_start_page()
        self._inputs_elements = self.get_inputs_elements()
        self._inputs_data = inputs_data
        
        self._score = {}
        self._totem_animals = []

    def parse_data(self):
        self.fill_inputs_elements()
        self.submit_input_data()
        sleep(20) # wait on page for the results
        self.parse_output_for_score()
        self.parse_output_for_totem_animals()
        self.quit_driver()

    @property
    def score(self):
        return self._score

    @property
    def totem_animals(self):
        return self._totem_animals

    @staticmethod
    def initialize_driver() -> WebDriver:
        exec_path = ChromeDriverManager().install()
        service = ChromeService(executable_path=exec_path)
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome(service=service, options=options)
        return driver

    def wait_until_locator_is_visible(self, locator: Tuple[str]) -> None:
        wait = WebDriverWait(self._driver, 10)
        wait.until(EC.visibility_of_element_located(locator))

    def wait_until_locator_is_clickable(self, locator: Tuple[str]) -> None:
        wait = WebDriverWait(self._driver, 10)
        wait.until(EC.element_to_be_clickable(locator))

    def load_start_page(self) -> None:
        self._driver.get(PAGE_URL)
        self.wait_until_start_page_is_loaded()

    def wait_until_start_page_is_loaded(self):
        self.wait_until_locator_is_visible((By.ID, 'kuta_data'))

    def get_inputs_elements(self) -> List[Dict]:
        inputs_elements = []
        for count, group in enumerate(INPUTS_XPATHS):
            inputs_elements.append(dict())
            for key, value in group.items():
                element = self._driver.find_element(By.XPATH, value)
                inputs_elements[count][key] = element
        return inputs_elements

    def fill_inputs_elements(self) -> None:
        for i in range(2):
            self.fill_date_input(self._inputs_data[i]['date'], self._inputs_elements[i]['date'])
            self.fill_time_input(self._inputs_data[i]['time'], self._inputs_elements[i]['time'])
            self.fill_coord(self._inputs_data[i]['latitude'], self._inputs_elements[i]['latitude'])
            self.fill_coord(self._inputs_data[i]['longitude'], self._inputs_elements[i]['longitude'])

    def fill_date_input(self, date: str, date_input: WebElement) -> None:
        day, month, year = date.split('.')
        self.wait_until_start_page_is_loaded()
        date_input.click()
        self.select_year(year)
        self.select_month(month)
        self.select_day(day)
        self.apply_date()

    def select_year(self, year: str) -> None:    
        while True: # select and click on the right year on page
            years_elements_on_page = self._driver.find_elements(By.CLASS_NAME, 'year')
            for year_element in years_elements_on_page:
                if year_element.text.strip() == year:
                    year_element.click()
                    break
            else: # only execute when it's no break in the inner loop
                datepicker_years_div = self._driver.find_element(By.CLASS_NAME, 'datepicker-years')
                previous_years_button = datepicker_years_div.find_element(By.CLASS_NAME, 'prev')
                previous_years_button.click()
                sleep(0.5) # for safety
                continue
            break

    def select_month(self, month: str):
        self.wait_until_locator_is_clickable((By.CLASS_NAME, 'month'))
        datepicker_div = self._driver.find_element(By.CLASS_NAME, 'datepicker-months')
        month_buttons = datepicker_div.find_elements(By.CLASS_NAME, 'month')
        month_button = month_buttons[int(month) - 1]
        month_button.click()

    def select_day(self, day: str):
        self.wait_until_locator_is_clickable((By.CLASS_NAME, 'day'))
        datepicker_div = self._driver.find_element(By.CLASS_NAME, 'datepicker-days')
        day_buttons = datepicker_div.find_elements(By.CSS_SELECTOR, 'td.day:not(.old):not(.new)')
        day_button = day_buttons[int(day) - 1]
        day_button.click()

    def apply_date(self):
        self.wait_until_locator_is_clickable((By.CLASS_NAME, 'apply'))
        action_bar_section = self._driver.find_element(By.CLASS_NAME, 'action-bar')
        apply_button = action_bar_section.find_element(By.CLASS_NAME, 'apply')
        apply_button.click()

    def fill_time_input(self, time: str, time_input: WebElement) -> None:
        hour, minute, second = *map(int, time.split(':')), 0
        am = True if 0 <= hour <= 11 else False # 12am -- 00:00; 12pm -- 12:00
        if am is False: hour = hour - 12
        am_pm = 0 if am else 1
        self.wait_until_start_page_is_loaded()
        time_input.click()

        # set time
        time_class_names = ((hour, 'dwwl0'), (minute, 'dwwl1'), (second, 'dwwl2'), (am_pm, 'dwwl3'))
        for item in time_class_names:
            section = self._driver.find_element(By.CLASS_NAME, item[1])
            css_selector = f'div[data-val="{item[0]}"]'
            option = section.find_element(By.CSS_SELECTOR, css_selector)
            arrow_down = section.find_element(By.CLASS_NAME, 'mbsc-ic-arrow-down5')
            while option.get_attribute('aria-selected') != 'true':
                arrow_down.click()
                sleep(0.02)
        
        # apply
        action_bar_section = self._driver.find_element(By.CLASS_NAME, 'action-bar')
        apply_button = action_bar_section.find_elements(By.CLASS_NAME, 'span')[1]
        apply_button.click()

    def fill_coord(self, coord: str, coord_input: WebElement) -> None:
        self.wait_until_start_page_is_loaded()
        coord_input.clear()
        coord_input.send_keys(coord)

    def submit_input_data(self) -> None:
        self.wait_until_locator_is_clickable((By.XPATH, SUBMIT_BUTTON_XPATH))
        submit_button = self._driver.find_element(By.XPATH, SUBMIT_BUTTON_XPATH)
        submit_button.click()

    def parse_output_for_score(self) -> None:
        self.wait_until_locator_is_visible((By.CLASS_NAME, 'result-header'))
        kutas = (
            'varna', 'vashya', 'dina', 'yoni',
            'grahamaitri', 'gana', 'rasi', 'nadi'
        )
        results = {'sum': 0}
        for kuta in kutas:
            css_selector = f'a[href*="#{kuta}"]'
            kuta_a = self._driver.find_element(By.CSS_SELECTOR, css_selector)
            kuta_span = kuta_a.find_element(By.CLASS_NAME, 'label')
            kuta_value = float(kuta_span.text.strip().split('/')[0].strip())
            results[kuta] = kuta_value
            results['sum'] += kuta_value
        self._score = results

    def parse_output_for_totem_animals(self) -> str:
        # get text about totem animals
        self.wait_until_locator_is_clickable((By.XPATH, TOTEM_BUTTON_XPATH))
        details_button = self._driver.find_element(By.XPATH, TOTEM_BUTTON_XPATH)
        details_button.click()
        self.wait_until_locator_is_visible((By.ID, 'yoni'))
        yoni_element = self._driver.find_element(By.ID, 'yoni')
        yoni_text = yoni_element.find_element(By.TAG_NAME, 'blockquote').text

        # parse text to extract totem animals
        indices_of_start = [m.start() for m in re.finditer('animal', yoni_text)]
        indices_of_end = [yoni_text.find(' and '), yoni_text.find(' get ')]
        self._totem_animals = [yoni_text[indices_of_start[i] + 9:indices_of_end[i]] for i in range(2)]

    def quit_driver(self) -> None:
        self._driver.quit()


# context manager ?
# constants in self ?