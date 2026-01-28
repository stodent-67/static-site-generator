from extract import*
from textnode import*

text = "hello this is Patrick"
(before, after) = text.split("This", 1)
print(before, after)