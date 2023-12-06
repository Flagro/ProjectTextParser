from ..text_parser import TextParser

class TXTParser(TextParser):
    def parse(self, path):
        with open(path, 'r') as file:
            # Read the file content
            content = file.read()
        return content
