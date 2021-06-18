Feature: Login Orange HRM

  Scenario Outline: : Login to Orange HRM with multiple sets of data
    Given Launching the chrome browser
    When Open the Homepage
    And Enter the username "<username>" and password "<password>"
    And I click the Login button
    Then User successfully logged in when the data is valid


    Examples:
      | username | password  |
      | Admin    | admin123 |
      | pranto   | pranto123 |
      | ray      | ray123    |
      | rayxyx   | rayxy     |


