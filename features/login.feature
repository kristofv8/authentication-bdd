Feature: Login to admin

  As a user, verify user should be able to login as user with valid credentials
  As a user, verify user should be able to logout from system
  As a user, verify user should not be able to login with invalid username
  As a user, verify user should not be able to login with invalid password

  Background:
    Given user opens the website

  @smoke @critical
  Scenario: verify user should be able to login as user with valid credentials
    And user enters the user username and password
    And user clicks on the login button
    Then user should see the dashboard with header and side menu

  @smoke @critical
  Scenario: verify user should be able to logout from system
    And user enters the user username and password
    And user clicks on the login button
    Then user should see the dashboard with header and side menu
    And user clicks on the all apps link
    And user clicks on the logout link
    Then user should see the logout page

  @normal
  Scenario: verify user should not be able to login with invalid username
    And user enters the invalid username and password
    And user clicks on the login button
    Then user should be able to see the error message

  @normal
  Scenario: verify user should not be able to login with invalid password
    And user enters the username and invalid password
    And user clicks on the login button
    Then user should be able to see the error message
