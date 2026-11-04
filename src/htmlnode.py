class HTMLNode:
    def __init__(self, tag: str | None , value: str | None, children: list | None, props: dict | None) -> None:
        self.tag = None
        self.value = None
        self.children = None
        self.props = None
        if tag:
           self.tag = tag
        if value:
            self.value = value
        if children:
            self.childrem = children
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
