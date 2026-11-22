"""Use a page's own banner image for its Open Graph / Twitter preview.

Add `image: images/foo.png` (path relative to docs/) to a page's front matter.
The social plugin still generates its card, but this hook rewrites the
og:image and twitter:image tags it injected to point at the page's image.

Works on the final HTML, so it is independent of how the social plugin
version in use injects its tags. Hooks run after plugins, and the social
plugin's on_post_page has priority 50, so its tags are already present.
"""
import os
import posixpath
import re

from PIL import Image

_TYPES = {".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg",
          ".webp": "image/webp", ".gif": "image/gif"}

_TAG = re.compile(
    r'(<meta\s+(?:property|name)="'
    r'(og:image(?::type|:width|:height)?|twitter:image)'
    r'"\s+content=")[^"]*(")'
)


def on_post_page(output, page, config):
    image = page.meta.get("image")
    if not image:
        return output

    url = posixpath.join(config.site_url or "/", image.lstrip("/"))
    with Image.open(os.path.join(config.docs_dir, image)) as img:
        width, height = img.size
    mime = _TYPES.get(os.path.splitext(image)[1].lower(), "image/png")

    values = {
        "og:image": url,
        "og:image:type": mime,
        "og:image:width": str(width),
        "og:image:height": str(height),
        "twitter:image": url,
    }
    return _TAG.sub(lambda m: m.group(1) + values[m.group(2)] + m.group(3),
                    output)
