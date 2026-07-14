# learn-python

Python 练习题与测试。

## 环境配置

```bash
uv sync
```

## 工作方式

每道题都在 `problems/` 目录下，包含一个需要你补全的函数。测试在 `tests/`
目录下。补全函数后，运行测试来检查你的答案。

## 运行测试

```bash
uv run pytest              # 运行所有测试
uv run pytest -k largest   # 只运行某一道题的测试
```

## 题目

- `problems/largest_number.py` — 找出列表中的最大数
- `problems/count_even_numbers.py` — 统计列表中偶数的个数
