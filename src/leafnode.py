from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, value, tag = None, props = None):
        super().__init__(tag, value, props = props)

    def to_html(self):
        if self.value:
            stuff = []
            if self.tag:
                stuff = [f'<{self.tag}']
                if self.props:
                    stuff.append(self.props_to_html())
                stuff.append('>')
                stuff.append(self.value)
                stuff.append(f'</{self.tag}>')
                return ''.join(stuff)

            return self.value

        raise ValueError('A "value" is required for a leaf node')