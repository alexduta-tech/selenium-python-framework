from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from utils.config import IMPLICIT_WAIT, DEFAULT_BROWSER, DEFAULT_HEADLESS
from utils.docker import running_in_docker

def get_driver(logger):
    browser_name = DEFAULT_BROWSER
    headless = DEFAULT_HEADLESS
    driver = None

    try:
        if browser_name == "chrome":
            driver = start_chrome_driver(headless)

        elif browser_name == "firefox":
            driver = start_firefox_driver(headless)

        elif browser_name == "edge":
            # Docker: Edge isn't in starndard Debian repos by default, using Chromium-based Edge
            if running_in_docker(logger):
                logger.info("Running in Docker: using Chromium-based Edge")
                driver = start_chrome_driver(headless)
            else:
                logger.info("Not running in Docker: using Microsoft Edge")
                driver = start_edge_driver(headless)

        else:
            logger.warning(f"Browser '{browser_name}' not supported, defaulting to Chrome.")
            driver = start_chrome_driver(headless)

    except Exception:
        logger.exception(
            "Failed to start WebDriver. WebDriverManager may have failed to download the driver."
        )
        raise

    # Only maximize when not running headless; headless uses explicit window-size above
    try:
        if not headless:
            driver.maximize_window()
    except Exception:
        # Some remote/unsupported drivers may not implement maximize; ignore but log
        logger.debug("maximize_window() failed or is not supported by the driver")

    driver.implicitly_wait(IMPLICIT_WAIT)
    logger.info(f"{browser_name.capitalize()} driver started. Headless={headless}")
    return driver

def start_chrome_driver(headless: bool):
    """Start a Chrome WebDriver instance."""
    options = ChromeOptions()
    if headless:
        options.add_argument("--headless=new")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=options)
        
    return driver
    
def start_firefox_driver(headless: bool):
    """Start a Firefox WebDriver instance."""
    options = FirefoxOptions()
    if headless:
        options.add_argument("--headless")
        options.add_argument("--width=1920")
        options.add_argument("--height=1080")
    driver = webdriver.Firefox(options=options)
        
    return driver

def start_edge_driver(headless: bool):
    """Start an Edge WebDriver instance."""
    options = EdgeOptions()
    if headless:
        options.add_argument("--headless")
        options.add_argument("--window-size=1920,1080")
    driver = webdriver.Edge(options=options)
        
    return driver