.PHONY: help test

help:
	@echo "Usage:"
	@echo "  make [options] <target>"
	@echo
	@echo "Options: see for the details \"man make\"."
	@echo
	@echo "Targets:"
	@echo "  help  Show this help message."
	@echo "  test  Run the unit tests."

test:
	python3 -m unittest discover --pattern '*_test.py'
