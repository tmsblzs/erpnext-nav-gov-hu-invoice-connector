Feature: Quering taxpayer data
        from Hungarion Tax Authority (NAV)

        Scenario: Querying a new customer with tax number
                Given   Open new customer add form
                When    Enter at least the first eight number of the tax number of the customer
                And     Click Nav menu Query taxpayer menuitem
                And     Display dialog window with taxpayer data and answer 'Yes'
                Then    Save tax payer data to database


        Scenario: Querying a new customer with tax number
                Given   Open new customer add form
                When    Enter at least the first eight number of the tax number of the customer
                And     Click Nav menu Query taxpayer menuitem
                And     Display dialog window with taxpayer data and answer 'No'
                Then    Not save tax payer data to database


        Scenario: Show error message if the given tax number is not valid
                Given   Open new customer add form
                When    Enter tax number that length is less than eight number
                And     Click Nav menu Query taxpayer menuitem
                Then    Show error message tax number is not valid


        Scenario: Show error message if the given tax number is not exists
                Given   Open new customer add form
                When    Enter tax number that is not exists
                And     Click Nav menu Query taxpayer menuitem
                Then    Show error message the given tax number is not exists


        Scenario: Querying a tax number for an existing customer as a new one, no modification
                Given   Enter a tax number that is already saved for a customer
                When    Display a dialog 'Would you like to modified an existing customer?'
                And     Answer 'No'
                Then    Not modified the existing customer


        Scenario: Querying a tax number for an existing customer as a new one, adjusted
                Given   Enter a tax number that is already saved for a customer
                When    Display a dialog 'Would you like to modified an existing customer?'
                And     Answer 'Yes'
                Then    Adjust the existing customer's data


        Scenario: Modifying tax number of an existing customer
                Given   Open an existing customer form
                When    Adjust tax number for an existing customer
                And     Click Nav menu Query taxpayer menuitem
                And     Display dialog window with taxpayer data and answer 'Yes'
                Then    Adjust the existing customer's data
