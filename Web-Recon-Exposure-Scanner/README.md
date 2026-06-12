# Web Reconnaissance & Exposure Scanner

## Overview

Web Reconnaissance & Exposure Scanner is a modular Python-based security reconnaissance tool designed to automate website discovery and basic exposure assessment.

The scanner performs recursive crawling, identifies potentially sensitive endpoints, evaluates HTTP security headers, analyzes robots.txt directives, and generates structured reports for further review.

This project was developed to strengthen practical cybersecurity, web security, and Python development skills while demonstrating secure reconnaissance methodologies.

---

## Features

### Reconnaissance

* Recursive website crawling
* Internal link discovery
* URL normalization and deduplication
* Configurable crawl depth
* Configurable page limits

### Security Analysis

* Sensitive endpoint detection

  * admin
  * login
  * upload
  * dashboard
  * backup
  * config
  * secret

* HTTP Security Header Assessment

  * Content-Security-Policy
  * Strict-Transport-Security
  * X-Frame-Options
  * X-Content-Type-Options
  * Referrer-Policy
  * Permissions-Policy

* HTML comment detection

* Login form discovery

* Upload form discovery

* JavaScript asset discovery

* Email exposure detection

### Discovery

* robots.txt analysis
* Sitemap discovery
* Internal page enumeration

### Reporting

* JSON report generation
* CSV report generation
* Risk scoring system
* Categorized findings

---

## Project Structure

```text
Web-Recon-Scanner/
│
├── scanner.py
├── crawler.py
├── analyzer.py
├── reporter.py
├── utils.py
│
├── reports/
├── screenshots/
│
├── requirements.txt
└── README.md
```

### Module Responsibilities

| File        | Purpose                                  |
| ----------- | ---------------------------------------- |
| scanner.py  | Main entry point and CLI interface       |
| crawler.py  | Crawling and URL discovery               |
| analyzer.py | Security analysis and finding generation |
| reporter.py | JSON and CSV report creation             |
| utils.py    | Shared helper functions                  |

---

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/Web-Recon-Scanner.git
cd Web-Recon-Scanner
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

Basic scan:

```bash
python scanner.py --url https://python.org
```

Specify crawl depth:

```bash
python scanner.py --url https://python.org --depth 3
```

Specify page limit:

```bash
python scanner.py --url https://python.org --pages 100
```

---

## Example Output

```text
WEB RECON & EXPOSURE SCANNER v1.1

robots.txt Findings:
Disallow: /
Disallow: /webstats/

[1/50] https://python.org
[2/50] https://python.org/jobs
[3/50] https://python.org/community

Pages Analyzed: 50

Reports Generated:
report_20260613.json
report_20260613.csv
```

---

## Risk Scoring

The scanner assigns a risk score based on discovered findings.

| Score | Risk   |
| ----- | ------ |
| 0–3   | LOW    |
| 4–6   | MEDIUM |
| 7+    | HIGH   |

Examples:

* Missing security headers
* Sensitive endpoint references
* Upload forms
* Login portals
* Exposed emails
* HTML comments

---

## Educational Purpose

This project is intended for:

* Security research
* Defensive reconnaissance
* Learning web security concepts
* Cybersecurity portfolio development

Only scan systems that you own or have explicit permission to assess.

---

## Roadmap

### Version 1.2

* HTML dashboard reporting
* Visual risk summaries
* Dashboard metrics

### Version 1.3

* JavaScript asset analysis
* Secret detection
* Endpoint classification

### Version 1.4

* Async crawling
* Performance optimization

### Version 2.0

* Screenshot capture
* Technology fingerprinting
* Interactive visualization

---

## Author

Nilanjan Chowdhury [ https://www.linkedin.com/in/nilanjan-chowdhury-a36787359/ ]

Cybersecurity | Web Security | Python Development
