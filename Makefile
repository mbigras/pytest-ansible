all: help

help:
	@echo "Welcome! This repository illustrates testing infrastructure."
	@echo ""
	@echo "This is what happens when you type 'make test'"
	@echo ""
	@echo "- A vagrant machine is launched"
	@echo "- Commands and playbooks are tested"
	@echo "- The vagrant machine is torn down"
	@echo ""
	@echo "The following are common commands:"
	@echo ""
	@echo "make help"
	@echo "make setup"
	@echo "make test"

setup:
	python3 -m venv venv
	venv/bin/pip install -r requirements.txt

test:
	venv/bin/pytest -sv
