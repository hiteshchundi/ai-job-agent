from app.scraper.linkedin_scraper import search_jobs

from app.utils.file_handler import save_jobs_to_json

from app.utils.file_handler import load_existing_jobs


def main():

    print("\nStarting AI Job Agent...\n")

    existing_jobs = load_existing_jobs()

    existing_links = {
        job["link"]
        for job in existing_jobs
    }

    scraped_jobs = search_jobs()

    new_jobs = []

    for job in scraped_jobs:

        if job["link"] not in existing_links:

            new_jobs.append(job)

    updated_jobs = existing_jobs + new_jobs

    save_jobs_to_json(updated_jobs)

    print(f"\nFound {len(new_jobs)} new jobs")

    print("\nJob scraping completed.\n")

if __name__ == "__main__":
    main()