from .helper import nifcloud


class TestDevOps:
    def test_devops_list_instances(self):
        res = nifcloud("devops list-instances")
        assert len(res["Instances"]) == 0
