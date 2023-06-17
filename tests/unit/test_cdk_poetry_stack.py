import aws_cdk as core
import aws_cdk.assertions as assertions

from cdk_poetry.cdk_poetry_stack import CdkPoetryStack

# example tests. To run these tests, uncomment this file along with the example
# resource in cdk_poetry/cdk_poetry_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CdkPoetryStack(app, "cdk-poetry")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
def test_123():
    assert 1 == 1
