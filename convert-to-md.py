from pathlib import Path
import nbformat
from nbconvert import MarkdownExporter


def convert_all_ipynb_in_dir(directory="."):
    directory = Path(directory)
    notebooks = directory.glob("*.ipynb")  # Use `rglob` for recursion
    exporter = MarkdownExporter()

    for notebook_path in notebooks:
        print(f"Converting: {notebook_path.name}")
        with notebook_path.open() as f:
            notebook = nbformat.read(f, as_version=4)
        markdown_content, _ = exporter.from_notebook_node(notebook)
        md_path = notebook_path.with_suffix(".md")
        md_path.write_text(markdown_content)
        print(f"→ Saved as: {md_path.name}\n")


# Run the function on current directory
convert_all_ipynb_in_dir()
