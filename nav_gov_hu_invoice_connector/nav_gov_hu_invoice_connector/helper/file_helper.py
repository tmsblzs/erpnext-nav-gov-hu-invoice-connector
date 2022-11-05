import os
from pathlib import Path


class FileHelper:
    DEFAULT_BASE_PATH = "/home/frappe/frappe-bench/sites/erp.dev.pensav.hu/public/files"

    def __init__(self):
        self._base_path = FileHelper.DEFAULT_BASE_PATH

    def save_to_file(self, filename, str_to_write):
        file_name = self.get_abs_path(FileHelper.DEFAULT_BASE_PATH, filename)
        with open(file_name, 'w') as file:
            file.write(str_to_write)

    @staticmethod
    def get_real_path(path):
        path_to_check = Path(path)
        if path_to_check.exists():
            return os.path.relpath(path)
        else:
            return path

    def get_abs_path(self, directory, filename):
        file = os.path.join(self._get_base_path(), directory, filename)
        return FileHelper.get_real_path(file)

    def _get_base_path(self):
        if not self._base_path:
            return FileHelper.get_real_path(FileHelper.DEFAULT_BASE_PATH)
        else:
            return FileHelper.get_real_path(self._base_path)
