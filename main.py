#!/usr/bin/env python
from constructs import Construct
from cdktf import App, TerraformOutput, TerraformStack
from cdktf_cdktf_provider_aws.provider import AwsProvider
from cdktf_cdktf_provider_aws.s3_bucket import S3Bucket


# Define your stack
class MyStack(TerraformStack):
    def __init__(self, scope: Construct, ns: str):
        super().__init__(scope, ns)

        # Configure the AWS provider to use the eu-west-3 region
        AwsProvider(
            self,
            "AWS",
            region="eu-west-3"
        )

        # Create your first bucket
        # pass the id of the resource and the name of the bucket
        # The code also configures the instance with named arguments, using camel case for properties that correspond to the AWS provider documentation.
        first_bucket = S3Bucket(
            self, "first_bucket",
            bucket="blog.abdelfare.me",
            acl="public-read"
        )

        TerraformOutput(self, "bucket_name", value=first_bucket.bucket)
        TerraformOutput(self, "bucket_arn", value=first_bucket.arn)


app = App()
MyStack(app, "s3-demo")

# Finally, the example code creates your application using the stack you have defined, configures a remote backend to store your project's state in Terraform Cloud, and runs app.synth() to generate Terraform configuration.
app.synth()
