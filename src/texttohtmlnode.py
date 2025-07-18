from textnode import TextType, TextNode
from leafnode import LeafNode

def text_node_to_html_node(text_node):
    props = None
    tag = None
    value = text_node.text

    match text_node.text_type:
        case TextType.TEXT:
            pass
        case TextType.BOLD:
            tag = 'b'
        case TextType.ITALIC:
            tag = 'i'
        case TextType.CODE:
            tag = 'code'
        case TextType.LINKS:
            tag = 'a'
            props = {'href': f'{text_node.url}'}
        case TextType.IMAGES:
            tag = 'img'
            props = {'src': f'{text_node.url}', 'alt': f'{value}'}
            value = ''
        case _:
            raise Exception(f'Unknown text type "{text_node.text_type}"')
        
    return LeafNode(tag = tag, value = value, props = props)
