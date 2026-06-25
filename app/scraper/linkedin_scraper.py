from playwright.sync_api import sync_playwright


def search_jobs():

    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=False
        )

        page = browser.new_page()

        page.set_viewport_size({
            "width": 1400,
            "height": 900
        })

        page.goto(
            "https://www.linkedin.com/jobs/search/?keywords=data%20analyst&location=India"
        )

        page.wait_for_load_state("networkidle")

        job_cards = page.locator(".base-search-card")

        count = job_cards.count()

        print(f"\nFound {count} jobs\n")

        jobs = []

        for i in range(count):

            try:

                card = job_cards.nth(i)

                title = card.locator(
                    ".base-search-card__title"
                ).inner_text().strip()

                company = card.locator(
                    ".base-search-card__subtitle"
                ).inner_text().strip()

                location = card.locator(
                    ".job-search-card__location"
                ).inner_text().strip()

                job_link = card.locator(
                    ".base-card__full-link"
                ).get_attribute("href")

                job_data = {
                    "title": title,
                    "company": company,
                    "location": location,
                    "link": job_link
                }

                jobs.append(job_data)

            except Exception as e:

                print(f"Error extracting card {i + 1}")
                print(e)

        print("\nEXTRACTED JOBS\n")

        for job in jobs:

            print("=" * 80)

            print(f"Title: {job['title']}")
            print(f"Company: {job['company']}")
            print(f"Location: {job['location']}")
            print(f"Link: {job['link']}")

        print("\nSCRAPING JOB DESCRIPTIONS\n")

        for index, job in enumerate(jobs):

            try:

                print(f"\nOpening Job {index + 1}")

                detail_page = browser.new_page()

                detail_page.goto(job["link"])

                detail_page.wait_for_load_state("networkidle")

                try:

                    description = detail_page.locator(
                        ".show-more-less-html__markup"
                    ).inner_text()

                except:

                    description = "Description not found"

                print(f"\n{job['title']}")
                print(f"\nDescription Preview:\n")

                print(description[:1000])

                detail_page.close()

            except Exception as e:

                print(f"Error scraping job detail page")
                print(e)

        input("\nPress Enter to close browser...")

        browser.close()


if __name__ == "__main__":
    search_jobs()