from enum import Enum

class TextType(Enum):
    NORMAL_TEXT = ""
    ITALIC_TEXT = "**"
    BOLD_TEXT = "_"
    CODE_TEXT = "'"
    LINK = "[anchor text](url)"
    IMAGE = "![alt text](url)"

class TextNode():
    def __init__(self, text, text_type, url):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eg__(self, other_textnode):
        if self.text == other.text and self.text_type == other.text_type and self.url == other.url:
            return True
    def __repr__(self):
        return (f"TextNode({self.text}, {self.text_type.value}, {self.url})")
