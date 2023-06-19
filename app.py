#!/usr/bin/env python3

import aws_cdk as cdk

from cdk_allure.cdk_allure_stack import CdkAllureStack


app = cdk.App()
CdkAllureStack(app, "cdk-allure")

app.synth()
