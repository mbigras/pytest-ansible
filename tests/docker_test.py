import subprocess
import time
from pytest import fixture
import requests

PORT = 3000

@fixture(scope="module")
def container():
    run_cmd(["docker", "build", "-t", "app:latest", "app"])
    run_cmd(
        [
            "docker",
            "run",
            "--rm",
            "-itd",
            "--name",
            "testapp",
            "-e",
            f"PORT={PORT}",
            "-p",
            f"{PORT}:{PORT}",
            "app:latest",
        ]
    )

    yield

    run_cmd(["docker", "rm", "-f", "testapp"])


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


def test_docker(container):
    run_cmd(
        [
            "docker",
            "exec",
            "testapp",
            "echo",
            "hello",
        ]
    )


def test_app(container):
    r = requests.get(f"http://localhost:{PORT}/")

    assert r.status_code == 200
    assert r.text == "up\n"
