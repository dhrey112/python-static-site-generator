from pathlib import Path

class Site:
    def __init__(self, source, dest):
        self.source = Path(source)
        # self.dest = dest
        self.dest = Path(dest)