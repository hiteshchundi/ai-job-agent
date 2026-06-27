import ollama


def extract_keywords(job_description):

    prompt = f"""

    You are an ATS optimization assistant.

    Extract:
    - technical skills
    - tools
    - programming languages
    - platforms
    - important keywords

    from this job description.

    Return only comma-separated keywords.

    Job Description:

    {job_description}

    """

    response = ollama.chat(

        model="llama3",

        messages=[

            {
                "role": "user",

                "content": prompt
            }

        ]
    )

def rewrite_resume_bullet(

    original_bullet,

    job_description
):

    prompt = f"""

    You are an expert ATS resume optimization assistant.

    Rewrite the following resume bullet
    to better align with this job description.

    Keep the experience truthful.

    Make the bullet:
    - stronger
    - achievement-oriented
    - ATS optimized
    - keyword aligned

    JOB DESCRIPTION:

    {job_description}

    ORIGINAL RESUME BULLET:

    {original_bullet}

    Return ONLY the improved bullet.

    """

    response = ollama.chat(

        model="llama3",

        messages=[

            {
                "role": "user",

                "content": prompt
            }

        ]
    )

    return response["message"]["content"]
