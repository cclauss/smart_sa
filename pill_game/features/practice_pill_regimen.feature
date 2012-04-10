Feature: Practice Pill Regimen
    ## The practice pill regimen is currently in Session 1, Activity 7

    Scenario: Find activity
        Using selenium
        Given I am logged in as a counselor
        When I access the url "/"
        When I click the "Let's get started!" link
        When I click the "Intervene" link
        When I fill in "test" in the "name" form field
        When I fill in "test" in the "id_number" form field
        When I submit the "login-participant-form" form
        Then I am on the Intervention page
        
        When I click on Session 1
        When I click on Activity 7
        When I click the "Next" link
        Then there is a game
        
    Scenario: Verify Practice Mode
        Using selenium
        There is a "Practice Regimen" title
        There is not an Add Pill button
        There are 3 pills
        There is a pill named "D4T"
        There is a pill named "3TC"
        There is a pill named "Efavirenz"
        
    Scenario: Drop a pill into the daytime bucket
        Using selenium
        Drop "D4T" into the "day" slot
        There is 1 "D4T" in the "day" slot
        
        
