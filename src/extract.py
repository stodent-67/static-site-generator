import re

def extract_markdown_images(text):
    output = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return output

def extract_markdown_links(text):
    output = re.findall(r"\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return output
