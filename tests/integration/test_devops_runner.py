from .helper import nifcloud


class TestDevOpsRunner:
    def test_devops_list_runners(self):
        res = nifcloud("devops-runner list-runners")
        assert len(res["Runners"]) == 0
