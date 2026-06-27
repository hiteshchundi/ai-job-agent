from app.ai.resume_generator import (
    generate_tailored_resume
)

from app.ai.export_resume import (
    export_resume_to_docx
)

from app.utils.file_handler import (
    load_existing_jobs
)


jobs = load_existing_jobs()


sample_job = next(

    (
        job for job in jobs

        if job.get("description")
    ),

    None
)


resume_bullets = [

    "Reviewed pharmaceutical application documentation for GxP compliance.",

    "Performed manual quality assurance validation for enterprise systems.",

    "Collaborated with cross-functional teams to resolve documentation issues."

]


tailored_resume = generate_tailored_resume(

    resume_bullets,

    sample_job["description"]
)


export_resume_to_docx(

    tailored_resume,

    "tailored_resume.docx"
)