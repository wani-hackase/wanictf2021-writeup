from playwright.sync_api import sync_playwright


def crawler(username, password):
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        page = browser.new_page()
        page.goto("http://nginx")
        page.type('input[name="username"]', username)
        page.type('input[name="password"]', password)
        page.click('button[type="submit"]')
        page.wait_for_load_state("networkidle")
        browser.close()
