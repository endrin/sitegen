import re


def markdown_to_blocks(markdown: str) -> list[str]:
    blocks = markdown.split("\n\n")
    blocks = map(str.strip, blocks)
    blocks = filter(
        bool, blocks
    )  # calling bool will basically check if string is empty

    return list(blocks)


def block_to_block_type(block: str) -> str:
    if is_heading(block):
        return "heading"

    if is_code(block):
        return "code"

    if is_quote(block):
        return "quote"

    if is_unordered_list(block):
        return "unordered_list"

    if is_ordered_list(block):
        return "ordered_list"

    return "paragraph"


def is_heading(block: str) -> bool:
    return re.match(r"^#{1,6}\s+", block) is not None


def is_code(block) -> bool:
    return re.match(r"^```.*```$", block, re.DOTALL) is not None


def is_quote(block: str) -> bool:
    block_lines = block.split("\n")
    return all(_has_prefix(line, ">") for line in block_lines)


def is_unordered_list(block: str) -> bool:
    block_lines = block.split("\n")
    return (  # don't touch this you damn formatter
        all(_has_prefix(line, "*") for line in block_lines)
        or all(_has_prefix(line, "-") for line in block_lines)
    )


def is_ordered_list(block: str) -> bool:
    block_lines = block.split("\n")
    return all(
        _has_prefix(line, f"{number}.")
        for number, line in enumerate(block_lines, start=1)
    )


def _has_prefix(line: str, prefix: str) -> bool:
    return line.startswith(f"{prefix} ") or line == prefix
