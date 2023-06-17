from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
    aws_lambda as _lambda
)
from constructs import Construct

class CdkPoetryStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        func = _lambda.Function(self, "test-function", 
                                runtime=_lambda.Runtime.PYTHON_3_10,
                                code=_lambda.Code.from_asset('cdk_poetry/lambdas/hello_world/hello_world'),
                                handler="index.handler"
                       )


        # The code that defines your stack goes here

        # example resource
        # queue = sqs.Queue(
        #     self, "CdkPoetryQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )
