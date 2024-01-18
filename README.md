# Selenium + Python + Behave Project

This project uses Selenium with Python and Behave for behavior testing on a web application.

## Project Structure

project/
|-- driver/
| |-- chromedriver.exe
|-- features/
| |-- google_search.feature
|-- pages/
| |-- init.py
| |-- google_search_page.py
|-- steps/
| |-- init.py
| |-- google_search_test_steps.py
|-- tests/
| |-- init.py
| |-- test_google_search.py
|-- utilities/
| |-- init.py
|-- behave.ini
.gitignore
README.md
postmanCollections/
JmeterTests/
testingQuestions/


## Directory Descriptions

- **driver:** This directory contains the `chromedriver.exe` executable. The Chrome driver is necessary for Selenium to interact with the Chrome browser during tests.
- **features:** In this directory, you'll find `.feature` files, such as `google_search.feature`, that describe test scenarios using Behave's Gherkin format.
- **pages:** Here, classes representing web pages of the application are defined. `__init__.py` is an initialization file, and `google_search_page.py` might contain methods to interact with the Google search page.
- **steps:** It contains Python files with step definitions for test scenarios. `__init__.py` is an initialization file, and `google_search_test_steps.py` might contain the implementation of specific steps for the Google search test.
- **tests:** This directory could contain test files, such as `test_google_search.py`, where unit tests are written using a framework like `unittest` or `pytest`.
- **utilities:** Here, you might store utility files or reusable Python modules for common functions in your project.


## Scenarios with Selenium

### Scenario 1: User can search with Google Search
- **Description:** This scenario tests the search functionality on Google.
- **Steps:**
  - Given I’m on the homepage
  - When I type “test automation” into the search field And I click the Google Search button
  - Then I go to the search results page, and the first 3 results contain the word “automation”

### Scenario 2: User can go to the first search result
- **Description:** This scenario verifies that links in search results are valid.
- **Steps:**
  - Given I Search by keyword
  - When I click on the first result link
  - Then I go to the page, and the page title contains the word “automation”


## Scenarios with Postman and JMeter

### Scenario 3: User can login
  - Use the following link and build the corresponding requests to login https://the-internet.herokuapp.com/login

### Scenario 4: User can upload file 
  - Use the following link and uploads any file to the webapp https://the-internet.herokuapp.com/upload


## SQL Exercises

### 1. Explain the difference, in databases, between ‘Having’ and ‘where’ when it comes to a query. Develop one example for each one of this two cases and point out the difference.

### 2. Write a query to create a data table ‘Student’ with the following attributes in it: ‘Name', ‘Code', ‘Class’, ‘Age’, ‘Favorite Subject', ‘GPA’ (5.0 scale).

### 3. Insert at least 40 records in the last table with close to real data.

### 4. Write a query to get the average of the GPA from all the students whose name starts with ‘A’.

### 5. Write a query to get the list of students that are in the same class, have a GPA higher than 3.5/5.0 and order them by Age and Name.

### 6. Write a query to get the list of all the students with ‘Name', ‘Code', ‘Class’, ‘Age’, ‘Favorite Subject', ‘GPA’.

### 7. Take the following 25 question quiz about SQL, please include a screenshot about the results and time it took to take the test http://www.w3schools.com/quiztest/quiztest.asp?qtest=SQL


## Testing Questions

### 1. What is the difference between a unit test, an acceptance test, an integration test and an end-to-end test?

### 2. Could you explain Cohn's automation pyramid?

### 3. What is the difference between black box and white box testing?

### 4. What is the purpose of an exploratory test and when is it useful to run them?

### 5. Mention at least 5 test design techniques and explain them briefly

### 6. What is the purpose of the following types of tests?
  a. Functional test
  b. Performance test
  c. Security test
  d. Usability test
  e. API test
  f. Unit Test












