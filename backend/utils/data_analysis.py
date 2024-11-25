import numpy as np

def calculate_market_statistics(ads: list) -> dict:
    """
    Oblicza statystyki rynkowe na podstawie pobranych ofert.
    """
    prices = [ad["price"] for ad in ads if ad.get("price") is not None]

    if not prices:  # Jeśli brak danych cenowych
        return {"average": None, "median": None, "distribution": []}

    # Obliczenia statystyczne
    average = np.mean(prices)
    median = np.median(prices)
    distribution = np.histogram(prices, bins=10)

    return {
        "average": average,
        "median": median,
        "distribution": {
            "bins": distribution[1].tolist(),  # Przedziały cenowe
            "counts": distribution[0].tolist()  # Liczba ofert w każdym przedziale
        }
    }
