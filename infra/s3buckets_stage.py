from aws_cdk import core as cdk

from infra.s3bucktes_stack import S3BucketsStack
from infra.utils.conf import get_conf
import pathlib


aws_conf = get_conf()


class S3BubcketsStage(cdk.Stage):
    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        s3_buckets_stack = S3BucketsStack(
            self,
            "S3Buckets",
            env=cdk.Environment(
                account=aws_conf.get("aws_account_id"),
                region=aws_conf.get("aws_region"),
            ),
        )
