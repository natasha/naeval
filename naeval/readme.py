
import re

from .io import (
    load_text,
    dump_text
)


def patch_readme(name, content, path):
    text = load_text(path)
    text = re.sub(
        rf'<!--- {name} --->(.+)<!--- {name} --->',
        f'<!--- {name} --->\n' + content + f'\n<!--- {name} --->',
        text,
        flags=re.S
    )
    dump_text(text, path)
