import json
import os
import pathlib
from subprocess import PIPE, Popen


def nifcloud(cmd, raw_output=False):
    repo_root = pathlib.Path(__file__).parent.parent.parent
    nifcloud_cmd = os.path.join(repo_root, "bin", "nifcloud")
    if not os.path.isfile(nifcloud_cmd):
        raise ValueError('Could not find "nifcloud" executable.')

    full_command = f"python {nifcloud_cmd} {cmd}"
    env = os.environ.copy()
    process = Popen(
        full_command, stdout=PIPE, stderr=PIPE, stdin=PIPE, shell=True, env=env
    )

    stdout, stderr = process.communicate()
    if process.returncode != 0:
        raise ValueError(
            f"return code is not 0 ({process.returncode}). stdout: {stdout.decode()}  stderr: {stderr.decode()}"
        )

    if raw_output:
        return stdout.decode()

    return json.loads(stdout.decode())
