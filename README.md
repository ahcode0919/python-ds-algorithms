# Python Data Structures and Algorithms ![](https://github.com/ahcode0919/python-ds-algorithms/actions/workflows/Python.yml/badge.svg?branch=main) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Various Data Structures and Algorithm Solutions in Python (3.x). Succinct Python one-liners are avoided in most solutions
to prevent obscuring the function and logic of the algorithms / data-structures.

* [Algorithm Theory](src/algorithm_theory/)
* [Data Structures](src/data_structures/)

## Algorithms

* [Arrays](src/arrays/)
* [Binary Search](src/binary_search/)
* [Binary Tree](src/binary_tree/)
* [Circularly Linked Lists](src/circularly_linked_list/)
* [Doubly Linked Lists](src/doubly_linked_list/)
* [Integers](src/integers/)
* [Math Problems](src/math_problems/)
* [Matrices](src/multi_dimensional_arrays/)
* [N-ary Tree](src/n_ary_tree/)
* [Queues](src/queues/)
* [Singly Linked Lists](src/singly_linked_lists/)
* [Stacks](src/stacks/)
* [Strings](src/strings/)
* [Trie](src/trie/)

Each directory's problems and approaches are documented as doc comments directly in the corresponding `.py` files.

## Project Setup

### Local Development Installation

Note: Project uses `uv` and `just` to manage project configuration and commands

* Install dependencies via Homebrew - `brew bundle install`
* Sync project - `just sync`

### VS Code Dev Container

* Download VSCode and Docker
* Launch project inside of Docker container in VSCode
* VSCode does the rest!

## Project Commands

* Lint project - `just lint`
* Sync uv environment - `just sync`
* Run Unit Tests - `just test`
* Install dependency: `uv add {package}`
