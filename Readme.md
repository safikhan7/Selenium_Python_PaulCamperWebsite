For Execution only:
    behave features\paulCamper.feature

For Execution and allure report:
    behave -f allure_behave.formatter:AllureFormatter -o reports/ features

After execution run this for generating allure report:
    allure serve reports/