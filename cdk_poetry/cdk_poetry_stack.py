from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
    aws_lambda as _lambda,
    aws_ecr_assets as ecr_assets,
)
from constructs import Construct


class CdkPoetryStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        func = _lambda.Function(
            self,
            "test-function",
            runtime=_lambda.Runtime.PYTHON_3_10,
            function_name="test-function",
            code=_lambda.Code.from_asset("cdk_poetry/lambdas/hello_world/hello_world"),
            handler="index.handler",
        )
        self.add_lambda("hello_world")
        self.add_lambda("another_lambda")

    def add_lambda(self, lambda_name: str):
        id = f"test-docker-function-{lambda_name}"
        func2 = _lambda.DockerImageFunction(
            self,
            id,
            function_name=id,
            code=_lambda.DockerImageCode.from_image_asset(
                directory="./cdk_poetry/lambdas/",
                file=f"hello_world/Dockerfile",
                platform=ecr_assets.Platform.LINUX_AMD64,
                build_args={"--target": lambda_name},
            ),
        )

        # The code that defines your stack goes here

        # example resource
        # queue = sqs.Queue(
        #     self, "CdkPoetryQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )
