def markdown_to_blocks(markdown):
    new_blocks = []
    if markdown:
        blocks = markdown.split('\n\n')
        for block in blocks:
            new_block = block.strip()
            if len(new_block) > 0:
                new_blocks.append(new_block)

    return new_blocks