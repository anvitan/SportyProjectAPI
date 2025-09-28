# REST Countries API Automated Test Suite

## Overview

Automated tests for the [REST Countries API](https://restcountries.com), using Python and pytest.  
Tests are data-driven from YAML files with rich logging and comprehensive HTML reporting.

## Project Structure
.
├── test_rest_countries.py
├── test_data.yaml
├── conftest.py
├── requirements.txt
├── report.html
└── README.md
---
## Test Cases Summary

| Test Name                 | Description                                  | Validation Used                                     | Reason                                        |
|---------------------------|----------------------------------------------|----------------------------------------------------|-----------------------------------------------|
| `test_search_countries_by_name` | Verify searching countries by name           | HTTP status codes, response list size, content field| To ensure API search returns correct countries|
| `test_get_countries_by_region`  | Verify fetching countries by region          | HTTP status, minimum number of countries returned   | Region-based filtering validation              |
| `test_get_country_by_code`      | Verify lookup of countries by ISO code      | HTTP status, exact country name                      | Validates country code correctness             |

---

## Validation Approach

- **Status Code Checks:** Confirms API properly returns 200 for success or 404 for invalid queries.
- **Schema and Content Validation:** Ensures response contains expected fields (e.g., `name.common`) and values matching input.
- **List Size Checks:** Validates the presence of an appropriate number of results from list endpoints.
- **Data-driven Testing:** Uses external YAML to flexibly add test cases without modifying code.
- **Logging:** Detailed API request/response logging aids debugging.
- **HTML Reporting:** Embeds logs and execution summaries for easy result analysis.

---
git clone [<your-ui-repo-url>](https://github.com/anvitan/SportyUIAutomation.git)
cd home-test-ui

2. Create virtual environment
python3 -m venv .venv
source .venv/bin/activate   # macOS/Linux
.venv\Scripts\activate  

3. Install dependencies
pip install -r requirements.txt


Run tests and generate `report.html`:

▶️ Running Tests
pytest --html=report.html --self-contained-html


Open the report in a web browser to inspect detailed test outcomes and logs.

---

## Extending Tests

- Add new scenarios in `test_data.yaml`.
- Write or extend test functions referencing YAML data.
- Logging and reporting features are auto-managed.
