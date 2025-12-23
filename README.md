# Python Selenium Docker

This project provides a Selenium WebDriver framework for testing web applications in a Docker container using Python. It includes sample test cases and demonstrates the use of the Page Object Model (POM) design pattern.

## Tech stack

- **Python:** The core programming language for writing tests.
- **Selenium WebDriver:** A powerful tool for automating web browsers.
- **Docker:** Used to create a consistent and isolated environment for running tests.
- **Pytest:** A mature testing framework for Python.
- **Pytest-HTML:** A pytest plugin for generating HTML reports.

## Features

- **Programming language:** Python, chosen for readability and strong Selenium ecosystem
- **Web framework:** Selenium WebDriver
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
    git clone https://github.com/your-username/python-selenium-docker.git
    cd python-selenium-docker
    ```

2.  **Build and start the container:**
    ```bash
    run_selenium_docker.bat
    ```

    This will build the Docker image and start the container in the background.
    
    Note: Initial Docker execution may take additional time to build the image and download dependencies. This is a one-time cost; later runs benefit from Docker’s caching mechanism.

## Running the Tests

### Docker execution
You can run the tests by executing commands inside the running container.

-   **Run all tests:**
    ```bash
    docker compose exec selenium_tests pytest tests/
    ```

-   **Run specific tests using markers:**
    ```bash
    docker compose exec selenium_tests pytest -m smoke
    ```

-   **Generate an HTML report:**
    ```bash
    docker compose exec selenium_tests pytest --html=reports/report.html --self-contained-html
    ```

The generated report will be available in the `reports` directory on your local machine.
The generated logs will be available in the `logs` directory on your local machine.

### Local execution
-   **Create virtual environment:**
    ```bash
    python -m venv .venv
    ```
-   **Activate virtual environment:**
    ```bash
    .\.venv\Scripts\activate
    ```
-   **Select venv from Visual Studio Code:**
    Open the Command Palette (Ctrl+Shift+P), search for the Python: Select Interpreter command, and select it (e.g. .venv\Scripts\python.exe)
-   **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
-   **Run all tests:**
    ```bash
    pytest tests/
    ```
-   **Run specific tests using markers:**
    ```bash
    pytest -m smoke --html=reports/report.html --self-contained-html
    ```

## Project Structure

```
.
├── conftest.py             # Pytest configuration
├── docker-compose.yml      # Docker Compose configuration
├── Dockerfile              # Dockerfile for the test environment
├── pages                   # Page Object Model classes
├── reports                 # Test reports
├── requirements.txt        # Python dependencies
├── run_selenium_docker.bat # Batch script to build and run the container
├── tests                   # Test suites
└── utils                   # Utility modules
    ├── browser.py
    ├── config.py
    ├── docker.py
    ├── logger.py
    └── selenium_utils.py
```

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.