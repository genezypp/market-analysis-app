import spacy

# Za�aduj model j�zykowy spaCy
nlp = spacy.load("en_core_web_sm")

# Lista fraz i ich klasyfikacja problem�w
PROBLEM_KEYWORDS = {
    "cracked screen": "P�kni�ta szybka",
    "broken": "Uszkodzone urz�dzenie",
    "not working": "Nie dzia�a",
    "minor scratches": "Drobne rysy",
    "like new": "Jak nowy"
}

def analyze_description(description: str) -> str:
    """
    Analizuje tekst opisu og�oszenia w celu wykrycia problem�w technicznych.
    """
    description_lower = description.lower()
    detected_problems = []

    for keyword, problem in PROBLEM_KEYWORDS.items():
        if keyword in description_lower:
            detected_problems.append(problem)

    if not detected_problems:
        return "Brak problem�w technicznych"

    return ", ".join(detected_problems)
