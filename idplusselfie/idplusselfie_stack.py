from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
    aws_iam as iam,
    aws_apigateway as apigateway
)
from constructs import Construct


class idplusselfieStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Define the lambda resource
        ips_lambda = _lambda.Function(self, "ipsHandler",
                                      code=_lambda.Code.from_asset('lambda'),
                                      handler="ips-lambda.lambda_handler",
                                      runtime=_lambda.Runtime.PYTHON_3_9,
                                      )

        # Create an IAM policy statement for the function to request rekognition
        ips_lambda.add_to_role_policy(iam.PolicyStatement(
            effect=iam.Effect.ALLOW,
            actions=[
                'rekognition:*',
            ],
            resources=[
                '*'
            ],
        ))

        # Define API Gateway
        api = apigateway.LambdaRestApi(self, "ipsApi",
                                       handler=ips_lambda,
                                       proxy=False)

        # Define resource
        items = api.root.add_resource("ips")
        items.add_method("POST") # POST /spi


