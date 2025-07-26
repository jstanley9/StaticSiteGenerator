from blocktype import  BlockType, block_to_block_type
from leafnode import LeafNode
from parentnode import ParentNode
from splitnodes import text_to_textnodes
from textnode import TextNode, TextType

def markdown_to_blocks(markdown):
    new_blocks = []
    if markdown:
        blocks = markdown.split('\n\n')
        for block in blocks:
            new_block = block.strip()
            if len(new_block) > 0:
                new_blocks.append(new_block)

    return new_blocks

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    parent_node = blocks_to_nodes(blocks)
    return parent_node

def blocks_to_nodes(blocks):
    children = blocks_to_div_nodes(blocks)
    node = ParentNode('div', children, None)
    return node

def blocks_to_div_nodes(blocks):
    children = []
    for block in blocks:
        block_type = block_to_block_type(block)
        match block_type:
            case BlockType.PARAGRAPH:
                node = make_paragraph_node(block)
            case BlockType.HEADING:
                node = make_heading_node(block)
            case BlockType.CODE:
                node = make_code_node(block)
            case BlockType.QUOTE:
                node = make_quote_node(block)
            case BlockType.UNORDERED_LIST:
                node = make_unordered_node(block)
            case BlockType.ORDERED_LIST:
                node = make_ordered_node(block)
            case _:
                node = make_paragraph_node(block)
        children.append(node)

    return children

def make_paragraph_node(block):
    children = make_paragraph_nodes(block)
    return ParentNode('p', children)

def make_paragraph_nodes(block):
    text_nodes = text_to_textnodes(' '.join(block.split('\n')))
    children = []
    for text_node in text_nodes:
        value = text_node.text
        match text_node.text_type:
            case TextType.TEXT:
                node = LeafNode(None, value)
            case TextType.BOLD:
                node = LeafNode('b', value)
            case TextType.ITALIC:
                node = LeafNode('i', value)
            case TextType.CODE:
                node = LeafNode('code', value)
            case TextType.LINKS:
                node = LeafNode('a', value, text_node.props)
            case TextType.IMAGES:
                node = LeafNode('img', value, text_node.props)
            case _:
                node = LeafNode(None, value)
        children.append(node)

    return children

def make_heading_node(block):
    start_pounds = block.split(' ', 1)
    heading = f'h{len(start_pounds[0])}'
    return LeafNode(heading, block[len(start_pounds):])

def make_code_node(block):
    return ParentNode('pre', [LeafNode('code', block.strip('`'))])

def make_quote_node(block):
    return LeafNode('blockquote', ''.join(block.split('>')))

def make_unordered_node(block):
    items = block.split('- ')
    children = []
    for line_item in items:
        if len(line_item) > 0:
            children.append(LeafNode('li', line_item.rstrip('\n')))

    return ParentNode('ul', children)

def make_ordered_node(block):
    items = block.split('\n')
    #print(f'items => {items}')
    children = []
    for line_item in items:
        if len(line_item) > 0:
            index = line_item.find(' ')
            children.append(LeafNode('li', line_item[index + 1:]))

    return ParentNode('ol', children)



markdown = """
# Testing markdown heading 1

This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

## block code

```
This is text that _should_ remain
the **same** even with inline stuff
```

- unordered
- list
- third item

1. ordered list
2. list second
3. third list item
"""

def main():
    node = markdown_to_html_node(markdown)
    html = node.to_html()

    print(html)

if __name__ == "__main__":
    main()