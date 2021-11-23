from typing import Dict

from aws_cdk import (
    core as cdk,
    aws_s3 as s3
)

from infra.utils.conf import get_conf


class S3BucketsStack(cdk.Stack):
    def __init__(
            self, scope: cdk.Construct, construct_id: str, **kwargs
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)
        conf = get_conf()
        if "s3buckets" in conf:
            bucket_confs = conf.get("s3buckets")
            for bucket_conf in bucket_confs:
                bucket_name = bucket_conf["bucket_name"]
                if "envs" in bucket_conf:
                    for name, params in bucket_conf["envs"].items():
                        env_bucket_name = f"{name}-{bucket_name}"
                        source_bucket = s3.Bucket(self, env_bucket_name, bucket_name=env_bucket_name,
                                                  versioned=params.get("versioned", False)
                                                  )
                        if "expiration_time_hours" in bucket_conf:
                            source_bucket.add_lifecycle_rule(
                                s3.LifecycleRule(enabled=True,
                                                 id=f"{env_bucket_name}_lifecycle",
                                                 expiration=cdk.Duration.hours(params["expiration_time_hours"]))
                            )



