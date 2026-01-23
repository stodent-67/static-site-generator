from textnode import TextType, TextNode

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props is None:
            return ""
        else:
            output = []
            for k, v in self.props.items():
                output.append(f' {k}="{v}"')
            return "".join(output)
    
    def __repr__(self):
        return f"HTMLNode object: tag = {self.tag}, value = {self.value}, children = {self.children}, props = {self.props}"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if not self.value:
            raise ValueError
        if not self.tag:
            return self.value
        my_props = self.props_to_html()
        return f"<{self.tag}{my_props}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"LeafNode object: tag = {self.tag}, value = {self.value}, props = {self.props}"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("ParentNode must have a tag")
        if not self.children:
            raise ValueError("ParentNode must have children")
        child_string = ""
        for child in self.children:
            child_string += child.to_html()
        props_str = self.props_to_html()
        return f"<{self.tag}{props_str}>{child_string}</{self.tag}>"

def text_node_to_html_node(text_node):
    if not text_node.text_type:
        raise Exception("TextNode must have a valid TextType")

    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            return LeafNode("a", text_node.text, dict([("href", text_node.url)]))
        case TextType.IMAGE:
            return LeafNode("img", "", dict([("src", text_node.url), ("alt", text_node.text)]))

    
