import requests
from collections import deque
from analyzer import analyze_page
from utils import (
    normalize_url,
    is_internal
)

SKIP_EXTENSIONS = (
    ".pdf",
    ".jpg",
    ".jpeg",
    ".png",
    ".gif",
    ".svg",
    ".zip",
    ".exe",
)

HEADERS = {
    "User-Agent":
    "WebReconScanner/1.1"
}


def discover_sitemap(start_url):

    sitemap_url = (
        start_url.rstrip("/")
        + "/sitemap.xml"
    )

    try:

        response = requests.get(
            sitemap_url,
            timeout=5
        )

        if response.status_code == 200:

            print(
                f"[+] Sitemap discovered"
            )

    except:
        pass


def crawl(
    start_url,
    max_depth,
    max_pages
):

    visited = set()

    queue = deque(
        [
            (
                start_url,
                0
            )
        ]
    )

    queued = set(
        [
            start_url
        ]
    )

    report = []

    session = requests.Session()

    discover_sitemap(
        start_url
    )

    while queue:

        if len(visited) >= max_pages:
            break

        current_url, depth = (
            queue.popleft()
        )

        if current_url in visited:
            continue

        if depth > max_depth:
            continue

        visited.add(
            current_url
        )

        try:

            print(
                f"[{len(visited)}/{max_pages}] "
                f"{current_url}"
            )

            response = session.get(
                current_url,
                timeout=5,
                headers=HEADERS
            )

            if (
                "text/html"
                not in response.headers.get(
                    "Content-Type",
                    ""
                )
            ):
                continue

            page_data = analyze_page(
                current_url,
                response.text,
                response.headers
            )

            report.append(
                page_data
            )

            for href in page_data[
                "links"
            ]:

                full_url = (
                    normalize_url(
                        current_url,
                        href
                    )
                )

                if (
                    full_url.endswith(
                        SKIP_EXTENSIONS
                    )
                ):
                    continue

                if not is_internal(
                    start_url,
                    full_url
                ):
                    continue

                if (
                    full_url not in visited
                    and full_url
                    not in queued
                ):

                    queue.append(
                        (
                            full_url,
                            depth + 1
                        )
                    )

                    queued.add(
                        full_url
                    )

        except Exception as e:

            print(
                f"Error: {e}"
            )

    return report
