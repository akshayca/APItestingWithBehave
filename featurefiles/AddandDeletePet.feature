Feature: Verify if Pet is added and deleted using Library API

  @PetStore
  Scenario: Verify Add and Delete pet API functionality
    Given the pet details which needs to be added to the Petstore
    When we execute the AddPet PostAPI method
    Then the pet is successfully added
    And  status code of response should be 200

#    the pet will delete with the help of 'after_scenario' hook

  @AddData
    Scenario Outline: Verify Add pet API functionality
    Given the pet details with <name> and <status>
    When we execute the AddPet PostAPI method
    Then the pet is successfully added
    And  status code of response should be 200
      Examples:
        |name  |  status |
        | ShibaInu | Available |
        | Chihuahua | Sold |
