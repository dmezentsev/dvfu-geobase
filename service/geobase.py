import os
from pathlib import Path
from typing import List, Optional

DEFAULT_ROOT = "datasets"
DEFAULT_LIMIT = 10


class Geobase:
    def __init__(self, root: str = DEFAULT_ROOT, validate: bool = False, linter: bool = False):
        self._validate = validate
        self._linter = linter
        self._storage: List[str] = []
        self.load(root=root)

    def load(self, root: str):
        for dirname, _, files in os.walk(root):
            if not files:
                continue
            for file in files:
                self.load_file(os.path.join(dirname, file))

    def load_file(self, file_path: str):
        parent_directory = str(Path(file_path).parent.name)
        with open(file_path, "r") as f:
            for line in f:
                self.add_record(line[:-1], parent_directory)

    def add_record(self, name: str, first_letters: Optional[str]):
        if self._validate and not name.lower().startswith(first_letters):
            raise ValueError(f"Значение `{name}` не начинается с `{first_letters}`")
        if self._linter and name.capitalize() != name:
            raise ValueError(f"Значение `{name}` должно начинаться с заглавной буквы")
        self._storage.append(name)

    def search(self, text: str, limit: int = DEFAULT_LIMIT) -> List[str]:
        result: List[str] = []
        for name in self._storage:
            if text.lower() in name.lower():
                result.append(name)
            if len(result) == limit:
                break
        return result
