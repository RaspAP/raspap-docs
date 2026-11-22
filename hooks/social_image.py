"""Use a page's own banner image for its Open Graph / Twitter preview.

Add `image: images/foo.png` (path relative to docs/) to a page's front matter.
The social plugin still generates its card, but this hook replaces the
og:image and twitter:image tags it injected with the page's image.
Hooks run after plugins, so the social plugin's tags already exist here.
"""
import os
import posixpath

from PIL import Image

_TYPES = {".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg",
          ".webp": "image/webp", ".gif": "image/gif"}


def on_page_content(html, page, config, files):
    image = page.meta.get("image")
    if not image:
        return html

    url = posixpath.join(config.site_url or "/", image.lstrip("/"))
    path = os.path.join(config.docs_dir, image)
    width, height = Image.open(path).size
    mime = _TYPES.get(os.path.splitext(image)[1].lower(), "image/png")

    replace = {
        "og:image": url,
        "og:image:type": mime,
        "og:image:width": str(width),
        "og:image:height": str(height),
        "twitter:image": url,
    }
    for tag in page.meta.get("meta", []):
        key = tag.get("property") or tag.get("name")
        if key in replace:
            tag["content"] = replace[key]
    return html
