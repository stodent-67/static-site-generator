from textnode import*
from delimiter import*
from extract import*

def text_to_textnodes(text):
    old_nodes = TextNode(text, TextType.TEXT)
    split_nodes = split_nodes_delimiter(split_nodes_delimiter(split_nodes_delimiter([old_nodes], "**", TextType.BOLD), "_", TextType.ITALIC), "`", TextType.CODE)
    type_nodes = split_nodes_link(split_nodes_image(split_nodes))
    return type_nodes
