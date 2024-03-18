import pytest

from nifcloudcli.link import get_document_site_url


class TestLink:
    DOC_DOMAIN = "pfs.nifcloud.com"

    @pytest.mark.parametrize(
        "service_id,operation",
        [
            ("rdb", "DescribeDBInstances"),
            ("nas", "DescribeNASInstances"),
            ("ess", "ListIdentities"),
            ("dns", "ListHostedZones"),
            ("service-activity", "DescribeServiceStatuses"),
        ],
    )
    def test_get_document_site_url(self, service_id, operation):
        actual = get_document_site_url(service_id, operation)
        expected = f"https://{self.DOC_DOMAIN}/api/{service_id}/{operation}.htm"
        assert actual == expected

    @pytest.mark.parametrize(
        "operation",
        [
            "DescribeInstances",
            "RunInstances",
            "TerminateInstances",
        ],
    )
    def test_get_document_site_url_computing(self, operation):
        actual = get_document_site_url("computing", operation)
        expected = f"https://{self.DOC_DOMAIN}/api/rest/{operation}.htm"
        assert actual == expected

    @pytest.mark.parametrize(
        "operation",
        [
            "GetObject",
            "PutObject",
            "DeleteObject",
        ],
    )
    def test_get_document_site_url_storage(self, operation):
        actual = get_document_site_url("storage", operation)
        expected = (
            f"https://{self.DOC_DOMAIN}/api/object-storage-service/{operation}.htm"
        )
        assert actual == expected
