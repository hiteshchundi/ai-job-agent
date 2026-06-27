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

    return response["message"]["content"]