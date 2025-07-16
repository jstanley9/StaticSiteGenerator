from enum import Enum

class InlineText(Enum):
    TEXT_PLAIN = "text"
    BOLD_TEXT = "bold"
    ITALIC_TEXT = "italic"
    CODE_TEXT = "code"
    LINKS = "links"
    IMAGES = "images"

class TextNode:
    def __init__(self, text, text_type, url = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return self.text == other.text and      \
               self.text_type == other.text_type
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

def main():
    testText = TextNode("sample text", InlineText.BOLD_TEXT, "https:/some.sort.of.url.ddd")
    print(f"{testText}")

if __name__ == "__main__":
    main()    