from enum import Enum

class TextType(Enum):
	PLAIN_TEXT = "plain"
	BOLD_TEXT = "bold"
	ITALIC_TEXT = "italic"
	CODE_TEXT = "code"
	LINK_TEXT = "link"
	IMAGE_TEXT = "image"
