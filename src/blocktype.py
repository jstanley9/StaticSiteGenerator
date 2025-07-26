import re
from enum import Enum

CODE_DELIMITER = '```'
HEADING_DELIMITER = r'^#{1,6} '
QUOTE_DELIMITER = '>'
UNORDERED_DELIMITER = '- '
ORDERED_START_DELIMITER = '1. '

class BlockType(Enum):
    PARAGRAPH = 'paragraph'
    HEADING = 'heading'
    CODE = 'code'
    QUOTE = 'quote'
    UNORDERED_LIST = 'unordered list'
    ORDERED_LIST = 'ordered list'

def block_to_block_type(markdowntext: str) -> BlockType:
    block_type = BlockType.PARAGRAPH
    if len(markdowntext) > 0:
        match markdowntext[0]:
            case '#':
                block_type = is_it_heading(block_type, markdowntext)
            case '`':
                block_type = is_it_code(block_type, markdowntext)
            case '>':
                block_type = is_it_quote(block_type, markdowntext)
            case '-':
                block_type = is_it_unordered_list(block_type, markdowntext)
            case char if char == '1':
                block_type = is_it_ordered_list(block_type, markdowntext)
            case _:
                pass

    return block_type

def is_it_heading(default_block_type: BlockType, markdowntext: str) -> BlockType:
    if re.search(HEADING_DELIMITER, markdowntext):
        return BlockType.HEADING
    return default_block_type
    
def is_it_code(default_block_type: BlockType, markdowntext: str) -> BlockType:
    if len(markdowntext) >= (len(CODE_DELIMITER) * 2) and \
        markdowntext.startswith(CODE_DELIMITER) and \
            markdowntext.endswith(CODE_DELIMITER):
        return BlockType.CODE
    return default_block_type
    
def is_it_quote(default_block_type: BlockType, markdowntext: str) -> BlockType:
    return do_all_lines_start_with(default_block_type, BlockType.QUOTE, QUOTE_DELIMITER, markdowntext)
    
def is_it_unordered_list(default_block_type: BlockType, markdowntext: str) -> BlockType:
    return do_all_lines_start_with(default_block_type, BlockType.UNORDERED_LIST, UNORDERED_DELIMITER, markdowntext)

def do_all_lines_start_with(default_block_type, good_block_type, delimiter, markdowntext):
    lines = markdowntext.split('\n')
    for line in lines:
        if not line.startswith(delimiter):
            return default_block_type
    return good_block_type
        
def is_it_ordered_list(default_block_type: BlockType, markdowntext: str) -> BlockType:
    expected_sequence = 1
    lines = markdowntext.split('\n')
    for line in lines:
        if line.startswith(f'{expected_sequence}. '):
            expected_sequence += 1
            continue
        return default_block_type
    return BlockType.ORDERED_LIST