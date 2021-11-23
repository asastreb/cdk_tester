from aws_cdk import (
    core as cdk,
    # aws_sqs as sqs,
)

from aws_cdk.pipelines import CodePipeline, CodePipelineSource, ShellStep
from infra.s3buckets_stage import S3BubcketsStage
from infra.utils.conf import get_conf


class PipelinePanionDsInfrastrucureCdkStack(cdk.Stack):
    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        aws_conf = get_conf()

        github = CodePipelineSource.git_hub(
            f"{aws_conf.get('github_owner')}/{aws_conf.get('github_project')}", "master"
        )

        synth_step = ShellStep(
            "Synth",
            input=github,
            commands=[
                "npm install -g aws-cdk",
                "python -m pip install -r requirements.txt",
                "cdk synth",
            ],
        )

        pipeline = CodePipeline(
            self,
            "Pipeline",
            pipeline_name="PanionDsInfrastructureCdkPipeline",
            synth=synth_step,
        )

        s3buckets_stage = S3BubcketsStage(
            self, "S3Buckets"
        )
        stage = pipeline.add_stage(s3buckets_stage)
