from .helper import nifcloud


class TestDevOps:
    def test_devops_list_instances(self):
        res = nifcloud("--region jp-west-1 devops list-instances")
        assert len(res["Instances"]) == 0
