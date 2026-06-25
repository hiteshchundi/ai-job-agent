import json


def save_jobs_to_json(jobs, filename="jobs.json"):

    with open(filename, "w", encoding="utf-8") as file:

        json.dump(
            jobs,
            file,
            indent=4,
            ensure_ascii=False
        )

    print(f"\nSaved {len(jobs)} jobs to {filename}")

def load_existing_jobs(filename="jobs.json"):

    try:

        with open(filename, "r", encoding="utf-8") as file:

            jobs = json.load(file)

            return jobs

    except FileNotFoundError:

        return []