import os
from typing import List

DEFAULT_ROOT = "datasets"
DEFAULT_LIMIT = 10


class Geobase:
    def __init__(self, root: str = DEFAULT_ROOT):
        self._storage: List[str] = []
        self.load(root=root)

    def load(self, root: str):
        for dirname, _, files in os.walk(root):
            if not files:
                continue
            for file in files:
                self.load_file(os.path.join(dirname, file))

    def load_file(self, file_path: str):
        with open(file_path, "r") as f:
            for line in f:
                self.add_record(line)

    def add_record(self, name: str):
        self._storage.append(name)

    def search(self, text: str, limit: int = DEFAULT_LIMIT) -> List[str]:
        result: List[str] = []
        for name in self._storage:
            if text.lower() in name.lower():
                result.append(name)
            if len(result) == limit:
                break
        return result
