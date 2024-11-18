pytest -vs --browser chrome --html Reports/Test_run_report_on_chrome.html --self-contained-html
pytest -vs --browser firefox --html Reports/Test_run_report_on_firefox.html --self-contained-html
pytest -vs -k test_login_with_data_driven --browser firefox --html Reports/Test_run_report_on_firefox.html --self-contained-html
