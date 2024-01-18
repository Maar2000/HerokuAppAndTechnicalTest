from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.google_search_page import GoogleSearchPage

@given('I am on the homepage')
def step_i_am_on_the_homepage(context):
    setup_the_page(context)

@when('I type "{query}" into the search field and search')
def step_i_type_into_the_search_field(context, query):
    context.google_search_page.search(query)

@then('I go to the search results page, and the first 3 results contain the word' "{expected_word}")
def step_i_go_to_the_search_results_page_and_first_3_results_contain_the_word(context, expected_word):
    # Obtiene los textos de los tres primeros resultados de búsqueda
    results = context.driver.find_elements(By.CSS_SELECTOR, 'h3')[:3]

    # Verifica que cada resultado contenga la palabra "automation"
    for result in results:
        assert expected_word.lower() in result.text.lower()

@given('I Search by keyword' "{query}")
def step_i_search_by_keyword(context, query):
    setup_the_page(context)
    context.google_search_page.search(query)

@when('I click on the first result link')
def step_i_click_on_the_first_result_link(context):
    first_result = context.driver.find_element(By.CSS_SELECTOR, 'h3')
    first_result.click()

@then('I go to the page, and the page title contains the word' "{expected_word}")
def step_i_go_to_the_page_and_check_title(context, expected_word):
    # Obtén el título de la página
    actual_title = context.driver.title

    # Muestra el título en la consola
    print(f"El título de la página es: {actual_title} y el espero es {expected_word}")

    assert expected_word.lower() in actual_title.lower()


@then(u'I should close the browser')
def step_then_close_browser(context):
    context.driver.quit()

def setup_the_page(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("https://www.google.com")
    context.google_search_page = GoogleSearchPage(context.driver) 
