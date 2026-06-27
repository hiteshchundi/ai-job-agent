from app.ai.matcher import match_resume_to_jobs

from app.utils.file_handler import load_existing_jobs

from app.ai.resume_parser import parse_resume


resume_text = parse_resume(
    "data/resume/resume1.docx"
)


jobs = load_existing_jobs()


results = match_resume_to_jobs(
    resume_text,
    jobs
)


print("\nTOP MATCHED JOBS\n")


for job in results[:10]:

    print("=" * 60)

    print(f"Title: {job['title']}")

    print(f"Company: {job['company']}")

    print(f"Match Score: {job['score']}")