Feature: Manage invoice via Hungarian Tax Authority Online Invoice Interface

  Scenario: Add manual invoice to invoice queue
    Given   Submit new invoice
    When    Application check if it is a manual invoice
    Then    Add invoice to invoice queue