from textnode import TextNode, TextType
from generatepage import generate_page

def main():
    generate_page('./content/index.md', './template.html', './public/index.html')

main()