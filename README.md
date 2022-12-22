# nifcloud-cli

[![Test](https://github.com/nifcloud/nifcloud-cli/workflows/Test/badge.svg)](https://github.com/nifcloud/nifcloud-cli/actions?query=workflow%3ATest)
[![PyPI](https://badge.fury.io/py/nifcloud-cli.svg)](https://pypi.org/project/nifcloud-cli)

Universal Command Line Interface for NIFCLOUD Services 

## Requirements

* Python 3.7 or later

## How to Install

### Using pip

```
$ pip install nifcloud-cli
$ nifcloud --version
```

### Using MSI installer (Windows only)

1. Download the MSI installer from [Release](https://github.com/nifcloud/nifcloud-cli/releases).
1. Run the downloaded MSI installer.
1. Check the nifcloud-cli from command prompt.
    ```
    C:\> nifcloud --version
    ```

### Using docker

```
$ docker run -it --rm ghcr.io/nifcloud/nifcloud-cli --version
```

## Usage

### Set credentials

You can configure credentials via environment variables or `nifcloud configure` command.

#### via environment variable

- Linux

```
$ export NIFCLOUD_ACCESS_KEY_ID=<Your NIFCLOUD Access Key ID>
$ export NIFCLOUD_SECRET_ACCESS_KEY=<Your NIFCLOUD Secret Access Key>
$ export NIFCLOUD_DEFAULT_REGION=jp-east-1
```

- Windows

```
C:\> set NIFCLOUD_ACCESS_KEY_ID=<Your NIFCLOUD Access Key ID>
C:\> set NIFCLOUD_SECRET_ACCESS_KEY=<Your NIFCLOUD Secret Access Key>
C:\> set NIFCLOUD_DEFAULT_REGION=jp-east-1
```

#### via `nifcloud configure` command

```
$ nifcloud configure
NIFCLOUD Access Key ID [None]: <Your NIFCLOUD Access Key ID>
NIFCLOUD Secret Access Key [None]: <Your NIFCLOUD Secret Access Key>
Default region name [jp-east-1]: jp-east-1
Default output format [None]:
```

config file is saved under the `.nifcloud` directory in your home directory (`$HOME` or `%UserProfile%`)

### Show available services

```
$ nifcloud help
```

### Show available actions for the service

```
$ nifcloud computing help
```

### Show available parameters for the action

```
$ nifcloud computing create-key-pair help
```

### Run the command actually

```
$ nifcloud computing create-key-pair --key-name foobar123 --password foobar123 
```

## License

See [LICENSE](LICENSE).
