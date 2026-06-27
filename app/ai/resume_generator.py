from app.ai.resume_tailor import rewrite_resume_bullet


def generate_tailored_resume(

    resume_bullets,

    job_description
):

    tailored_bullets = []

    for bullet in resume_bullets:

        improved_bullet = rewrite_resume_bullet(

            bullet,

            job_description
        )

        tailored_bullets.append(
            improved_bullet
        )

    return tailored_bullets