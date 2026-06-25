from app.scraper.linkedin_scraper import search_jobs

from app.utils.file_handler import save_jobs_to_json


def main():

    print("\nStarting AI Job Agent...\n")

    jobs = search_jobs()

    save_jobs_to_json(jobs)

    print("\nJob scraping completed.\n")


if __name__ == "__main__":
    main()