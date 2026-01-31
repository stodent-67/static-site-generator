from enum import Enum
import re

class BlockType(Enum):
    PARA = "paragraph"
    HEAD = "heading"
    CODE = "code"
    QUOT = "quote"
    UNOR = "unordered_list"
    ORDE = "ordered_list"

def block_to_block_type(text):
    if re.match(r"(?<!.)\#{1,6} ", text):
        return BlockType.HEAD
    if text.startswith("```") and text.endswith("\n```"):
        return BlockType.CODE
    #return None
    