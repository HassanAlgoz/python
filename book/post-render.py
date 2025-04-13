import os
from pathlib import Path
import re

import parsel

# if not os.getenv("QUARTO_PROJECT_RENDER_ALL"):
#   exit()

# files = os.getenv("QUARTO_PROJECT_OUTPUT_FILES").split('\n')

files = Path('docs').glob('**/*.html')
term_pattern = re.compile(r'\(\s*[a-zA-Z]+\s*\)')

for file in files:
    print(file)
    with open(file, 'r') as f:
        content = f.read()
    doc = parsel.Selector(content)
    terms = []
    for p in doc.css('p::text').getall():
        terms.extend(term_pattern.findall(p))
    for h in [h for i in range(1,7) for h in doc.css(f'h{i}::text').getall()]:
        terms.extend(term_pattern.findall(h))
    print(terms)
    if len(terms) > 50:
        break

# for file in files:
#     print(file)
#     with open(file, 'r') as f:
#         content = f.read()
#     doc = parsel.Selector(content)
#     for term in doc.css('strong').getall():
#         print(term)
#     break
