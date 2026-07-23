"""
Hands-On 4
Selenium WebDriver Setup, Browser Drivers & Basic Commands

Selenium Components

1. WebDriver
- Connects Python with the browser.
- Executes browser commands through ChromeDriver.

2. Selenium Grid
- Executes tests on multiple browsers and machines simultaneously.

3. Selenium IDE
- Browser extension used for recording and playback of test cases.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Chrome Options
options = webdriver.ChromeOptions()

# Run in Headless Mode
options.add_argument("--headless=new")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

# Implicit Wait
driver.implicitly_wait(10)

try:

    # Open Selenium Playground
    driver.get("https://www.lambdatest.com/selenium-playground/")

    print("Page Title:")
    print(driver.title)

    # Set Browser Size
    driver.set_window_size(1280, 800)

    print("Window Size:")
    print(driver.get_window_size())

    # Click Simple Form Demo
    driver.find_element(By.LINK_TEXT, "Simple Form Demo").click()

    # Verify URL
    assert "simple-form-demo" in driver.current_url

    print("URL Verified")

    # Back to Home
    driver.back()

    # Open Google in New Tab
    driver.execute_script(
        "window.open('https://www.google.com');"
    )

    print("Tabs:")
    print(driver.window_handles)

    # Switch to Google
    driver.switch_to.window(driver.window_handles[1])

    print("Google Title:")
    print(driver.title)

    # Switch Back
    driver.switch_to.window(driver.window_handles[0])

    # Screenshot
    driver.save_screenshot("playground_screenshot.png")

    print("Screenshot Saved")

finally:
    driver.quit()