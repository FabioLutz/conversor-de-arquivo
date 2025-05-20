import markdown


def convert_md2html(markdown_file, output_file):
    with open(markdown_file, "r") as markdownInput:
        inputContent = markdownInput.read()

    html = markdown.markdown(inputContent)

    with open(output_file, "w") as htmlOutput:
        htmlOutput.write(html)
