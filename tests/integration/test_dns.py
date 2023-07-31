from .helper import nifcloud


class TestDNS:
    def test_dns_list_hosted_zones(self):
        res = nifcloud("dns list-hosted-zones")
        assert len(res["HostedZones"]) == 1
