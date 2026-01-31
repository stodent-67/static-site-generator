from block import*
import unittest

class TestBlockType(unittest.TestCase):
    def test_block_heading(self):
        blocks = ["# Heading 1",
                    "## Heading 2",
                    "### Heading 3",
                    "#### Heading 4",
                    "##### Heading 5",
                    "###### Heading 6",
                    "####### Not Heading",
                    "Normal",
                    "huh### ",
                    "I am a naughty block ### lol"
                    ]
        results = []
        for block in blocks:
            results.append(block_to_block_type(block))
        expect = [BlockType.HEAD, 
                    BlockType.HEAD, 
                    BlockType.HEAD, 
                    BlockType.HEAD, 
                    BlockType.HEAD, 
                    BlockType.HEAD, 
                    None, 
                    None, 
                    None, 
                    None
                    ]
        self.assertListEqual(results, expect)
    
    def test_block_code(self):
        blocks = ["""```
This is code
```""",
"`` This is not code ```",
"""```
This is also code on 
multiple lines
```"""]
        results = []
        for block in blocks:
            results.append(block_to_block_type(block))
        expect = [BlockType.CODE, None, BlockType.CODE]
        self.assertListEqual(results, expect)


if __name__ == "__main__":
    unittest.main()