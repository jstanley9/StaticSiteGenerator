class HTMLNode: 
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        html = ''
        if self.tag:
            html += self.tag_open_to_html()
        
        if self.value:
            html += self.value

        for child in self.children:
            html += child.to_html()

        if self.tag:
            html += self.tag_close_to_html()

        return html;
    
    def props_to_html(self):
        properties = ''
        for property, value in self.props.items():
            properties += f' {property}="{value}"'
        
        return properties
    
    def tag_open_to_html(self):
        stuff = [f'<{self.tag}']
        if self.props:
            stuff.append(self.props_to_html())
        stuff.append('>')
        return ''.join(stuff)

    def tag_close_to_html(self):
        return f'</{self.tag}>'
    
    def rep_field(self, key, value):
        if value:
            return f'"{key}": "{value}",'
        return ''

    def __repr__(self):
        text = ''.join([self.rep_field("tag", self.tag),
                        self.rep_field("value", self.value),
                        self.rep_field("children", self.children),
                        self.rep_field("props", self.props)
                        ])
        return text[:len(text) - 1]
