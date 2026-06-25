from app.scraper.linkedin_scraper import search_jobs


def main():

    print("\nStarting AI Job Agent...\n")

    search_jobs()

    print("\nJob scraping completed.\n")


if __name__ == "__main__":
    main()