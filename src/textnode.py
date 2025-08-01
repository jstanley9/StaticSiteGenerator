from enum import Enum

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINKS = "links"
    IMAGES = "images"

class TextNode:
    def __init__(self, text, text_type, url = None): 
        self.text = text
        self.text_type = text_type
        self.url = url

    def get_link_props(self):
        return {'href': self.url}
    
    def get_image_props(self):
        return {'src': self.url, 'alt': self.text}


    def __eq__(self, other):
        return self.text == other.text and      \
               self.text_type == other.text_type
    
    def __repr__(self):
        return f'TextNode("{self.text}", "{self.text_type.value}", "{self.url}")'
