from .helper import nifcloud


class TestNAS:
    def test_nas_describe_nas_instances(self):
        res = nifcloud("nas describe-nas-instances")
        assert len(res["NASInstances"]) == 0
