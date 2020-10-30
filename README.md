# pytest-ansible

> This repository illustrates testing infrastructure.

## Overview

This repository is inspired by [terratest](https://github.com/gruntwork-io/terratest).
The idea is that you create infrastructure, test the infrastructure, and tear it down.
Terratest tends to use golang and terraform. This repository illustrates the same idea with python, vagrant, and ansible.

This is what happens when you type `make test`:

- A vagrant machine is launched
- Commands and playbooks are tested
- The vagrant machine is torn down

## Quickstart

```
make setup
make test
```
