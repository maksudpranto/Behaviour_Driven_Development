Feature: Login to Orange HRM
  Scenario: Login to Orange HRM with valid data
    Given I launch chrome browser
    When I open Orange HRM Homepage
    And I enter username "Admin" and Password "admin123"
    And I click login button
    Then User must successfully logged in


