import requests

BASE_URL = "https://www.olx.pl/api/v1"

def fetch_ads(category: str, min_price: int = None, max_price: int = None) -> list:
    """
    Pobiera oferty z OLX API na podstawie kategorii i opcjonalnych filtrów cenowych.
    """
    params = {"category": category}
    if min_price:
        params["min_price"] = min_price
    if max_price:
        params["max_price"] = max_price

    try:
        response = requests.get(f"{BASE_URL}/ads", params=params)
        response.raise_for_status()
        return response.json().get("data", [])
    except requests.exceptions.RequestException as e:
        print(f"Error fetching ads: {e}")
        return []
