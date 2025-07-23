import re

from textnode import TextNode, TextType
from extractimagesandlinks import extract_markdown_images, extract_markdown_links


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        url = node.url
        split_nodes = node.text.split(delimiter)
        last_idx = len(split_nodes) - 1
        if len(split_nodes) <= 1:
            # The delimiter must be paired so there is no delimiter or just a single delimiter.
            # Nothing to do here.
            new_nodes.append(node)
        else:
            in_type = True
            for idx, text in enumerate(split_nodes):
                in_type = not in_type
                if len(text) > 0:
                    if idx == last_idx:
                        if in_type:
                            raise Exception(f'Missing closing delimeter for {text_type.value} ({delimiter})')
                    if in_type:
                        new_nodes.append(TextNode(text, text_type, url))
                    else:
                        new_nodes.append(TextNode(text, TextType.TEXT, url))
                    url = None
                # if text is empty there is no sense in outputting an empty string
                        
    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        text = node.text
        image_couples = extract_markdown_images(text)
        if len(image_couples) == 0:
            new_nodes.append(node)
            continue

        for couple in image_couples:
            alt_text = couple[0]
            url = couple[1]
            match = f'![{alt_text}]'
            image_start = text.find(match)
            if image_start < 0:
                raise Exception(f'Internal fault: found image ({alt_text}) not found on second find\n({text})') 
            elif image_start > 0:
                new_nodes.append(TextNode(text[:image_start], TextType.TEXT))
            new_nodes.append(TextNode(alt_text, TextType.IMAGES, url))
            url_start = text.find(url)
            if url_start < 0:
                raise Exception(f'Internal fault: found image ({url}) not found on second find\n({text})')
            image_close = text.find(')', url_start + len(url) - 1)
            if image_close < 0:
                raise Exception(f'Internal fault: found image (closing paren) not found on second find\n({text})')
            text = text[image_close + 1:]

        if len(text) > 0:                        
            new_nodes.append(TextNode(text, TextType.TEXT))

    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        text = node.text
        link_couples = extract_markdown_links(text)
        if len(link_couples) == 0:
            new_nodes.append(node)
            continue

        for couple in link_couples:
            alt_text = couple[0]
            url = couple[1]
            match = f'[{alt_text}]'
            image_start = text.find(match)
            if image_start < 0:
                raise Exception(f'Internal fault: found link ({alt_text}) not found on second find\n({text})') 
            elif image_start > 0:
                new_nodes.append(TextNode(text[:image_start], TextType.TEXT))
            new_nodes.append(TextNode(alt_text, TextType.LINKS, url))
            url_start = text.find(url)
            if url_start < 0:
                raise Exception(f'Internal fault: found link ({url}) not found on second find\n({text})')
            link_close = text.find(')', url_start + len(url) - 1)
            if link_close < 0:
                raise Exception(f'Internal fault: found link (closing paren) not found on second find\n({text})')
            text = text[link_close + 1:]

        if len(text) > 0:                        
            new_nodes.append(TextNode(text, TextType.TEXT))

    return new_nodes

def text_to_textnodes(text):
    nodes = split_nodes_link(split_nodes_image([TextNode(text, TextType.TEXT)]))
    nodes = split_nodes_delimiter(nodes, '**', TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, '__', TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, '*', TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, '_', TextType.ITALIC)
    return split_nodes_delimiter(nodes, '`', TextType.CODE)