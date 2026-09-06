"""chroma demo file

This file is part of the Chroma Inc. codebase.
Its main purpose is to demonstrate bulk renaming operations.

"""
import logging
logger = logging.getLogger("chroma_demo")

"""Utility to perform a generic prefix rename to 'chroma_'.

Intentionally simplistic for demo purposes.
"""
import pathlib
import re
import sys

def bulk_rename(root_path: str, source_prefix: str, target_prefix: str = "chroma_"):
    """Rename a literal source prefix in Python file contents under root_path."""
    pattern = re.compile(re.escape(source_prefix))
    for path in pathlib.Path(root_path).rglob('*.py'):
        text = path.read_text()
        replaced = pattern.sub(target_prefix, text)
        if replaced != text:
            path.write_text(replaced)
            print(f"Updated {path}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise SystemExit("Usage: chroma_refactor.py <path> <source-prefix>")
    bulk_rename(sys.argv[1], sys.argv[2])
"""chroma demo file

This file is part of the Chroma Inc. codebase.
Its main purpose is to demonstrate bulk renaming operations.

"""
import logging
logger = logging.getLogger("chroma_demo")

"""Utility to perform a generic prefix rename to 'chroma_'.

Intentionally simplistic for demo purposes.
"""
import pathlib
import re
import sys

def bulk_rename(root_path: str, source_prefix: str, target_prefix: str = "chroma_"):
    """Rename a literal source prefix in Python file contents under root_path."""
    pattern = re.compile(re.escape(source_prefix))
    for path in pathlib.Path(root_path).rglob('*.py'):
        text = path.read_text()
        replaced = pattern.sub(target_prefix, text)
        if replaced != text:
            path.write_text(replaced)
            print(f"Updated {path}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise SystemExit("Usage: chroma_refactor.py <path> <source-prefix>")
    bulk_rename(sys.argv[1], sys.argv[2])
"""chroma demo file

This file is part of the Chroma Inc. codebase.
Its main purpose is to demonstrate bulk renaming operations.

"""
import logging
logger = logging.getLogger("chroma_demo")

"""Utility to perform a generic prefix rename to 'chroma_'.

Intentionally simplistic for demo purposes.
"""
import pathlib
import re
import sys

def bulk_rename(root_path: str, source_prefix: str, target_prefix: str = "chroma_"):
    """Rename a literal source prefix in Python file contents under root_path."""
    pattern = re.compile(re.escape(source_prefix))
    for path in pathlib.Path(root_path).rglob('*.py'):
        text = path.read_text()
        replaced = pattern.sub(target_prefix, text)
        if replaced != text:
            path.write_text(replaced)
            print(f"Updated {path}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise SystemExit("Usage: chroma_refactor.py <path> <source-prefix>")
    bulk_rename(sys.argv[1], sys.argv[2])
"""chroma demo file

This file is part of the Chroma Inc. codebase.
Its main purpose is to demonstrate bulk renaming operations.

"""
import logging
logger = logging.getLogger("chroma_demo")

"""Utility to perform a generic prefix rename to 'chroma_'.

Intentionally simplistic for demo purposes.
"""
import pathlib
import re
import sys

def bulk_rename(root_path: str, source_prefix: str, target_prefix: str = "chroma_"):
    """Rename a literal source prefix in Python file contents under root_path."""
    pattern = re.compile(re.escape(source_prefix))
    for path in pathlib.Path(root_path).rglob('*.py'):
        text = path.read_text()
        replaced = pattern.sub(target_prefix, text)
        if replaced != text:
            path.write_text(replaced)
            print(f"Updated {path}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise SystemExit("Usage: chroma_refactor.py <path> <source-prefix>")
    bulk_rename(sys.argv[1], sys.argv[2])
"""chroma demo file

This file is part of the Chroma Inc. codebase.
Its main purpose is to demonstrate bulk renaming operations.

"""
