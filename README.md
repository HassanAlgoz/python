# كتاب البايثونية

**⚠️: لا يزال الكتاب في طوْر المسودة**

[اضغط هنا لتصفح الكتاب](https://hassanalgoz.github.io/python/)

## Development

### Install dependencies

Do your self a favor and [install `uv`](https://docs.astral.sh/uv/) which is ⚡️ 10-100x faster than `pip`.

Then run:

```bash
uv sync
```

This will install the dependencies in the `pyproject.toml` file. Vwalah! 

Everything is installed in `.venv/`.

Finally, point VS Code Language Server (bottom-right) and Notebook Kernel (top-right) to the Python Interpreter in `.venv/`.

Make sure you activate it:

```bash
source .venv/bin/activate
```

Preview the book:

```bash
quarto preview book
```