class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html():
        raise NotImplemented("ToDo")
    
    def props_to_html(self):
        properties = ''
        for property, value in self.props.items():
            properties += f' {property}:"{value}"'

    def repr(self, key, value):
        if value:
            return f' "{key}": "{value}"'
        return ''
    
    def __repr__(self):
        representation = ''
        for property_name, value in vars(self).items():
            representation += self.repr(property_name, value)
            
        return representation
