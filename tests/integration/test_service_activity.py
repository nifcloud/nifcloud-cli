from .helper import nifcloud


class TestServiceActivity:
    def test_service_activity_describe_service_statuses(self):
        res = nifcloud("service-activity describe-service-statuses")
        assert len(res["Data"]["ServiceMenu"]) != 0
