import bleach

allowed_tags = ['b', 'i', 'u', 'ul', 'ol', 'li', 'p', 'br', 'strong', 'em']
allowed_attributes = {}
allowed_styles = []

def sanitize_html(content):
    return bleach.clean(
        content,
        tags=allowed_tags,
        attributes=allowed_attributes,
        # styles=allowed_styles,
    )