Feature: Behave Background Checking

    Background:
        Given   Print "This is Background"
        Then    Print "It prints Background everytime"

    Scenario: First Background Printing
        Given   Print "is Background Printed"
        When    Print "I think so"
        Then    Print "It's passed"

    Scenario: Second Background Printing
        Given   Print "Does second Background Printed"
        When    Print "I am not sure"
        Then    Print "Lets Pass"
