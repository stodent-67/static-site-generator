import re
from textnode import*

def extract_markdown_images(text):
    output = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return output

def extract_markdown_links(text):
    output = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return output

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
            continue
        
        images = extract_markdown_images(node.text)

        if not images:
            new_nodes.append(node)
            continue

        curr_text = node.text
        for (alt, url) in images:
            splitted = curr_text.split(f"![{alt}]({url})", 1)
            if splitted[0] != "":
                node_before = TextNode(splitted[0], TextType.TEXT)
                new_nodes.append(node_before)
            if len(splitted) > 1:
                node_image = TextNode(alt, TextType.IMAGE, url)
                new_nodes.append(node_image)
                curr_text = splitted[1]
        if curr_text != "":
            new_nodes.append(TextNode(curr_text, TextType.TEXT))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
            continue
        
        links = extract_markdown_links(node.text)

        if not links:
            new_nodes.append(node)
            continue

        curr_text = node.text
        for (anchor, url) in links:
            splitted = curr_text.split(f"[{anchor}]({url})", 1)
            if splitted[0] != "":
                node_before = TextNode(splitted[0], TextType.TEXT)
                new_nodes.append(node_before)
            if len(splitted) > 1:
                node_link = TextNode(anchor, TextType.LINK, url)
                new_nodes.append(node_link)
                curr_text = splitted[1]
        if curr_text != "":
            new_nodes.append(TextNode(curr_text, TextType.TEXT))
    return new_nodes
