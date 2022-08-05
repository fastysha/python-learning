import webbrowser
HTML_TEMPLATE = """
<html>
<body>
{0}
</body>
</html>
"""

print("Hello!!!it is HTML generator")

class HtmlTag:
    def __init__(self, tag, text):
        self.tag = tag
        self.text = text

    def format_to_html_tag(self) -> str:
        return "<{0}>{1}</{0}>".format(self.tag, self.text)

tag_list = []

while True:
    tag = input("Write your tag: ")
    text = input("Write your text: ")
    stop_word=input("Write |stop| if want end: ")
    

    html_tag = HtmlTag(tag, text)

    tag_list.append(html_tag.format_to_html_tag())
    # h1 | Header => <h1>Header</h1>
    if stop_word=="stop":
        break

    
user_html = "".join(tag_list)

with open("index.html", "w") as file:
    file.write(HTML_TEMPLATE.format(user_html))
webbrowser.open_new_tab("index.html")