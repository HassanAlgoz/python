from pathlib import Path

import typer

app = typer.Typer()

@app.command()
def hello(name: str):
    print('Hello', name)

@app.command()
def uppercase(file_path: str):
    # قراءة الملف
    p = Path(file_path).resolve()
    with open(file=p, mode='r') as file:
        content = file.read()
    
    # معالجة النص
    content = content.upper()

    # كتابة النتيجة
    p = p.with_stem(f'{p.stem}_processed')
    with open(file=p, mode='w') as file:
        file.write(content)

if __name__ == "__main__":
    app()