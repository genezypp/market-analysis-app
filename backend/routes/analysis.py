from fastapi import APIRouter, HTTPException
from utils.olx_api import fetch_ads
from utils.data_analysis import calculate_market_statistics
from fastapi import APIRouter, HTTPException
from utils.olx_api import fetch_ads
from utils.text_analysis import analyze_description

router = APIRouter()

@router.get("/prices")
def get_price_analysis(category: str, min_price: int = None, max_price: int = None):
    """
    Endpoint do analizy cen.
    """
    ads = fetch_ads(category, min_price, max_price)
    if not ads:
        raise HTTPException(status_code=404, detail="No ads found for the given criteria")

    stats = calculate_market_statistics(ads)
    return stats

@router.get("/market-depth")
def get_market_depth(category: str, min_price: int, max_price: int):
    """
    Endpoint do analizy g³êbokoœci rynku (oferty w przedziale cenowym).
    """
    ads = fetch_ads(category, min_price, max_price)
    if not ads:
        raise HTTPException(status_code=404, detail="No ads found for the given criteria")

    # Lista ofert w wybranym przedziale cenowym
    return [{"title": ad["title"], "price": ad["price"], "url": ad["url"]} for ad in ads]

@router.get("/market-depth")
def get_market_depth_with_analysis(category: str, min_price: int, max_price: int):
    """
    Endpoint do analizy g³êbokoœci rynku z analiz¹ tekstu og³oszeñ.
    """
    ads = fetch_ads(category, min_price, max_price)
    if not ads:
        raise HTTPException(status_code=404, detail="No ads found for the given criteria")

    results = []
    for ad in ads:
        results.append({
            "title": ad["title"],
            "price": ad["price"],
            "description": ad.get("description", ""),
            "problems": analyze_description(ad.get("description", "")),
            "url": ad["url"]
        })

    return results