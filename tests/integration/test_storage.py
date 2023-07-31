import os

from .helper import nifcloud


class TestStorage:
    def setup_method(self, method):
        self.org_nifcloud_access_key_id = os.environ["NIFCLOUD_ACCESS_KEY_ID"]
        self.org_nifcloud_secret_access_key = os.environ["NIFCLOUD_SECRET_ACCESS_KEY"]
        os.environ["NIFCLOUD_ACCESS_KEY_ID"] = os.environ[
            "NIFCLOUD_STORAGE_ACCESS_KEY_ID"
        ]
        os.environ["NIFCLOUD_SECRET_ACCESS_KEY"] = os.environ[
            "NIFCLOUD_STORAGE_SECRET_ACCESS_KEY"
        ]

    def teardown_method(self, method):
        os.environ["NIFCLOUD_ACCESS_KEY_ID"] = self.org_nifcloud_access_key_id
        os.environ["NIFCLOUD_SECRET_ACCESS_KEY"] = self.org_nifcloud_secret_access_key

    def test_storage_get_service(self):
        res = nifcloud("storage get-service")
        assert len(res["Buckets"]) == 0
