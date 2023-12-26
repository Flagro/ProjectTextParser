from ..base_parser import TextParser


class TXTParser(TextParser):
    def get_texts(self, path):
        with open(path, 'r') as file:
            # Read the file content
            content = file.read()
        return [(content, {})]
