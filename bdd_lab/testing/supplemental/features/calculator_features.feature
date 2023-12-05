# Here is a feature file for a basic calculator containing the scenario followed by the steps for testing.

Feature: Basic Calculator

  Scenario: Add and Multiply Numbers
    Given the calculator is on
    When the user adds two numbers
    Then the result should be the sum
    When the user multiplies two numbers
    Then the result should be the product


  Scenario: Divide Numbers
    Given the calculator is on
    When the user divides two numbers
    Then the result should be the quotient


  Scenario: Subtract Numbers
    Given the calculator is on
    When the user subtracts two numbers
    Then the result should be the difference


  Scenario: Handle Negative Numbers
    Given the calculator is on
    When the user subtracts a larger number from a smaller number
    Then the result should be a negative difference
