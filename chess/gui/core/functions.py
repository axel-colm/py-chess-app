import os

PROJECT_PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
class Function:
    @staticmethod
    def icon_path(name: str) -> str:
        return os.path.join(PROJECT_PATH, "files", "icons", name)

