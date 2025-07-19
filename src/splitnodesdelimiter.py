from textnode import TextNode, TextType


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
