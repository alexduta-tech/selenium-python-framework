"""
Conftest file to define pytest fixtures for Selenium WebDriver tests.
Fixtures to run before and after each test, including, driver, logger, etc.
"""
import csv
import os
import platform
import uuid
import pytest
from monitoring import resource_monitor
from utils.browser import get_driver
from utils.config import DEFAULT_REPORT_DIR
from utils.docker import running_in_docker
from utils.logger import get_logger

# Ensure reports directory exists
os.makedirs(DEFAULT_REPORT_DIR, exist_ok=True)

@pytest.fixture
def logger(request):
    """
    Fixture to log the start and end of each test.
    """
    test_name = request.node.name
    logger = get_logger(test_name)
    logger.info(f"Start test: {test_name}")
    yield logger
    logger.info(f"Finish test: {test_name}")

@pytest.fixture
def driver(request, logger):
    """Provide a WebDriver instance and capture a screenshot at the end of the test.

    This fixture yields a live WebDriver and ensures cleanup.
    """
    logger.debug(f"Selenium test")
    logger.debug(f"Operating System: {platform.platform()}")
    running_in_docker(logger)

    driver = get_driver(logger)
    yield driver

    # Always attempt to save a screenshot at the end of the test
    try:
        screenshot_path = os.path.join(DEFAULT_REPORT_DIR, f"{request.node.name}.png")
        driver.save_screenshot(screenshot_path)
        logger.info(f"Screenshot saved at {screenshot_path}")
    except Exception:
        logger.exception("Failed to save screenshot")

    # Ensure driver quits 
    try:
        driver.quit()
    except Exception:
        logger.exception("Failed to quit WebDriver")

@pytest.hookimpl(tryfirst=True)
def pytest_sessionstart(session):
    session.resource_monitor = resource_monitor.ResourceMonitor(interval=0.1)
    session.resource_monitor.start()

@pytest.hookimpl(trylast=True)
def pytest_sessionfinish(session, exitstatus):
    session.resource_monitor.stop()
    results = session.resource_monitor.summary()

    run_id = str(uuid.uuid4())[:8]

    with open("reports/resource_summary.csv", "a", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "run_id",
                "framework",
                "os", 
                "browser", 
                "headles", 
                "process_name",  
                "cpu_avg", 
                "cpu_peak",
                "mem_avg_mb",
                "mem_peak_mb",
                ],
        )
        if f.tell() == 0:
            writer.writeheader()

        writer.writerow({"run_id": run_id, **results})
