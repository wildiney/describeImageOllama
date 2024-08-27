.PHONY: build

PYTHON = python

build:
	@echo "Building"
	pyinstaller --onefile describeimage/describeimage.py