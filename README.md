# Python Data Structures and Algorithms ![](https://github.com/ahcode0919/python-ds-algorithms/actions/workflows/Python.yml/badge.svg?branch=main) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Various Data Structures and Algorithm Solutions in Python (3.x). Succinct Python one-liners are avoided in most solutions
to prevent obscuring the function and logic of the algorithms / data-structures.  

* [Algorithm Theory](algorithm_theory/README.md)
  * [Searches](algorithm_theory/README.md#searches)
    * [Binary Search](algorithm_theory/README.md#binary-search)
    * [Jump Search](algorithm_theory/README.md#jump-search)
    * [Linear Search](algorithm_theory/README.md#linear-search)
  * [Sorts](algorithm_theory/README.md#sorts)
    * [Bubble Sort](algorithm_theory/README.md#bubble-sort)
* [Data Structures](data_structures/README.md)
  * [Binary Tree](data_structures/README.md#binary-tree)
  * [Circularly Linked List](data_structures/README.md#circularly-linked-list)
  * [Doubly Linked List](data_structures/README.md#doubly-linked-list)
  * [Singly Linked List](data_structures/README.md#singly-linked-list)
  * [Queue](data_structures/README.md#queue)
  * [Stack](data_structures/README.md#stack)
  * [Trie](data_structures/README.md#trie)

## Algorithms

* [Arrays](arrays/README.md)
* [Binary Search](binary_search/README.md)
* [Binary Tree](binary_tree/README.md)
* [Circularly Linked Lists](circularly_linked_list/README.md)
* [Doubly Linked Lists](doubly_linked_list/README.md)
* [Integers](integers/README.md)
* [Matrices](multi_dimensional_arrays/README.md)
* [N-ary Tree](n_ary_tree/README.md)
* [Queues](queues/README.md)
* [Singly Linked Lists](singly_linked_lists/README.md)
* [Stacks](stacks/README.md)
* [Strings](strings/README.md)
* [Trie](trie/README.md)

## Project Setup

### Local development

- Install `pyenv`
- Install current Python version: `pyenv install 3.10`
- Set global Python version: `pyenv global 3.10`
- Initialize virtual environment: `python -m venv .venv`
- Activate: source `.venv/bin/activate`
- Install packages: `pip3 -r requirements.txt`

### VS Code Dev Container

- Download VSCode and Docker
- Launch project inside of Docker container in VSCode
- VSCode does the rest!

## Project Commands

* Lint project - `flake8`
* Run Unit Tests - `pytest`
