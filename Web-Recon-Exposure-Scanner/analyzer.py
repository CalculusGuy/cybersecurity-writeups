import re
import requests
from bs4 import BeautifulSoup, Comment
from utils import risk_level

EMAIL_REGEX = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-z]{2,}"

SECURITY_HEADERS = [
    "Content-Security-Policy",
    "Strict-Transport-Security",
    "X-Frame-Options",
    "X-Content-Type-Options",
    "Referrer-Policy",
    "Permissions-Policy"
]


def analyze_headers(headers):

    findings = []
    score = 0

    for header in SECURITY_HEADERS:

        if header not in headers:
            findings.append(
                f"Missing Security Header: {header}"
            )
            score += 1

    return findings, score


def analyze_page(url, html, headers):

    soup = BeautifulSoup(html, "html.parser")

    findings = []
    score = 0

    title = (
        soup.title.text.strip()
        if soup.title
        else "Untitled"
    )

    links = []

    for a in soup.find_all("a", href=True):

        href = a["href"]
        links.append(href)

        sensitive = [
            "admin",
            "login",
            "upload",
            "dashboard",
            "backup",
            "config",
            "secret"
        ]

        if any(
            word in href.lower()
            for word in sensitive
        ):
            findings.append(
                f"Sensitive Endpoint: {href}"
            )
            score += 2

    forms = soup.find_all("form")

    for form in forms:

        action = form.get("action", "")

        if "login" in action.lower():
            findings.append(
                f"Login Form: {action}"
            )
            score += 2

        if "upload" in action.lower():
            findings.append(
                f"Upload Form: {action}"
            )
            score += 3

    comments = soup.find_all(
        string=lambda text:
        isinstance(text, Comment)
    )

    if comments:
        findings.append(
            f"HTML Comments Found ({len(comments)})"
        )
        score += 1

    scripts = soup.find_all(
        "script",
        src=True
    )

    if scripts:
        findings.append(
            f"JavaScript Files Found ({len(scripts)})"
        )
        score += 1

    emails = list(
        set(
            re.findall(
                EMAIL_REGEX,
                html
            )
        )
    )

    if emails:
        findings.append(
            f"Emails Exposed ({len(emails)})"
        )
        score += 2

    header_findings, header_score = analyze_headers(
        headers
    )

    findings.extend(
        header_findings
    )

    score += header_score

    return {
        "url": url,
        "title": title,
        "risk_score": score,
        "risk": risk_level(score),
        "findings": findings,
        "links": links,
        "emails": emails
    }


def analyze_robots(base_url):

    robots_url = base_url.rstrip("/") + "/robots.txt"

    findings = []

    try:

        response = requests.get(
            robots_url,
            timeout=5
        )

        if response.status_code == 200:

            for line in response.text.splitlines():

                if line.startswith(
                    "Disallow:"
                ):
                    findings.append(
                        line.strip()
                    )

    except:
        pass

    return findings
