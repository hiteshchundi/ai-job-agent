from playwright.sync_api import sync_playwright


def search_jobs():

    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=False
        )

        page = browser.new_page()

        page.goto(
            "https://www.linkedin.com/jobs/search/?keywords=data%20analyst&location=India"
        )

        page.wait_for_timeout(5000)

        print(page.title())

        input("Press Enter/Return to close browser...")

        browser.close()


if __name__ == "__main__":
    search_jobs()