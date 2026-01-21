# Python Selenium Framework for testing Web Applications in Docker

This project provides a Selenium WebDriver framework for testing web applications in Docker container using Python. It includes sample test cases and demonstrates the use of the Page Object Model (POM) design pattern.

## Tech stack

- **Python:** The core programming language for writing tests.
- **Selenium WebDriver:** A powerful tool for automating web browsers.
- **Docker:** Used to create a consistent and isolated environment for running tests.
- **Pytest:** A mature testing framework for Python.
- **Pytest-HTML:** A pytest plugin for generating HTML reports.

## Features

- **Programming language:** Python, chosen for readability and strong Selenium ecosystem
- **Web automation framework:** Selenium WebDriver
- **Cross-platform support:** Windows and Linux
- **Cross-browser testing:** Chrome, Firefox, and Edge
- **Dockerized Environment:** Tests can be run in Docker containers with all dependencies preinstalled, enabling consistent and OS-independent execution
- **Page Object Model:** Organizes page elements and interactions for better maintainability.
- **Pytest Framework:** Uses pytest for writing and running tests.
- **HTML Reports:** Generates HTML test reports using `pytest-html`.
- **Centralized Configuration:** Manages configuration through `utils/config.py`.
- **Virtual environment:** Uses Python `venv` for isolated dependency management based on `requirements.txt`.
- **Logging:**  Uses Python’s built-in `logging` module for configurable and structured test logs

## Prerequisites

- [Docker](https://www.docker.com/get-started)
- [Python](https://www.python.org/downloads/) (for local development)

## Getting Started

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/alexduta-tech/selenium-python-framework.git
    cd selenium-python-framework
    ```

2.  **Build and start the container:**
- Docker setup is automated using a batch script.
    1. Ensure Docker Desktop is installed and running
    2. Run the setup script:

        ```bash
        run_selenium_docker.bat
        ```

- This will build the Docker image and start the container in the background.
    
- Note: Initial Docker execution may take additional time to build the image and download dependencies. This is a one-time cost; later runs benefit from Docker’s caching mechanism.

## Running the Tests

### Prerequisites
Start Automation Playground application (locally or in Docker container) 
Please see the instructions here: https://github.com/alexduta-tech/automation-lab

### Docker execution
- You can run the tests by executing commands inside the running container.
- From selenium-python-framework folder execute the following commands:

-   **Run all tests:**
    ```bash
    docker compose exec selenium_tests pytest tests/
    ```

-   **Run specific tests using markers:**
    ```bash
    docker compose exec selenium_tests pytest -m smoke
    ```

-   **Run tests a given number of times (e.g. 2 times):**    
    ```bash
    docker compose exec selenium_tests pytest -m smoke --count=2
    ```    

Notes:
- In Docker the `headless` mode option is the strongly recommended to be used to run the automated tests (this is the default option set in the config file).

### Local execution
-   **Create virtual environment (if not already created):**
    ```bash
    python -m venv .venv
    ```
-   **Activate virtual environment (if not already activated):**
    ```bash
    .\.venv\Scripts\activate
    ```
-   **Select interpreter from Visual Studio Code (if not already selected):**
    Open the Command Palette (Ctrl+Shift+P), search for the Python: Select Interpreter command, and select it (e.g. .venv\Scripts\python.exe)
-   **Install dependencies (if not already installed):**
    ```bash
    pip install -r requirements.txt
    ```
-   **Run all tests:**
    ```bash
    pytest tests/
    ```
-   **Run specific tests using markers:**
    ```bash
    pytest -m smoke
    ```
-   **Run tests a given number of times (e.g. 2 times):**    
    ```bash
    pytest -m smoke --count=2
    ```

### Browser's
-   To run tests on different browsers, update \utils\config.py\ DEFAULT_BROWSER variable:
    ```bash
    DEFAULT_BROWSER = "chrome"
    DEFAULT_BROWSER = "firefox"
    DEFAULT_BROWSER = "edge"
    ```
-   To run tests in headed mode (only locall runs/not on Docker) please update to false the following variable:
    ```
    \utils\config.py\ DEFAULT_HEADLESS 
    ```

### Reports and logs
- The generated reports (html, screenshots) will be available in the `reports` directory on the execution machine.
- Also a `.json report file` will be generated in the `reports` directory, this file contains all the execution details like overall and individual test status, execution time etc.
- The generated logs will be available in the `logs` directory on the execution machine.

## Project Structure

```
.
├── conftest.py             # Pytest configuration
├── docker-compose.yml      # Docker Compose configuration
├── Dockerfile              # Dockerfile for the test environment
├── pages                   # Page Object Model classes
├── reports                 # Test reports
├── logs                    # Test logs
├── requirements.txt        # Python dependencies
├── pyproject.toml          # Python project metadata (define markers, html report generation etc.)
├── run_selenium_docker.bat # Batch script to build and run the container
├── data                    # Test data
├── tests                   # Test suites
└── utils                   # Utility modules
    ├── browser.py
    ├── config.py
    ├── constants.py
    ├── data_generator.py
    ├── docker.py
    ├── logger.py
    └── selenium_utils.py
```

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.