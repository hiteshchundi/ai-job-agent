from app.ai.resume_tailor import extract_keywords

from app.utils.file_handler import load_existing_jobs


jobs = load_existing_jobs()


sample_job = next(

    (
        job for job in jobs

        if job.get("description")
    ),

    None
)

if not sample_job:

    print("No job descriptions found")

    exit()

keywords = extract_keywords(

    sample_job.get(
        "description",
        ""
    )
)


print("\nEXTRACTED KEYWORDS\n")

print(keywords)