from playwright.sync_api import Page, expect, sync_playwright
import re



html = ""

with sync_playwright() as p:
    browser = p.firefox.launch(headless=False)
    page = browser.new_page()
    page.goto("https://playwright.dev")
    html = page.content()

