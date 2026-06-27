from app.ai.resume_tailor import rewrite_resume_bullet

from app.utils.file_handler import load_existing_jobs


jobs = load_existing_jobs()


sample_job = next(

    (
        job for job in jobs

        if job.get("description")
    ),

    None
)


original_bullet = """

Reviewed pharmaceutical application
documentation for GxP compliance.

"""


rewritten = rewrite_resume_bullet(

    original_bullet,

    sample_job["description"]
)


print("\nORIGINAL BULLET\n")

print(original_bullet)


print("\nREWRITTEN BULLET\n")

print(rewritten)