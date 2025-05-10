PROJECT_NAME := ozon-seller
PROJECT_PACKAGE := $(shell echo "$(PROJECT_NAME)" | tr "-" "_")

.PHONY: help lint test install uninstall check-installation

help:
	@echo "Usage:"
	@echo "  make [options] <target>"
	@echo
	@echo "Options: see for the details \"man make\"."
	@echo
	@echo "Targets:"
	@echo "  help                Show this help message."
	@echo "  lint                Run the linter."
	@echo "  test                Run the unit tests."
	@echo "  install             Install the project package."
	@echo "  uninstall           Uninstall the project package."
	@echo "  check-installation  Check the installation of the project package."

lint:
	mypy "$(PROJECT_PACKAGE)"

test:
	python3 -m unittest discover --pattern '*_test.py'

install:
	python3 -m pip install .
	"$(MAKE)" check-installation

uninstall:
	python3 -m pip uninstall --yes "$(PROJECT_NAME)"

check-installation:
	python3 -c "import $(PROJECT_PACKAGE); print($(PROJECT_PACKAGE).__version__)"
