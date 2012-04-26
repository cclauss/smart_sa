Feature: SSNMTree Basics
## The tree is in Session 1, Activity 12 & 14
## Defaulter Session 4, Activity 13

    Scenario: 1 - Fill in the tree & test state save
        Using selenium
        Given I am logged in as a counselor
        Given I have logged in a participant
        Given participant "test" is a defaulter
        When I go to Activity 13 of Session 1
        When I click the "Next →" link
        Then there is a game
        When I fill in the SSNM Tree with "regular"
        There is a filled in SSNM Tree with "regular"
        
        # Verify state saved
        When I click the "Next →" link
        When I click the "← Back" link
        There is a filled in SSNM Tree with "regular"
        Finished using Selenium
        
    Scenario: 2 - Test disclosure & support buttons
        Using selenium
        # Disclosure
        Given I am logged in as a counselor
        Given I have logged in a participant
        Given participant "test" is a defaulter
        When I go to Activity 13 of Session 1
        When I click the "Next →" link
        Then there is a game
        When I fill in the SSNM Tree with "regular"
        There is a filled in SSNM Tree with "regular"
        Then "disclosure" is selected
        When I click the circle
        Then the circle is "gold"
        When I click the circle
        Then the circle is not "gold"
        
        # Support
        When I click the "support" button
        When I click the circle
        Then the circle is "purple"
        When I click the circle
        Then the circle is not "purple"
        
        # Disclosure & support
        When I click the "disclosure" button
        When I click the circle
        Then the circle is "gold"
        When I click the "support" button
        When I click the circle
        Then the circle is "gold and purple"
        
        # Verify state saved
        When I click the "Next →" link
        When I click the "← Back" link
        Then the circle is "gold and purple"
        
        # Check the clear functionality
        Then "disclosure" is selected
        When I clear the circle
        Then the circle is not "gold"
        Then the circle is not "purple"
        
        # Circles cannot have attributes w/o a name
        When I click the circle
        Then the circle is not "gold"
        
        # Restore the state
        When I name the circle "regular"
        There is a filled in SSNM Tree with "regular"
        
        Finished using Selenium
        
    Scenario: 3 - Test Defaulter saving
        Using selenium
        Given I am logged in as a counselor
        Given I have logged in a participant
        Given participant "test" is a defaulter
        When I go to Activity 13 of Session 1
        When I click the "Next →" link
        Then there is a game
        When I fill in the SSNM Tree with "regular"
        There is a filled in SSNM Tree with "regular"
        
        When I click the circle
        Then the circle is "gold"
        When I click the "support" button
        When I click the circle
        Then the circle is "gold and purple"
        There is a filled in SSNM Tree with "regular"
        
        When I click the "Sessions" link
        Then I am on the Intervention page
        When I click on Session 4
        When I click on Activity 13
        When I click the "Next →" link
        Then there is a game
        There is a filled in SSNM Tree with "regular"
        Then the circle is "gold and purple"
        When I fill in the SSNM Tree with "defaulter"
        There is a filled in SSNM Tree with "defaulter"
        
        # Clearing out the name (via the fill-in command), clears out the attributes
        Then "disclosure" is selected
        Then the circle is not "gold"
        Then the circle is not "purple"
        
        # Add back some attributes
        When I click the circle
        Then the circle is "gold"
        
        # Verify data saved
        When I click the "Sessions" link
        Then I am on the Intervention page
        When I click on Session 4
        When I click on Activity 13
        When I click the "Next →" link
        There is a filled in SSNM Tree with "defaulter"
        Then the circle is "gold"
        
        # Make sure the regular session data remains the same
        When I click the "Sessions" link
        Then I am on the Intervention page
        When I click on Session 1
        Then I click on Activity 13
        When I click the "Next →" link
        Then there is a game
        There is a filled in SSNM Tree with "regular"  
        Then the circle is "purple"      
        Finished using Selenium                
        
        
            
         
    
    
    
        
