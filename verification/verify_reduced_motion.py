
import sys
from playwright.sync_api import sync_playwright

def verify_reduced_motion():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Load the local HTML file
        import os
        cwd = os.getcwd()
        page.goto(f"file://{cwd}/verification/index.html")

        # Emulate prefers-reduced-motion: reduce
        page.emulate_media(reduced_motion="reduce")

        # Get the computed style of the animated element
        box = page.locator(".anim-fade-in")
        animation_name = box.evaluate("el => getComputedStyle(el).animationName")

        print(f"Animation Name (with reduced motion): {animation_name}")

        if animation_name == "none":
            print("SUCCESS: Animation disabled for anim-fade-in")
        else:
            print(f"FAILURE: Animation enabled for anim-fade-in: {animation_name}")
            sys.exit(1)

        # Get the computed style of the transition element
        hover_box = page.locator(".hover-grow")
        transition_property = hover_box.evaluate("el => getComputedStyle(el).transitionProperty")

        print(f"Transition Property (with reduced motion): {transition_property}")

        if transition_property == "none":
            print("SUCCESS: Transition disabled for hover-grow")
        else:
             print(f"FAILURE: Transition enabled for hover-grow: {transition_property}")
             sys.exit(1)

        browser.close()

if __name__ == "__main__":
    verify_reduced_motion()
