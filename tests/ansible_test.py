import subprocess
import time
from pytest import fixture


@fixture(scope="module")
def vm():
    """
    Start a vagrant machine at the beginning of test module.
    Then yield to all the tests
    Tear down the vagrant machine at the end of the test module
    """
    run_cmd(["vagrant", "up"])
    time.sleep(10)

    yield

    run_cmd(["vagrant", "destroy", "-f"])


def run_cmd(cmd):
    """
    Run command and raise subprocess.CalledProcessError exception if command fails.
    
    The benefit of raises an exception is pytest will fail the test.
    If a test function doesn't raise an exception then it's marked as a success.
    This avoids needing to call assert result.returncode == 0 after every test.
    """
    print("\nRunning the following command:")
    print(" ".join(cmd))
    subprocess.run(cmd, check=True)


def test_vagrant_ssh_connection(vm):
    run_cmd(
        [
            "vagrant",
            "ssh",
            "default",
            "-c",
            "echo hello world",
        ]
    )


def test_ssh_connection(vm):
    run_cmd(
        [
            "ssh",
            "-i",
            "~/.vagrant.d/insecure_private_key",
            "-o",
            "StrictHostKeyChecking=no",
            "-o",
            "UserKnownHostsFile=/dev/null",
            "vagrant@192.168.33.10",
            "echo",
            "hello",
            "world",
        ]
    )


def test_ansible_adhoc(vm):
    run_cmd(["ansible", "all", "-m", "ping"])


def test_ansible_playbook(vm):
    run_cmd(["ansible-playbook", "ping.yml"])
