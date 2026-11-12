class HTMLNode:
    def __init__(self, tag: str | None , value: str | None, children: list | None, props: dict | None = None) -> None:
        self.tag = None
        self.value = None
        self.children = None
        self.props = None
        if tag:
           self.tag = tag
        if value:
            self.value = value
        if children:
            self.children = children
        if props:
            self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        html: str = ''
        if not self.props:
            return ''
        for att in self.props:
            html += f' {att}="{self.props[att]}"'
        return html

    def __repr__(self) -> str:
        return f'HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})'

class LeafNode(HTMLNode):
    def __init__(self, tag: str, value: str, props: dict | None = None) -> None:
        super().__init__(tag, value, children=None, props=props)


    def to_html(self) -> str:
        if not self.value:
            raise ValueError("Invalid HTML: no value")
        if not self.tag:
            return self.value
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
        
    def __repr__(self):
        return f'LeafNode({self.tag}, {self.value}, {self.props})'
