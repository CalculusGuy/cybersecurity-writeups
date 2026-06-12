import json
import pandas as pd
from pathlib import Path
from datetime import datetime

REPORT_DIR = Path(
    "reports"
)

REPORT_DIR.mkdir(
    exist_ok=True
)


def export(results):

    timestamp = (
        datetime.now()
        .strftime(
            "%Y%m%d_%H%M%S"
        )
    )

    json_file = (
        REPORT_DIR
        /
        f"report_{timestamp}.json"
    )

    csv_file = (
        REPORT_DIR
        /
        f"report_{timestamp}.csv"
    )

    with open(
        json_file,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            results,
            f,
            indent=2
        )

    rows = []

    for r in results:

        rows.append(
            {
                "URL":
                r["url"],

                "Title":
                r["title"],

                "Risk":
                r["risk"],

                "Score":
                r["risk_score"],

                "Findings":
                "; ".join(
                    r["findings"]
                )
            }
        )

    pd.DataFrame(
        rows
    ).to_csv(
        csv_file,
        index=False
    )

    print(
        "\nReports Generated:"
    )

    print(
        json_file
    )

    print(
        csv_file
    )
