import re

from htmlnode import ParentNode
from textnode import TextNode, TextType
from transforms import text_node_to_html_node, text_to_textnodes


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


def wrap_text_nodes(parent_tag, nodes):
    return ParentNode(parent_tag, [text_node_to_html_node(node) for node in nodes])


def block_to_html_node(block: str) -> ParentNode:
    match block_to_block_type(block):
        case "heading":
            [markup, content] = block.split(" ", maxsplit=1)
            nodes = text_to_textnodes(content)
            return wrap_text_nodes(f"h{len(markup)}", nodes)
        case "code":
            content = block.removeprefix("```").removesuffix("```").strip()
            nodes = [TextNode(content, TextType.CODE)]
            return wrap_text_nodes("pre", nodes)
        case "quote":
            content = "\n".join(
                line.removeprefix(">").removeprefix(" ") for line in block.split("\n")
            )
            nodes = [TextNode(content, TextType.TEXT)]
            return wrap_text_nodes("blockquote", nodes)
        case "unordered_list":
            list_mark = block[0]
            lines = [
                line.removeprefix(list_mark).removeprefix(" ")
                for line in block.split("\n")
            ]
            return ParentNode(
                "ul", [wrap_text_nodes("li", text_to_textnodes(line)) for line in lines]
            )
        case "ordered_list":
            lines = [
                line.split(".", maxsplit=1)[1].removeprefix(" ")
                for line in block.split("\n")
            ]
            return ParentNode(
                "ol", [wrap_text_nodes("li", text_to_textnodes(line)) for line in lines]
            )
        case "paragraph":
            return wrap_text_nodes("p", text_to_textnodes(block))


def markdown_to_html_node(markdown: str) -> ParentNode:
    blocks = markdown_to_blocks(markdown)
    return ParentNode("div", [block_to_html_node(block) for block in blocks])
