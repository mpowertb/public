import os
import openai  # oder nutze HuggingFace Transformers

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_summary(analysis):
    prompt = "Fasse die folgenden statistischen Kennzahlen in natürlicher Sprache zusammen:\n\n"
    for col, stats in analysis.items():
        prompt += f"{col}: Mittelwert={stats['mean']:.2f}, Median={stats['median']:.2f}, Std={stats['std']:.2f}\n"

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

    return response.choices[0].message["content"]
