from appium.webdriver.common.appiumby import AppiumBy


def test_android_click(android_driver):
    el = android_driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Battery"]')
    el.click()

    percentage_value = android_driver.find_element(by=AppiumBy.ID, value='com.android.settings:id/usage_summary').text

    assert '100 %' == percentage_value
