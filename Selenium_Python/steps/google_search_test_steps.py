from behave import given, when, then
from selenium.webdriver.common.by import By
from pages.google_search_page import GoogleSearchPage

@given('I am on the homepage')
def step_i_am_on_the_homepage(context):
    GoogleSearchPage.setup_the_page(context)

@when('I type "{query}" into the search field and search')
def step_i_type_into_the_search_field(context, query):
    context.google_search_page.search(query)

@then('I go to the search results page, and the first 3 results contain the word' "{expected_word}")
def step_i_go_to_the_search_results_page_and_first_3_results_contain_the_word(context, expected_word):
    # Get the texts of the first three search results.
    results = context.driver.find_elements(By.CSS_SELECTOR, GoogleSearchPage.SEARCH_RESULTS_SELECTOR)[:3]

    # Verify that each result contains the word "automation."
    for result in results:
        assert expected_word.lower() in result.text.lower(), f"Expected word '{expected_word}' not found in result: {result.text}"

@given('I Search by keyword' "{query}")
def step_i_search_by_keyword(context, query):
    GoogleSearchPage.setup_the_page(context)
    context.google_search_page.search(query)

@when('I click on the first result link')
def step_i_click_on_the_first_result_link(context):
    context.google_search_page.click_first_result()

@then('I go to the page, and the page title contains the word' "{expected_word}")
def step_i_go_to_the_page_and_check_title(context, expected_word):
    actual_title = context.driver.title
    assert expected_word.lower() in actual_title.lower()

@then(u'I should close the browser')
def step_then_close_browser(context):
    context.driver.quit()


