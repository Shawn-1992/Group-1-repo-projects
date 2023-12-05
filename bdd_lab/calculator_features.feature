# Here is a feature file for a basic calculator containing the scenario followed by the steps for testing.

Feature: Basic Calculator

  Scenario: Add and Multiply Numbers
    Given the calculator is on
    When the user adds two numbers
    Then the result should be the sum
    And the user multiplies two numbers
    Then the result should be the product
