from html.parser import HTMLParser


class HTMLValidator:
    """Check whether HTML content is well-formed, i.e. every tag has a matching close tag.

    This only verifies tag balance/nesting via a streaming `html.parser.HTMLParser`, not
    conformance to the actual HTML5 element vocabulary or content model — unknown tag names
    (e.g. `<foobar>`) are accepted as well-formed as long as they're properly closed.
    """

    @staticmethod
    def validate_html(path: str) -> bool:
        """Return True if the file at `path` is well-formed HTML, False otherwise.

        Reads and parses the file in chunks so memory use stays bounded regardless of file size.
        """
        parser = TagChecker()

        try:
            with open(path, "r", encoding="utf-8") as f:
                while chunk := f.read(64000):
                    parser.feed(chunk)
            parser.close()
        except FileNotFoundError as e:
            raise e
        except ValueError:
            return False

        return parser.tag_stack == []

    @staticmethod
    def validate_string(string: str) -> bool:
        """Return True if `string` is well-formed HTML, False otherwise."""
        parser = TagChecker()

        try:
            parser.feed(string)
            parser.close()
        except ValueError:
            return False
        return parser.tag_stack == []


class TagChecker(HTMLParser):
    """Tracks open tags on a stack, raising ValueError on any mismatched or unclosed tag."""

    def __init__(self):
        super().__init__()
        self.tag_stack = []

    def handle_starttag(self, tag, attrs):
        self.tag_stack.append(tag)

    def handle_endtag(self, tag):
        if not self.tag_stack or self.tag_stack[-1] != tag:
            raise ValueError(f"Mismatched end tag: {tag}")
        self.tag_stack.pop()

    def close(self):
        """Flush any buffered data, then raise ValueError if any tags were left unclosed."""
        super().close()
        if self.tag_stack:
            raise ValueError(f"Unclosed tags: {self.tag_stack}")
