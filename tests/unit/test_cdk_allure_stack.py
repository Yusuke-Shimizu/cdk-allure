import aws_cdk as core
import aws_cdk.assertions as assertions
from cdk_allure.cdk_allure_stack import CdkAllureStack


def test_sqs_queue_created():
    """
    Stack:
        CdkAllureStack
    Item:
        SQSの可視性タイムアウトの確認
    Expect:
        300秒であること
    """
    app = core.App()
    stack = CdkAllureStack(app, "cdk-allure")
    template = assertions.Template.from_stack(stack)

    template.has_resource_properties("AWS::SQS::Queue", {
        "VisibilityTimeout": 300
    })


def test_sns_topic_created():
    """
    Stack:
        CdkAllureStack
    Item:
        SNSトピック数の確認
    Expect:
        1個だけ存在すること
    """
    app = core.App()
    stack = CdkAllureStack(app, "cdk-allure")
    template = assertions.Template.from_stack(stack)

    template.resource_count_is("AWS::SNS::Topic", 1)
