from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag and len(str(self.tag).strip()) > 0:
            if self.children and len(self.children) > 0:
                html_list = [self.tag_open_to_html()]
                for node in self.children:
                    html_list.append(node.to_html())
                html_list.append(self.tag_close_to_html())
                return ''.join(html_list)

            raise ValueError('A parent node must have one or more children')

        raise ValueError('A non-blank "tag" is required for a parent node')
