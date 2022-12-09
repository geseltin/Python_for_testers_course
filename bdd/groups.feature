Scenario Outline: add new group
    Given a group list
    Given a group with <name>, <header>, and <footer>
    When I add the group to the list
    Then the new group list is equal to the old list with the added group

    Examples:
    | name  | header  | footer  |
    | name1 | header1 | footer1 |
    | name2 | header2 | footer2 |

Scenario Outline: modify random group
    Given check if group list is not empty
    Given a group list
    Given choose random group and generate data to modify
    When modify random group
    Then the new group list is equal to the old list with modified group

Scenario Outline: delete random group
    Given check if group list is not empty
    Given a group list
    Given choose random group
    When delete group
    Then the new group list is equal to the old list without deleted group


