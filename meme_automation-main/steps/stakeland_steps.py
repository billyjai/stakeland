from time import sleep

import yaml

from pages import Pages
from pytest_bdd import given, when, then, parsers

parse = parsers.parse


@then("User is on home Page")
@given("User is on home Page")
def on_home_info_page(pages: Pages):
    pages.stakeland_home_page.user_is_on_home_page()


@when(parse("User input case '{case}' stake amount in stake input box"))
def user_input_stake_amount(case: str, pages: Pages):
    with open("yml/test_data.yml", "r") as file:
        data = yaml.safe_load(file)
    case_number = case
    memecoin = data[case_number]["memecoin"]
    pages.stakeland_home_page.input_box_stake(memecoin)


@then(parse("User should see correct steak, slider, wasted in case '{case}'"))
def user_see_correct_steak_slider_wasted(case: str, pages: Pages):
    with open("yml/test_data.yml", "r") as file:
        data = yaml.safe_load(file)
    case_number = case
    memecoin = data[case_number]["memecoin"]
    boost = data[case_number]["boost"]
    pages.stakeland_home_page.assert_change_after_stake_input_box(number=memecoin, boost=boost)


@when(parse("User slides case '{case}' movement in slider"))
def user_slide_in_slider(case: str, pages: Pages):
    with open("yml/test_data.yml", "r") as file:
        data = yaml.safe_load(file)
    case_number = case
    memecoin = data[case_number]["memecoin"]
    pages.stakeland_home_page.slider_moves(memecoin)


@then(parse("User should see correct steak, input box value, wasted in case '{case}'"))
def user_see_correct_steak_slider_wasted(case: str, pages: Pages):
    with open("yml/test_data.yml", "r") as file:
        data = yaml.safe_load(file)
    case_number = case
    memecoin = data[case_number]["memecoin"]
    boost = data[case_number]["boost"]
    pages.stakeland_home_page.assert_change_after_slider_movement(number=memecoin, boost=boost)


@when("User visits New to Stakeland Pop up")
def user_visits_new_to_stakeland(pages: Pages):
    pages.stakeland_home_page.click_new_to_stakeland_button()


@when("User checks New to Stakeland Pop up UI")
def user_checks_new_to_stakeland_ui(pages: Pages):
    pages.stakeland_home_page.check_new_to_stakeland_title()
    pages.stakeland_home_page.scroll_down_in_new_to_stakeland()


@when("User clicks LFG button")
def user_clicks_lfg_button(pages: Pages):
    pages.stakeland_home_page.click_button_lfg()
