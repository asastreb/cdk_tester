#!/usr/bin/env python3

from aws_cdk import core as cdk

# For consistency with TypeScript code, `cdk` is the preferred import name for
# the CDK's core module.  The following line also imports it as `core` for use
# with examples from the CDK Developer's Guide, which are in the process of
# being updated to use `cdk`.  You may delete this import if you don't need it.

from infra.pipeline_stack import PipelinePanionDsInfrastrucureCdkStack

from infra.utils.conf import get_conf

aws_conf = get_conf()

app = cdk.App()

PipelinePanionDsInfrastrucureCdkStack(app,
                                      "PipelinePanionDsInfrastrucureCdkStack",
                                      env=cdk.Environment(account=aws_conf.get("aws_account_id"),
                                                          region=aws_conf.get("aws_region"))
                                      )

app.synth()
