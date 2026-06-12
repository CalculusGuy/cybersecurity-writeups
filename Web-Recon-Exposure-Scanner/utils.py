from urllib.parse import urljoin, urlparse


def normalize_url(base, href):
    """Convert relative URLs to absolute URLs."""
    full_url = urljoin(base, href)
    return full_url.split("#")[0].rstrip("/")


def is_internal(base, target):
    """Check if target URL belongs to same domain."""
    return urlparse(base).netloc == urlparse(target).netloc


def risk_level(score):
    """Convert numeric score into risk category."""
    if score >= 7:
        return "HIGH"
    elif score >= 4:
        return "MEDIUM"
    return "LOW"
