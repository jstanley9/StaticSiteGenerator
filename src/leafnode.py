from htmlnode import HTMLNode

class LeafNode(HTMLNode): 
    def __init__(self, tag = None, value = None, props = None):
        super().__init__(tag, value, props = props)

    def to_html(self):
        if self.value != None:
            if self.tag:
                html_list = [self.tag_open_to_html()]
                html_list.append(self.value)
                html_list.append(self.tag_close_to_html())
                return ''.join(html_list)

            return self.value

        raise ValueError('A "value" is required for a leaf node')