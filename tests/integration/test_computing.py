from .helper import nifcloud


class TestComputing:
    def test_computing_describe_instances(self):
        res = nifcloud("computing describe-instances")
        assert len(res["ReservationSet"]) == 0

    def test_computing_describe_regions(self):
        res = nifcloud("computing describe-regions")
        expected_regions = [
            {
                "RegionName": "east-1",
                "RegionEndpoint": "jp-east-1.computing.api.nifcloud.com",
            },
            {
                "RegionName": "east-2",
                "RegionEndpoint": "jp-east-2.computing.api.nifcloud.com",
            },
            {
                "RegionName": "east-3",
                "RegionEndpoint": "jp-east-3.computing.api.nifcloud.com",
            },
            {
                "RegionName": "jp-east-4",
                "RegionEndpoint": "jp-east-4.computing.api.nifcloud.com",
            },
            {
                "RegionName": "west-1",
                "RegionEndpoint": "jp-west-1.computing.api.nifcloud.com",
            },
            {
                "RegionName": "jp-west-2",
                "RegionEndpoint": "jp-west-2.computing.api.nifcloud.com",
            },
            {
                "RegionName": "us-east-1",
                "RegionEndpoint": "us-east-1.computing.api.nifcloud.com",
            },
        ]
        for actual, expected in zip(res["RegionInfo"], expected_regions):
            assert actual["RegionName"] == expected["RegionName"]
            assert actual["RegionEndpoint"] == expected["RegionEndpoint"]
