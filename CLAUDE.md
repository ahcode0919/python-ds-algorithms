# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

This project uses `uv` for dependency management and `just` as the command runner.

```bash
just sync                      # install/sync dependencies (uv sync --all-groups)
just lint                      # uv run ruff check . --fix && uv run ruff format .
just test                      # uv run pytest
uv run pytest tests/algorithm_theory/test_binary_search.py        # run one test file
uv run pytest tests/algorithm_theory/test_binary_search.py::test_binary_search_iterative  # run one test
uv add {package}                # add a dependency
```

There is no separate build step; this is a pure Python (3.14+) library of algorithms with no runtime dependencies.

## Architecture

The repo is organized by topic into top-level directories, each containing implementation modules directly at the
top level (no `src/` layout). `pyproject.toml` sets `pythonpath = ["."]`, so both implementation and test code
import via the top-level package name, e.g. `from algorithm_theory.binary_search import binary_search_iterative`.

Three categories of top-level directories, per the root `README.md`:

- **`algorithm_theory/`** — canonical/fundamental algorithm approaches (e.g. binary/jump/linear search, bubble
  sort).
- **`data_structures/`** — custom implementations of core data structures (binary tree, linked lists, queue,
  stack, trie) that other topic directories' problems build on top of.
- **Topic/problem directories** (`arrays/`, `binary_search/`, `binary_tree/`, `circularly_linked_list/`,
  `doubly_linked_list/`, `integers/`, `math_problems/`, `multi_dimensional_arrays/`, `n_ary_tree/`, `queues/`,
  `singly_linked_lists/`, `stacks/`, `strings/`, `trie/`)

The problem description, constraints, and examples live as a
**doc comment directly on the function/class that solves it** (see any existing file, e.g.
`arrays/two_sum.py`, as the template when adding a new problem). Only when a file genuinely has multiple
top-level functions/classes for one problem (e.g. a brute-force and an optimized approach, like
`stacks/daily_temperatures.py`) does it use a module-level docstring for the shared problem statement plus a
short docstring per function for the approach-specific detail — a single-function file should never have both a module docstring and a redundant function docstring.

Tests live under `tests/<same-directory-name>/test_<module>.py`, mirroring the source layout 1:1 (e.g.
`algorithm_theory/binary_search.py` → `tests/algorithm_theory/test_binary_search.py`). `test_helpers/test_helpers.py`
holds shared builders/fixtures (e.g. `get_binary_search_tree`, `get_singly_linked_list`) used across multiple test
directories for constructing trees and linked lists — check there before writing new setup code for tree/list-based
tests.

Node/structure classes used across multiple directories (e.g. `binary_tree.tree_node.TreeNode`,
`data_structures.singly_linked_list_node.SinglyLinkedListNode`, `n_ary_tree.nary_tree_node.NaryTreeNode`) are
imported directly from their defining module rather than redefined per problem.

## Style

Ruff is configured in `pyproject.toml` (line length 100, target `py314`, rule sets `E, F, W, I, N, D`). Docstring
presence itself is not enforced (`D100-D107` ignored), but when docstrings are present their formatting is linted.
`tests/*` is exempt from docstring rules entirely. Solutions favor explicit, readable Python over terse one-liners
(stated explicitly in the root `README.md`).
