import os

# Logging and reporting configuration 
ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
DEFAULT_LOG_DIR = os.path.join(ROOT_DIR, "logs")
DEFAULT_LOG_LEVEL = "DEBUG"  # DEBUG|INFO|WARNING|ERROR|CRITICAL
DEFAULT_REPORT_DIR = os.path.join(ROOT_DIR, "reports")

# Application settings(can be overridden by the environment variables stored in the existing docker-compose.yml)
BASE_URL = os.getenv("BASE_URL", "http://localhost:3000/")
IMPLICIT_WAIT = 10

# Browser configuration defaults (can be overridden by the environment variables stored in the existing docker-compose.yml)
DEFAULT_BROWSER = "chrome"  # Options: "chrome", "firefox", "edge"
DEFAULT_HEADLESS = os.getenv("HEADLESS", "true").lower() in ("1", "true", "yes", "y", "on")
