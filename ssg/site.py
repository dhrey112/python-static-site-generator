from pathlib import path

class Site:
    def __init__(self, source, dest):
        self.source = source
        self.source = Path(self.source)
        self.dest = dest
        self.dest = Path(self.dest)