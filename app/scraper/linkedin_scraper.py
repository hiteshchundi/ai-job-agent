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

        job_cards = page.locator(".base-search-card")

        count = job_cards.count()

        print(f"\nFound {count} job cards\n")

        for i in range(count):

            card = job_cards.nth(i)

            title = card.locator(
                ".base-search-card__title"
            ).inner_text()

            company = card.locator(
                ".base-search-card__subtitle"
            ).inner_text()

            location = card.locator(
                ".job-search-card__location"
            ).inner_text()

            print(f"Job {i + 1}")
            print(f"Title: {title}")
            print(f"Company: {company}")
            print(f"Location: {location}")
            print("-" * 50)

        input("Press Enter to close browser...")

        browser.close()


if __name__ == "__main__":
    search_jobs()