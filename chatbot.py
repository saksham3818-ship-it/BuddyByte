import os
from dotenv import load_dotenv

# Load API keys
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")


def _get_active_provider_and_key():
    if GEMINI_API_KEY and GEMINI_API_KEY.startswith("AIza"):
        return "gemini", GEMINI_API_KEY
    if GROQ_API_KEY:
        return "groq", GROQ_API_KEY
    if GEMINI_API_KEY:
        return "gemini", GEMINI_API_KEY
    return None, None


def get_response(question):
    provider, api_key = _get_active_provider_and_key()

    if not api_key:
        return (
            "GROQ_API_KEY or GEMINI_API_KEY is missing. Please add it to your .env file "
            "to enable AI responses."
        )

    try:
        if provider == "gemini":
            try:
                from google import genai
            except ModuleNotFoundError:
                return (
                    "Gemini support is not installed. Run: pip install google-genai"
                )

            client = genai.Client(api_key=api_key)
            response = client.models.generate_content(
                model="gemini-2.0-flash",
                contents=(
                    "You are an AI Student Support Assistant. Help students with programming, "
                    "Python, Java, DSA, DBMS, Operating Systems, Computer Networks, AI, "
                    "Machine Learning, assignments, placements, interview preparation, and "
                    "career guidance. Answer in a simple and friendly way.\n\nUser: "
                    + question
                ),
            )

            if hasattr(response, "text") and response.text:
                return response.text
            if hasattr(response, "candidates") and response.candidates:
                return response.candidates[0].content.parts[0].text
            return str(response)

        from groq import Groq

        client = Groq(api_key=api_key)
        completion = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are an AI Student Support Assistant. "
                        "Help students with programming, Python, Java, DSA, DBMS, "
                        "Operating Systems, Computer Networks, AI, Machine Learning, "
                        "assignments, placements, interview preparation, and career guidance. "
                        "Answer in a simple and friendly way."
                    ),
                },
                {
                    "role": "user",
                    "content": question,
                },
            ],
            temperature=0.7,
            max_tokens=1024,
        )

        return completion.choices[0].message.content

    except Exception as e:
        return f"Error: {e}"


# Test in Terminal
if __name__ == "__main__":

    while True:

        q = input("You: ")

        if q.lower() == "exit":
            break

        print("\nAssistant:\n")

        print(get_response(q))