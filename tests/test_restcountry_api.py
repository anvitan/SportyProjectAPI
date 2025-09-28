import pytest
import requests
import yaml
import logging
from pytest_html import extras

BASE = "https://restcountries.com/v3.1"

# Setup logger
logger = logging.getLogger("api_test_logger")
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
ch.setFormatter(formatter)
logger.addHandler(ch)

def log_request_response(response):
    req = response.request
    logger.info(f"Request: {req.method} {req.url}")
    logger.info(f"Request headers: {req.headers}")
    if req.body:
        logger.info(f"Request body: {req.body}")
    logger.info(f"Response status: {response.status_code}")
    try:
        json_data = response.json()
        keys = list(json_data[0].keys()) if isinstance(json_data, list) else list(json_data.keys())
        logger.info(f"Response json keys: {keys}")
    except Exception:
        logger.info(f"Response content: {response.text[:200]}")

# Load YAML test data once
with open("test_data.yaml", "r") as f:
    test_data = yaml.safe_load(f)

@pytest.mark.parametrize(
    "name_query, full_text, expected_code, expected_min_count, expected_contains",
    [(d["name_query"], d["full_text"], d["expected_code"], d["expected_min_count"], d["expected_contains"])
     for d in test_data["search_countries_by_name"]],
    ids=[f"search_{d['name_query']}_ft_{d['full_text']}" for d in test_data["search_countries_by_name"]]
)
def test_search_countries_by_name(name_query, full_text, expected_code, expected_min_count, expected_contains, request):
    url = f"{BASE}/name/{name_query}"
    params = {"fullText": "true"} if full_text else {}
    response = requests.get(url, params=params)

    log_request_response(response)

    # Attach logs to pytest-html report
    if hasattr(request.node, "add_extra"):
        request.node.add_extra(extras.text(f"Request URL: {response.request.url}", name="Request URL"))
        request.node.add_extra(extras.text(f"Request headers: {response.request.headers}", name="Request Headers"))
        request.node.add_extra(extras.text(f"Status Code: {response.status_code}", name="Status Code"))
        try:
            pretty_json = response.json()
            request.node.add_extra(extras.text(str(pretty_json)[:1000], name="Response JSON"))
        except Exception:
            request.node.add_extra(extras.text(response.text[:1000], name="Response Text"))

    assert response.status_code == expected_code

    if expected_code == 200:
        data = response.json()
        assert isinstance(data, list)
        assert len(data) >= expected_min_count
        if expected_contains:
            country_names = [country["name"]["common"] for country in data]
            assert any(expected_contains in name for name in country_names)
