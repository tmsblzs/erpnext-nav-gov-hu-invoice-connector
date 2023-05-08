Feature: Import purchase invoice
  Querying purchase invoice from NAV GOV HU online invoice system
  and import to ERPNext

  @implemented
  @wip
  Scenario: No purchase invoice to import
    Given   Querying purchase invoice
    When    No purchase invoice
    Then    Return without error

  Scenario: No supplier in ERPNext
    Given   Querying purchase invoice
    When    New supplier in the response
    Then    Add new supplier to ERPNext

  Scenario: No item in ERPNext
    Given   Querying purchase invoice
    When    New item in the response
    Then    Add new item to ERPNext