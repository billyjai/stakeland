import yaml
from hamcrest import assert_that
from pages.base_screen import BaseScreen


class StakeLandHomePage(BaseScreen):
    # Stake Calculation
    input_box_stake = ("xpath", "//a[contains(@aria-label, 'Stake Amount:')]")
    label_memecoin_value = ("xpath", "//a[contains(@aria-label, 'Meme Coin Value')]")
    label_steak_value = ("xpath", "//a[contains(@aria-label, 'Steak Value')]")
    label_wasted = ("xpath", "//a[contains(@aria-label, 'Wasted')]")
    slider_memecoin = ("xpath", "//a[contains(@aria-label, 'Slider')]")
    button_max = ("xpath", "//a[contains(@aria-label, 'Max')]")
    label_boost_value = ("xpath", "//a[contains(@aria-label, 'Boost Value')]")

    # New To Stakeland button
    button_new_to_stakeland = ("xpath", "//a[contains(@aria-label, 'new_to_stakeland')]")
    label_stakeland_guide = ("xpath", "//a[contains(@aria-label, 'Stakeland Guide')]")
    button_LFG = ("xpath", "//a[contains(@aria-label, 'LFG')]")
    label_complete_quests_farm_steak = ("xpath", "//a[contains(@aria-label, 'Complete Quests, Farm Steaks!')]")
    new_to_stakeland_pop_up_container = ("xpath", "//a[contains(@aria-label, 'New to Stakeland Container')]")

    # Base button
    button_base = ("xpath", "//a[contains(@aria-label, 'Base Button')]")
    label_base = ("xpath", "//a[contains(@aria-label, 'Base')]")
    button_close = ("xpath", "//a[contains(@aria-label, 'Close')]")

    # home page
    title_meme_staking = ("xpath", "//a[contains(@aria-label, 'Meme Staking')]")

    def label_per_nft_crew(self, row) -> tuple:
        return "xpath", f"//a[contains(@aria-label, 'Per NFT/Crew')][{row}]"

    def label_quota(self, row) -> tuple:
        return "xpath", f"//a[contains(@aria-label, 'Quota')][{row}]"

    def user_is_on_home_page(self):
        self.is_visible(self.title_meme_staking)

    def input_stake_inputbox(self, number):
        self.send_keys(self.input_box_stake, number)

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

    def assert_change_after_stake_input_box(self, number: float, boost: float):
        meme_coin_value = float(self.text(self.label_memecoin_value))
        steak_value = float(self.text(self.label_steak_value))
        wasted = float(self.text(self.label_wasted))
        slider_movement = float(self.slider_movement(self.slider_memecoin))
        boost = float(self.text(self.label_boost_value))

        assert_that(meme_coin_value, equal_to(number), "meme_coin_value is incorrect")
        assert_that(steak_value, equal_to(number * boost), "steak_value is incorrect")
        assert_that(wasted, equal_to(6900000 - number), "wasted is incorrect")
        assert_that(slider_movement, equal_to(number / 6900000), "slider movement is incorrect")

    def click_new_to_stakeland_button(self):
        self.click(self.button_new_to_stakeland)

    def check_new_to_stakeland_title(self):
        self.is_visible(self.label_stakeland_guide)

    def scroll_down_in_new_to_stakeland(self):
        self.scrolling(self.new_to_stakeland_pop_up_container, "Chrome")
        self.is_visible(self.label_complete_quests_farm_steak)

    def click_button_lfg(self):
        self.click(self.button_LFG)
