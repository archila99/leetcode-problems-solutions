# LeetCode practice

Personal collection of [LeetCode](https://leetcode.com/)-style problem solutions in **Python 3**. Solutions are grouped by topic or data structure so they are easy to browse and revisit.

## Repository layout

| Folder | Focus |
|--------|--------|
| `Trees/` | Binary trees (depth, symmetry, BST range sum, inversion, subtrees, helpers in `tree_utils.py`) |
| `Hashes/` | Hash maps and sets (anagrams, subsets, grouping) |
| `two-pointers/` | Two-pointer patterns |
| `Sliding/` | Sliding window |
| `Linked-List/` | List manipulation and merges |
| `Binary/` | Binary / bit-related exercises |
| `Heep/` | Heap and priority-queue style problems |
| `Graphs/` | Graph cloning and related |
| `Tries/` | Trie structures |
| `backtracking/` | Permutations, subsets, N-Queens, combination sum |
| `greedy/` | Greedy strategies |

Standalone scripts at the **repository root** cover misc topics (e.g. arrays, strings, stacks): `valid-parenthesis.py`, `merge.py`, `sum-to-target.py`, and others.

## Running locally

Use Python 3. From the repo root:

```bash
python3 path/to/some_solution.py
```

Some files import helpers from the same folder (for example `Trees/invert_binary_tree.py` imports `tree_utils`). Run those from inside that folder, or ensure the folder is on `PYTHONPATH`:

```bash
cd Trees && python3 invert_binary_tree.py
```

## Publishing to GitHub

If this folder is not a Git repository yet:

```bash
cd /path/to/leetcode-practice
git init
git add .
git commit -m "Initial commit: LeetCode practice solutions"
```

Create a new empty repository on GitHub, then connect and push:

```bash
git remote add origin https://github.com/<your-username>/<your-repo-name>.git
git branch -M main
git push -u origin main
```

Optional: add a `.gitignore` so you do not commit editor settings or bytecode, for example:

```
__pycache__/
*.pyc
.vscode/
```

## License

This repository is for personal learning. Problem statements belong to LeetCode and respective rights holders.
