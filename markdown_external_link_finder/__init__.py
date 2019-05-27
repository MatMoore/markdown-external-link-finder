import glob
import mistune
from mistune import Renderer
from urllib.parse import urlsplit

def url_is_absolute(url):
    return bool(urlsplit(url, scheme='https').netloc)


class LinkRenderer(Renderer):
    def __init__(self):
        self.urls = []
        super().__init__()

    def link(self, link, title, text):
        if url_is_absolute(link):
            self.urls.append(link)


def extract_markdown_links(markdown_files):
    impl = LinkRenderer()
    renderer = mistune.Markdown(renderer=impl)

    for markdown_file in markdown_files:
        with open(markdown_file) as f:
            text = f.read()
        renderer(text)

    yield from impl.urls


if __name__ == '__main__':
    markdown_files = glob.glob('**/*.md', recursive=True)
    for url in extract_markdown_links(markdown_files):
        print(url)