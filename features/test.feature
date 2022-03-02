Feature: Test Feature

    Scenario: Implementing Parameters
        Given   Print "First Scenario - Single Parameter"
        When    Two variables "5" and "10"
        Then    Add Two Variable
        And     Check output is "15"

    Scenario Outline: Implementing Multiple Parameters
        Given   Print "Second Scenario - Multiple Parameter"
        When    Two variables "<a>" and "<b>"
        Then    Add Two Variable
        And     Check output is "<c>"

        Examples:
            |   a   |   b   |   c   |
            |   5   |   10   |   15   |
            |   5   |   10   |   15   |
            |   6   |   12   |   18   |
            |   50   |   10   |   60   |
            |   50   |   20   |   70   |

