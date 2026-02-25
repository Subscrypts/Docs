"""
MkDocs hook: rewrite mkdocs-redirects pages to use absolute root-relative URLs.

mkdocs-redirects generates relative URLs (e.g. "../introduction/").
With MkDocs Material's navigation.instant, relative URLs are resolved
against the application scope root rather than the redirect page's own
URL, which causes broken redirects (e.g. "/introduction/" instead of
"/subscrypts/introduction/"). This hook post-processes all redirect pages
and replaces every relative URL with its resolved absolute equivalent.
"""

import os
import posixpath
import re


def on_post_build(config, **kwargs):
    site_dir = config["site_dir"]
    _walk(site_dir, site_dir)


def _walk(directory, site_dir):
    for entry in os.listdir(directory):
        full = os.path.join(directory, entry)
        if os.path.isdir(full):
            _walk(full, site_dir)
        elif entry == "index.html":
            _rewrite_if_redirect(full, site_dir)


def _rewrite_if_redirect(path, site_dir):
    with open(path, encoding="utf-8") as fh:
        content = fh.read()

    if "<title>Redirecting...</title>" not in content:
        return

    # Determine this page's directory relative to site root (POSIX separators).
    page_dir = os.path.relpath(os.path.dirname(path), site_dir).replace("\\", "/")
    # page_dir is e.g. "subscrypts/01-introduction"

    def make_absolute(rel_url):
        """Resolve a relative redirect URL to a root-relative absolute URL."""
        # posixpath.normpath resolves ".." segments.
        resolved = posixpath.normpath(posixpath.join(page_dir, rel_url))
        # Ensure leading slash and trailing slash (directory URL convention).
        abs_url = "/" + resolved.lstrip("/")
        if not abs_url.endswith("/"):
            abs_url += "/"
        return abs_url

    # Find the one relative redirect URL used in all three places in the template.
    match = re.search(r'url=([^"]+)"', content)
    if not match:
        return

    rel_url = match.group(1)
    abs_url = make_absolute(rel_url)

    if abs_url == rel_url:
        return  # already absolute, nothing to do

    # Replace all occurrences of the relative URL in the redirect page.
    new_content = content.replace(f'href="{rel_url}"', f'href="{abs_url}"')
    new_content = new_content.replace(f"url={rel_url}", f"url={abs_url}")
    new_content = new_content.replace(
        f'location.href="{rel_url}"', f'location.href="{abs_url}"'
    )

    if new_content != content:
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(new_content)
