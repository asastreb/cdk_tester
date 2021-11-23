import json
import pathlib
import os


def get_conf():
    conf_path = os.path.join(pathlib.Path.cwd(),"cdk_conf.json")

    assert os.path.isfile(conf_path), f"cdk_conf.json file not found in {conf_path}"

    with open(conf_path, "r") as f:
        aws_env = json.load(f)

    for field in ["github_owner", "github_project", "aws_account_id", "aws_region"]:
        assert field in aws_env, f"{field} is not present in cdk_conf.json file"

    return aws_env
