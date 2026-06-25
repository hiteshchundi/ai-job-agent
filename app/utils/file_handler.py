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