from .helper import nifcloud


class TestESS:
    def test_ess_list_identities(self):
        res = nifcloud("ess list-identities")
        assert len(res["Identities"]) == 0

    def test_ess_get_send_quota(self):
        res = nifcloud("ess get-send-quota")
        assert res["Max24HourSend"] == 2500000.0
        assert res["MaxSendRate"] == 50.0
        assert res["SentLast24Hours"] == 0.0

    def test_ess_get_send_statistics(self):
        res = nifcloud("ess get-send-statistics")
        assert len(res["SendDataPoints"]) == 0
