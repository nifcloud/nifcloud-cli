# nifcloud-cli

[![Test](https://github.com/nifcloud/nifcloud-cli/workflows/Test/badge.svg)](https://github.com/nifcloud/nifcloud-cli/actions?query=workflow%3ATest)
[![PyPI](https://badge.fury.io/py/nifcloud-cli.svg)](https://pypi.org/project/nifcloud-cli)

Universal Command Line Interface for NIFCLOUD Services 

## Requirements

* Python 3.7 or later

## How to Install

```
pip install nifcloud-cli
```

## Usage

```
## Set credentials and default region
$ export NIFCLOUD_ACCESS_KEY_ID=<Your NIFCLOUD Access Key ID>
$ export NIFCLOUD_SECRET_ACCESS_KEY=<Your NIFCLOUD Secret Access Key>
$ export NIFCLOUD_DEFAULT_REGION=jp-east-1

## Show available services
$ nifcloud help

## Show available actions for the service
$ nifcloud computing help

## Show available parameters for the action
$ nifcloud computing create-key-pair help

## Run the command actually
$ nifcloud computing create-key-pair --key-name foobar123 --password foobar123 
```

## License

See [LICENSE](LICENSE).
