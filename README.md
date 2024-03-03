ProjectName - Automated Testing of an E-commerce Platform
ProjectName is a Python project designed for automated testing of an e-commerce platform using Selenium WebDriver. The target website for testing is hosted at https://tutorialsninja.com/demo/.

Table of Contents
Introduction
Features
Prerequisites
Installation
Usage
Project Structure
Testing Scenarios
Reports
Contributing
Introduction
The goal of ProjectName is to automate the testing process of an e-commerce platform to ensure its reliability and functionality across various scenarios. It utilizes Selenium WebDriver for interacting with web elements programmatically.

Features
Modular Project Structure: Organized into separate directories for easy maintenance and scalability.
Comprehensive Testing Scenarios: Covers functional and edge cases such as logging in, registering, and searching for products.
Integration with pytest HTML Report: Provides detailed test reporting and debugging capabilities.
Dynamic Data Generation: Generates dynamic data for testing scenarios, enhancing test coverage.
Best Practices in Automated Testing: Implements error handling and explicit waits for robust testing.
Prerequisites
Before running this project, ensure you have the following installed:

Chrome Browser: Required for Selenium WebDriver.
Python 3.11: Install the latest Python version.
Dependencies: Install the following third-party modules:

pip install selenium
pip install webdriver-manager

Usage
To run the tests, execute the following command:

pytest --html=report.html
This command will run all the test cases and generate an HTML report named report.html.

Project Structure
The project is organized as follows:

Pages: Contains classes representing different pages of the website.
Utilities: Contains utility functions for reading configurations.
Tests: Contains test classes for different functionalities.
Testing Scenarios
The testing scenarios include:

Logging in with valid and invalid credentials.
Registering with valid and invalid inputs.
Searching for products with valid and invalid queries.
Reports
The pytest HTML report provides detailed information about test outcomes, including any failures or errors encountered during testing. It facilitates debugging and helps in identifying issues quickly.

Contributing
Contributions are welcome! If you'd like to contribute to this project, please fork the repository and create a pull request with your changes.
