#!/usr/bin/env python3

from conversor_de_arquivos.md2html import convert_md2html


def main():
    print("markdown de entrada: ")
    markdown_file = input()

    print("arquivo de saída: ")
    output_file = input()

    convert_md2html(markdown_file, output_file)


if __name__ == "__main__":
    main()
