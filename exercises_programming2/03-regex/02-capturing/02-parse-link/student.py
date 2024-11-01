import re

def parse_link(string):
    match = re.fullmatch(r'<a href="(.*)">(.*)?</a>', string)
    if match:
        link, caption = match.groups('Empty caption')
        return (caption, link)

    return None