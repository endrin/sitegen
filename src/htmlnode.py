class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        if children is not None:
            self.children = children
        self.props = props if props is not None else {}

    def to_html(self):
        raise NotImplementedError("this method is subclass only")

    def props_to_html(self):
        if not self.props:
            return ""

        return " " + " ".join(f'{key}="{value}"' for key, value in self.props.items())

    def __repr__(self):
        members = ", ".join(
            f"{name}={value!r}" for name, value in self.__dict__.items()
        )
        return f"{self.__class__.__name__}({members})"


class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        if tag is None and props is not None:
            raise ValueError("tag is missing")

        super().__init__(tag=tag, value=value, props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError("Leaf Node cannot be empty")

        tag = self.tag
        value = self.value
        return (
            f"<{tag}{self.props_to_html()}>{value}</{tag}>"
            if tag is not None
            else value
        )
