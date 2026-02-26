
import sys
import os
from playwright.sync_api import sync_playwright

def verify_reduced_motion_visual():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Determine the absolute path to the HTML file
        cwd = os.getcwd()
        html_path = os.path.join(cwd, "verification/index.html")

        # Load the local HTML file
        page.goto(f"file://{html_path}")

        # Emulate prefers-reduced-motion: reduce
        page.emulate_media(reduced_motion="reduce")

        # Take a screenshot
        screenshot_path = os.path.join(cwd, "verification/reduced_motion_test.png")
        page.screenshot(path=screenshot_path)
        print(f"Screenshot saved to: {screenshot_path}")

        browser.close()

if __name__ == "__main__":
    verify_reduced_motion_visual()
