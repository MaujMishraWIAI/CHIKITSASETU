import openai

def extract_prescription(img_base64):
    prompt = """
    Extract the medicine names and their dosages per day from the prescription image provided. Follow these instructions carefully:

    - Output only in bullet points — no extra text or commentary.
    - For each medicine, include:
    - Correct medicine name (auto-correct any misspellings to the nearest valid drug name using medical spelling standards).
    - Dosage per intake (e.g., 500 mg, 1 tablet, etc.).
    - Frequency per day, identified using standard medical abbreviations or patterns (e.g., OD, BD, TDS, QID, HS).
    - Time of administration if available (e.g., morning, after food, night).
    - Normalize and standardize all extracted information (e.g., convert "twice a day" or "BD" to "2 times/day").
    - If frequency or dosage is missing or ambiguous, infer from context or note as “unspecified”.
    - Do not include vitamins or supplements unless explicitly prescribed with a dosage.
    """
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{img_base64}"}}
                ]
            }
        ],
        max_tokens=600,
        temperature=0
    )

    return response.choices[0].message.content, response.usage