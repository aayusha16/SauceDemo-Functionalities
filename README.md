# SauceDemo Automation Framework

## Overview
This project is an automation testing framework for **SauceDemo** using **Playwright** and **Pytest**. It includes:

- Page Object Model (POM) structure  
- Login, Inventory, and Cart page tests  
- Logging and screenshot capture on failure  
- CSV-based test data for login  
- HTML reports generation  

---

## Project Structure
SauceDemo/
│
├── pages/ # Page object classes
│ ├── loginpage.py
│ ├── inventorypage.py
│ └── add_to_cartpage.py
│
├── tests/ # Pytest test cases
│ ├── test_login.py
│ ├── test_inventory.py
│ └── test_addcartpage.py
│
├── data/ # Test data (CSV files)
│ └── login_data.csv
│
├── utils/ # Utility scripts
│ └── data_reader.py
│
├── screenshots/ # Screenshots saved on test failure
│
├── conftest.py # Pytest fixtures and hooks
├── requirements.txt # Required Python packages
├── pytest_cache/ # Pytest cache
├── report.html # Test report (generated after running tests)
└── .github/workflows/ # GitHub Actions workflow for CI
└── playwright.yml
