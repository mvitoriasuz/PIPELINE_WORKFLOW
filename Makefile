.PHONY: all test clean
all: test
test:
 python -m pytest tests/
clean:
 rm -rf __pycache__ dist build *.spec