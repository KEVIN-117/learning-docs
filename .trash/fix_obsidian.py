import re
import os

docs_path = "docs"  # Cambia esto si tienes otra estructura

def replace_obsidian_syntax(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Reemplaza la sintaxis de Obsidian con la de Markdown
    content = re.sub(r'!\[\[(.*?)\]\]', r'![\1](images/\1)', content)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

for root, _, files in os.walk(docs_path):
    for file in files:
        if file.endswith(".md"):
            replace_obsidian_syntax(os.path.join(root, file))

print("✅ Se han convertido las imágenes de Obsidian a formato Markdown.")
