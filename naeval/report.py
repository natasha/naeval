

def table_html(table):
    html = table.to_html(escape=False)  # <b>...</b> highlights
    html = html.replace('border="1"', 'border="0"')  # for github
    return html
