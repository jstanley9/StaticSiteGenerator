import os
import sys

from textnode import TextNode, TextType
from generatepages import generate_pages_recursive
from outpututility import init_public_space

def main():
    basepath = '/'
    if len(sys.argv) > 1:
        basepath = sys.argv[1]

    init_public_space('docs')
    generate_pages_recursive('./content', 'template.html', './docs', basepath)

main()