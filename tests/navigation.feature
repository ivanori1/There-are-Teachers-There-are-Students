Feature: Test Navigation Between Pages

  This is just simple test case to navigate all pages in our app

  Scenario: Homepage can go to Teacher page
    Given I am on the homepage
    When I click on the link with id "teachers-link"
    Then I am on the page "teacher"
    And  The title tag has content "This is the Teacher page"
