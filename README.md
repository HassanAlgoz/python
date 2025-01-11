# كتاب البايثونية

اضغط على رابط [كتاب البايثونية](https://hassanalgoz.github.io/python/) للتصفح.

**⚠️: لا تزال النسخة تحت الإنشاء.**

## Development (التطوير)

### Install dependencies

Do your self a favor and [install `uv`](https://docs.astral.sh/uv/) which is ⚡️ 10-100x faster than `pip`.

Then run:

```
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