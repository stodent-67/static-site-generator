from textnode import*

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    input_nodes = old_nodes
    new_nodes = []

    input_pair = (delimiter, text_type)
    check_pairs = [("**", TextType.BOLD), ("_", TextType.ITALIC), ("`", TextType.CODE)]
    if input_pair not in check_pairs:
        raise Exception(f"Invalid markdown syntax: {delimiter} does not match {text_type}")
    
    for node in input_nodes:
        count = node.text.count(delimiter)
        if count % 2 != 0:
            raise Exception(f"Invalid markdown syntax: unmatched {delimiter}")
        if count == 0:
            new_nodes.append(node)
        else:
            nodes_list = node.text.split(delimiter)
            for i in range(len(nodes_list)):
                if i % 2 == 0:
                    new_nodes.append(TextNode(nodes_list[i], TextType.TEXT))
                else:
                    new_nodes.append(TextNode(nodes_list[i], text_type))
        
    return new_nodes
