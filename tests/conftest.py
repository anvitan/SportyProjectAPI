def pytest_html_report_title(report):
    report.title = "REST Countries API Test Report"

def pytest_html_results_summary(prefix, summary, postfix):
    prefix.extend([
        "Project Name: REST Countries API Testing",
        "Tester: Your Name",
    ])

