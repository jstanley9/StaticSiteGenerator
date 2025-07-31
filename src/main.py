from textnode import TextNode, TextType
from generatepages import generate_pages_recursive
from outpututility import init_public_space

def main():
    init_public_space()
    generate_pages_recursive('./content', 'template.html', './public')

main()