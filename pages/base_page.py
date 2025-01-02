from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains


class BasePage:
    # Locators
    SEARCH_INPUT = (By.NAME, 'q')
    BUTTON = (By.ID, 'submit-button')
    HEADER = (By.XPATH, "//h1[contains(text(),'Welcome')]")
    ITEM_LIST = (By.CSS_SELECTOR, '.item-list .item')

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10  # Default wait time

    # General methods

    def find_element(self, by_locator):
        """Find a single element by locator."""
        return WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(by_locator))

    def find_elements(self, by_locator):
        """Find multiple elements by locator."""
        return WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_all_elements_located(by_locator))

    def click(self, by_locator):
        """Click on an element."""
        WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(by_locator)).click()

    def enter_text(self, by_locator, text):
        """Enter text into an input field."""
        element = self.find_element(by_locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, by_locator):
        """Get text from an element."""
        return self.find_element(by_locator).text

    def is_visible(self, by_locator):
        """Check if an element is visible."""
        try:
            return bool(self.find_element(by_locator))
        except TimeoutException:
            return False

    def is_enabled(self, by_locator):
        """Check if an element is enabled."""
        return self.find_element(by_locator).is_enabled()

    def is_displayed(self, by_locator):
        """Check if an element is displayed."""
        return self.find_element(by_locator).is_displayed()

    def wait_for_element(self, by_locator, timeout=None):
        """Wait for an element to be present."""
        wait_time = timeout if timeout else self.timeout
        WebDriverWait(self.driver, wait_time).until(
            EC.presence_of_element_located(by_locator))

    def get_element_attribute(self, by_locator, attribute):
        """Get the attribute of an element."""
        return self.find_element(by_locator).get_attribute(attribute)

    # Additional common methods

    def scroll_to_element(self, by_locator):
        """Scroll to a specific element."""
        element = self.find_element(by_locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def select_dropdown_by_value(self, by_locator, value):
        """Select an option from a dropdown by value."""
        select = Select(self.find_element(by_locator))
        select.select_by_value(value)

    def select_dropdown_by_visible_text(self, by_locator, text):
        """Select an option from a dropdown by visible text."""
        select = Select(self.find_element(by_locator))
        select.select_by_visible_text(text)

    def select_dropdown_by_index(self, by_locator, index):
        """Select an option from a dropdown by index."""
        select = Select(self.find_element(by_locator))
        select.select_by_index(index)

    def switch_to_iframe(self, by_locator):
        """Switch to an iframe."""
        iframe = self.find_element(by_locator)
        self.driver.switch_to.frame(iframe)

    def switch_to_default_content(self):
        """Switch back to the default content."""
        self.driver.switch_to.default_content()

    def switch_to_window(self, window_index):
        """Switch to a specific window or tab by index."""
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[window_index])

    def javascript_click(self, by_locator):
        """Click an element using JavaScript."""
        element = self.find_element(by_locator)
        self.driver.execute_script("arguments[0].click();", element)

    def reload_page(self):
        """Reload the current page."""
        self.driver.refresh()

    def accept_alert(self):
        """Accept an alert dialog."""
        WebDriverWait(self.driver, self.timeout).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        alert.accept()

    def dismiss_alert(self):
        """Dismiss an alert dialog."""
        WebDriverWait(self.driver, self.timeout).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        alert.dismiss()

    def get_page_title(self):
        """Get the page title."""
        return self.driver.title

    def get_current_url(self):
        """Get the current URL."""
        return self.driver.current_url

    def wait_for_element_invisibility(self, by_locator, timeout=None):
        """Wait for an element to become invisible."""
        wait_time = timeout if timeout else self.timeout
        WebDriverWait(self.driver, wait_time).until(
            EC.invisibility_of_element_located(by_locator))

    def get_cookie(self, cookie_name):
        """Get a specific cookie by name."""
        return self.driver.get_cookie(cookie_name)

    def add_cookie(self, cookie):
        """Add a cookie."""
        self.driver.add_cookie(cookie)

    def select_radio_button(self, by_locator):
        """Select a radio button if not already selected."""
        element = self.find_element(by_locator)
        if not element.is_selected():
            element.click()

    def select_checkbox(self, by_locator):
        """Select a checkbox if not already selected."""
        element = self.find_element(by_locator)
        if not element.is_selected():
            element.click()

    def deselect_checkbox(self, by_locator):
        """Deselect a checkbox if selected."""
        element = self.find_element(by_locator)
        if element.is_selected():
            element.click()

    def drag_and_drop(self, source_locator, target_locator):
        """Perform drag and drop from source to target element."""
        source_element = self.find_element(source_locator)
        target_element = self.find_element(target_locator)
        action_chains = ActionChains(self.driver)
        action_chains.drag_and_drop(source_element, target_element).perform()

    def close_modal(self, by_locator):
        """Close a modal dialog by clicking the close button."""
        element = self.find_element(by_locator)
        element.click()

    # Example methods using the locators

    def search_for(self, text):
        """Enter search text and submit."""
        self.enter_text(self.SEARCH_INPUT, text)
        self.driver.find_element(*self.SEARCH_INPUT).submit()

    def click_submit_button(self):
        """Click the 'Submit' button."""
        self.click(self.BUTTON)

    def is_header_visible(self):
        """Check if the header is visible."""
        return self.is_visible(self.HEADER)

    def get_all_items(self):
        """Get all items in a list."""
        return self.find_elements(self.ITEM_LIST)
