import spacy

# Załaduj model językowy spaCy
nlp = spacy.load("en_core_web_sm")

# Lista fraz i ich klasyfikacja problemów
PROBLEM_KEYWORDS = {
    "cracked screen": "Pęknięta szybka",
    "broken": "Uszkodzone urządzenie",
    "not working": "Nie działa",
    "minor scratches": "Drobne rysy",
    "like new": "Jak nowy"
}

def analyze_description(description: str) -> str:
    """
    Analizuje tekst opisu ogłoszenia w celu wykrycia problemów technicznych.
    """
    description_lower = description.lower()
    detected_problems = []

    for keyword, problem in PROBLEM_KEYWORDS.items():
        if keyword in description_lower:
            detected_problems.append(problem)

    if not detected_problems:
        return "Brak problemów technicznych"

    return ", ".join(detected_problems)
