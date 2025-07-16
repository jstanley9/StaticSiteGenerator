from textnode import *

def main():
    print("Started")
    testText = TextNode("sample text", InlineText.BOLD_TEXT, "https:/some.sort.of.url.ddd")
    print(testText)

main()