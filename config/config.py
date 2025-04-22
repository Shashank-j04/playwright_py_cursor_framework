import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    # Base URL for the application
    BASE_URL = os.getenv("BASE_URL", "https://example.com")
    
    # API Configuration
    API_BASE_URL = os.getenv("API_BASE_URL", "https://api.example.com")
    API_KEY = os.getenv("API_KEY", "")
    
    # Browser Configuration
    BROWSER = os.getenv("BROWSER", "chromium")
    HEADLESS = os.getenv("HEADLESS", "True").lower() == "true"
    SLOW_MO = int(os.getenv("SLOW_MO", "0"))
    
    # Test Configuration
    TIMEOUT = int(os.getenv("TIMEOUT", "30000"))
    RETRY_COUNT = int(os.getenv("RETRY_COUNT", "2"))
    
    # Report Configuration
    REPORT_DIR = os.getenv("REPORT_DIR", "reports")
    SCREENSHOT_DIR = os.path.join(REPORT_DIR, "screenshots")
    
    @staticmethod
    def setup_directories():
        """Create necessary directories for reports and screenshots"""
        os.makedirs(Config.REPORT_DIR, exist_ok=True)
        os.makedirs(Config.SCREENSHOT_DIR, exist_ok=True) 