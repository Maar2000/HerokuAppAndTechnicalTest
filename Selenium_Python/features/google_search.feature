Feature: Search about automation in Google
    As a user
    I would like to go to the Google Search page
    To research information about automation

    Scenario: User can search with Google Search
        Given I am on the homepage
        When I type "test automation" into the search field and search
        Then I go to the search results page, and the first 3 results contain the word "automation"

    Scenario: User can go to the first search result
        Given I Search by keyword test automation
        When I click on the first result link
        Then I go to the page, and the page title contains the word automation 