from textnode import TextNode, TextType
from outpututility import init_public_space

def main():
    print("Started")
    init_public_space()
    testText = TextNode("sample text", TextType.BOLD, "https:/some.sort.of.url.ddd")
    print(testText)

# text = '**stuff**more stuff****antipod**'
# flun = text.split('**')
# print(f'Number sections is {len(flun)}')
# for sec in flun:
#     print(f'{sec}[{len(sec)}]')
# single = 'just a simple string'
# uno = single.split('**')
# print(f'{len(uno)}:|{uno[0]}|')
main()