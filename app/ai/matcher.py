import ollama

import numpy as np


def get_embedding(text):

    response = ollama.embeddings(

        model="nomic-embed-text",

        prompt=text
    )

    return response["embedding"]


def cosine_similarity(vec1, vec2):

    vec1 = np.array(vec1)

    vec2 = np.array(vec2)

    similarity = np.dot(vec1, vec2) / (

        np.linalg.norm(vec1)

        * np.linalg.norm(vec2)
    )

    return similarity


def match_resume_to_jobs(
    resume_text,
    jobs
):

    print("\nGenerating resume embedding...\n")

    resume_embedding = get_embedding(
        resume_text
    )

    scored_jobs = []

    for job in jobs:

        description = job.get(
            "description",
            ""
        )

        if not description:
            continue

        print(
            f"Matching: {job['title']}"
        )

        job_embedding = get_embedding(
            description
        )

        score = cosine_similarity(
            resume_embedding,
            job_embedding
        )

        scored_jobs.append({

            "title": job["title"],

            "company": job["company"],

            "score": round(score, 4)
        })

    scored_jobs.sort(

        key=lambda x: x["score"],

        reverse=True
    )

    return scored_jobs