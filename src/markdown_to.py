def markdown_to_blocks(text):
    new_lines = text.split("\n\n")
    strip_lines = []
    for line in new_lines:
        stripped = line.strip()
        if stripped != "":
            strip_lines.append(stripped)
    return strip_lines
