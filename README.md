# learn-python

中文文档见 [README.zh.md](README.zh.md)。

Python practice problems with tests.

## Setup

```bash
uv sync
```

## How it works

Each problem lives in `problems/` with a function to complete. Tests live in
`tests/`. Fill in the function, then run the tests to check your work.

## Run the tests

```bash
uv run pytest              # run all tests
uv run pytest -k largest   # run one problem's tests
```

## Problems

- `problems/largest_number.py` — find the largest number in a list
- `problems/count_even_numbers.py` — count how many even numbers are in a list
