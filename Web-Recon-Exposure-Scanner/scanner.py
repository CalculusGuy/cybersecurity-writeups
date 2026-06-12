import argparse

from crawler import crawl
from reporter import export
from analyzer import (
    analyze_robots
)

parser = argparse.ArgumentParser()

parser.add_argument(
    "--url",
    required=True,
    help="Target URL"
)

parser.add_argument(
    "--depth",
    type=int,
    default=2
)

parser.add_argument(
    "--pages",
    type=int,
    default=50
)

args = parser.parse_args()

print("=" * 60)
print("WEB RECON & EXPOSURE SCANNER v1.1")
print("=" * 60)

robots = analyze_robots(
    args.url
)

if robots:

    print(
        "\nrobots.txt Findings:"
    )

    for r in robots:
        print(
            f"  {r}"
        )

results = crawl(
    args.url,
    args.depth,
    args.pages
)

print(
    f"\nPages Analyzed: "
    f"{len(results)}"
)

export(results)

print(
    "\nScan Complete."
)
