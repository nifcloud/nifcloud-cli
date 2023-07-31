from .helper import nifcloud


class TestCLI:
    def test_cli_help(self):
        res = nifcloud("help", raw_output=True)
        available_services = [
            "computing",
            "rdb",
            "nas",
            "dns",
            "ess",
            "script",
            "storage",
            "service-activity",
        ]
        for service in available_services:
            assert service in res
