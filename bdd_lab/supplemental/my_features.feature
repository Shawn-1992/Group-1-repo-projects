# calculator.feature

Feature: Basic Calculator

  Scenario: Add and Multiply Numbers
    Given the calculator is on
    When the user adds two numbers
    Then the result should be the sum
    And the user multiplies two numbers
    Then the result should be the product
