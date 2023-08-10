from .helper import nifcloud


class TestRDB:
    def test_rdb_describe_db_instances(self):
        res = nifcloud("rdb describe-db-instances")
        assert len(res["DBInstances"]) == 0

    def test_rdb_describe_db_engine_versions(self):
        res = nifcloud(
            "rdb describe-db-engine-versions --engine=mysql --engine-version=5.7.15"
        )
        db_engine_versions = res["DBEngineVersions"]
        assert len(db_engine_versions) == 1
        db_engine_version = db_engine_versions[0]
        assert db_engine_version["DBEngineDescription"] == "MySQL Community Edition"
        assert db_engine_version["DBEngineVersionDescription"] == "MySQL 5.7.15"
        assert db_engine_version["DBParameterGroupFamily"] == "mysql5.7"
        assert db_engine_version["Engine"] == "mysql"
        assert db_engine_version["EngineVersion"] == "5.7.15"
