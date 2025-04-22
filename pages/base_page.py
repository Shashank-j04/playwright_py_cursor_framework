from playwright.sync_api import Page
from config.config import Config

class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.config = Config()
    
    def navigate(self, url: str = ""):
        """Navigate to a specific URL or the base URL"""
        full_url = f"{self.config.BASE_URL}{url}"
        self.page.goto(full_url)
    
    def wait_for_selector(self, selector: str, timeout: int = None):
        """Wait for an element to be visible"""
        timeout = timeout or self.config.TIMEOUT
        return self.page.wait_for_selector(selector, timeout=timeout)
    
    def click(self, selector: str):
        """Click on an element"""
        self.wait_for_selector(selector).click()
    
    def fill(self, selector: str, value: str):
        """Fill an input field"""
        self.wait_for_selector(selector).fill(value)
    
    def get_text(self, selector: str) -> str:
        """Get text content of an element"""
        return self.wait_for_selector(selector).text_content()
    
    def take_screenshot(self, name: str):
        """Take a screenshot and save it to the reports directory"""
        screenshot_path = f"{self.config.SCREENSHOT_DIR}/{name}.png"
        self.page.screenshot(path=screenshot_path)
        return screenshot_path 