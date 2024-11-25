import spacy

# Za³aduj model jêzykowy spaCy
nlp = spacy.load("en_core_web_sm")

# Lista fraz i ich klasyfikacja problemów
PROBLEM_KEYWORDS = {
    "cracked screen": "Pêkniêta szybka",
    "broken": "Uszkodzone urz¹dzenie",
    "not working": "Nie dzia³a",
    "minor scratches": "Drobne rysy",
    "like new": "Jak nowy"
}

def analyze_description(description: str) -> str:
    """
    Analizuje tekst opisu og³oszenia w celu wykrycia problemów technicznych.
    """
    description_lower = description.lower()
    detected_problems = []

    for keyword, problem in PROBLEM_KEYWORDS.items():
        if keyword in description_lower:
            detected_problems.append(problem)

    if not detected_problems:
        return "Brak problemów technicznych"

    return ", ".join(detected_problems)
