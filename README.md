# `Stakeland` Automation testing assignment by Billy Lam



## Introduction
This is the demo code so it cannot be run at this moment but I have try my best to complete 70% of it. The missing is part is just the driver setup for all browsers, correct element name and setting up a selenium web driver action.

I am using a **Page Object Model** to separate Feature, Steps and Pages. It can be easily managed.

## Poetry and virtual Env
If the project is completed, I suggest QA can use virtual env and poetry to install the relevant library on this project.
Please run the poetry command to install the package:

```shell
poetry install
```

## Mobile testing set up
You can also set up the testing device info into the config file
config.yml
```yaml
platform: &platform
    platform: android

device_config: &device_config
    ios:
        platformName: 'ios'
        platformVersion: '13.5'
        deviceName: 'iPhone 11 Pro MT'
        automationName: 'XCUITest'
        appPackage: ''
        appActivity: ''
        noReset: True
        folder: 'xxxxx'
    android:
        platformName: 'android'
        platformVersion: '12'
        deviceName: 'xxxxx'
        automationName: 'uiautomator2'
        appPackage: 'xxxxx'
        app: 'xxxxx'
        noReset: False
        fullReset: True

production:
    <<: *platform
    <<: *device_config
```

## Run the file
```shell
poetry run pytest test/stakeland.py -vs
```
You will get the correct result like this. Every action it did will be recorded here
```output
Given User is on home Page
When User slides case '4Ns2Sp' movement in slider
Then User should see correct steak, input box value, wasted in case '4Ns2Sp'
PASSED

```
However, if the page is not accessed, you will get an assertion error here.
```output
Given User is on home Page
When User visits New to Stakeland Pop up
And User checks New to Stakeland Pop up UI
And User clicks LFG button
Then User is on home Page
FAILED

E       AssertionError: The element is not found
```

## Code Introduction
I try to make the BDD steps to be dynamic because we can have so many test combinations in the simulator so I use a yaml file to store all the test data. Then pass the test case to the step to retrieve the data. Therefore, you just need to edit the `test_data.yml` to input all combinations
```python
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
```

Then I will do the assertion to the value I added from test_data.yml to see if it is same as in the web
    
I have special testing method to the slider because I see that there's a value from 1-100 to indicate the movement of the slide bar so I use `memecoin / 6900000 * 100` to calculate the movement
```python
    def slider_moves(self, memecoin):
        self.slider_move(self.slider_memecoin, memecoin / 6900000 * 100)
        
    def assert_change_after_slider_movement(self, number: float, boost: float):
        meme_coin_value = float(self.text(self.label_memecoin_value))
        steak_value = float(self.text(self.label_steak_value))
        wasted = float(self.text(self.label_wasted))
        meme_input_box = float(self.text(self.input_box_stake))
        boost = float(self.text(self.label_boost_value))

        assert_that(meme_coin_value, equal_to(number), "meme_coin_value is incorrect")
        assert_that(steak_value, equal_to(number * boost), "steak_value is incorrect")
        assert_that(wasted, equal_to(6900000 - number), "wasted is incorrect")
        assert_that(meme_input_box, equal_to(number), "stake input bos is incorrect")
```
