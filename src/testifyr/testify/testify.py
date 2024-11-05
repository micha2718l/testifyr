import argparse
from pathlib import Path

from ._convert_utils import open_notebook, export, detect_file_changes


name = "kinematics_problems"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--watch", action="store_true")
    parser.add_argument("--pdf", action="store_true")
    parser.add_argument("--html", action="store_true")
    parser.add_argument("--no_pre", action="store_true")
    parser.add_argument(
        "--file", type=str, default="notebooks/kinematics_problems.ipynb"
    )
    parser.add_argument("--rerun", action="store_true")

    args = parser.parse_args()
    path = Path(args.file)
    name = path.stem
    if not path.exists():
        raise FileNotFoundError(f"File {path} not found")

    if args.rerun:
        print("Command not implemented, please use `nbconvert` to rerun the notebook")

    if not args.no_pre:
        notebook = open_notebook(path)
        export(notebook, name, {}, args.pdf, args.html)
    if args.watch:
        detect_file_changes(path, pdf=args.pdf, html=args.html)
