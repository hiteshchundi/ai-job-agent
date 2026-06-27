from app.database.db import SessionLocal

from app.database.models import Job


def save_jobs_to_db(jobs):

    session = SessionLocal()

    try:

        for job in jobs:

            existing_job = session.query(Job).filter(
                Job.link == job["link"]
            ).first()

            if existing_job:

                continue

            new_job = Job(

                title=job["title"],

                company=job["company"],

                location=job["location"],

                link=job["link"],

                description=job.get(
                    "description",
                    ""
                )
            )

            session.add(new_job)

        session.commit()

        print("\nJobs saved to database successfully!")

    except Exception as e:

        session.rollback()

        print("\nDatabase insertion failed")

        print(e)

    finally:

        session.close()