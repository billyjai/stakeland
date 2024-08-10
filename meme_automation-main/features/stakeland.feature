# Created by billylam at 7/8/2024
Feature: Stakeland Calculation and UI testing

#Check New to Stakeland UI
  Scenario: [5Bj7Qc] User checks New to Stakeland UI
    Given User is on home Page
    When User visits New to Stakeland Pop up
    And User checks New to Stakeland Pop up UI
    And User clicks LFG button
    Then User is on home Page

#Check memecoin, steak, wasted, slider change after input in stake input box

#Boost 1X
#Slide to the middle
  Scenario: [3Th4Uy] Slider movement affects stake input box, meme coins staked number and steaks/week
    Given User is on home Page
    When User slides case '3Th4Uy' movement in slider
    Then User should see correct steak, input box value, wasted in case '3Th4Uy'

#Boost 1X
#Slide to the rightmost
  Scenario: [8Af3If] Slider move rightmost hits maximum for input box, meme coins staked number and steaks/week
    Given User is on home Page
    When User slides case '8Af3If' movement in slider
    Then User should see correct steak, input box value, wasted in case '8Af3If'

#Boost 1X
#Slide to the leftmost
  Scenario: [4Ns2Sp] Slider remains leftmost and input box, meme coins staked number and steaks/week remain zero
    Given User is on home Page
    When User slides case '4Ns2Sp' movement in slider
    Then User should see correct steak, input box value, wasted in case '4Ns2Sp'

#Stake Input Box changed affects meme coins staked number and steaks/week

#Boost: 1X
#Input: 1
  Scenario: [0Nj4Jo] Stake Input Box changed affects meme coins staked number and steaks/week
    Given User is on home Page
    When User input case '0Nj4Jo' stake amount in stake input box
    Then User should see correct steak, slider, wasted in case '0Nj4Jo'

#Boost: 2X
#Input: 1,000,000
  Scenario: [0Nj4Jo] Stake Input Box changed affects meme coins staked number, steaks/week and slider with boost
    Given User is on home Page
    When User input case '0Nj4Jo' stake amount in stake input box
    Then User should see correct steak, slider, wasted in case '0Nj4Jo'

#Boost: 2X
#Input: 0
  Scenario: [9Ok4Tq] Stake Input Box remains zero and it would not be affected by boost
    Given User is on home Page
    When User input case '9Ok4Tq' stake amount in stake input box
    Then User should see correct steak, slider, wasted in case '9Ok4Tq'