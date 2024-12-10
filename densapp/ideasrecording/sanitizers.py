import nh3

ALLOWED_TAGS = {"a",
                "abbr",
                "acronym",
                "b",
                "blockquote",
                "code",
                "em",
                "I",
                "li",
                "ol",
                "strong",
                "ul",
                "s",
                "sup",
                "sub",}
ALLOWED_ATTRIBUTES = {"a": {"href"},}
URL_SCHEMES = {'https'}

def sanitize_html(content):
    """Sanitize HTML content using nh3."""
    return nh3.clean(
        content,
        tags=ALLOWED_TAGS,
        attributes=ALLOWED_ATTRIBUTES,
        url_schemes=URL_SCHEMES,
        strip_comments=True,
        link_rel="noopener noreferrer",
    )