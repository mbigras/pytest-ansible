# pytest-infrastructure

> Illustrates testing infrastructure.

## Overview

Inspired by [terratest](https://github.com/gruntwork-io/terratest).
You create infrastructure, test the infrastructure, and tear it down.
Terratest uses golang and terraform. This repository illustrates the same idea with python, vagrant, and ansible. Also there is a docker test.

This is what happens when you type `make test`:

- A vagrant machine is launched
- Tests are performed by running commands.
- The vagrant machine is torn down
- A docker image is built
- A docker container is created and started
- Tests are performed by running commands and issuing requests
- The docker container is removed

## Quickstart

```
make setup
make test
```

## Pytest interesting points

* A test passes if the command succeeds and fails if the command fails.
* A [fixture](https://docs.pytest.org/en/stable/fixture.html#scope-sharing-fixtures-across-classes-modules-packages-or-session) is used to create a vagrant machine at the start of the test session and tear it down at the end.
* If a command fails then an exception is raised. This is the mechanism for marking a test as a failure. The raised exception tells pytest the test failed. If no exception is raised then pytest marks the test as passing. This avoids adding `assert result.returncode == 0` after every test.
