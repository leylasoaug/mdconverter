import os
import markdown

def convert_md_to_html(md_file_path, html_file_path):
    with open(md_file_path, 'r', encoding='utf-8') as md_file:
        md_content = md_file.read()
        html_content = markdown.markdown(md_content)

    with open(html_file_path, 'w', encoding='utf-8') as html_file:
        html_file.write(html_content)

if __name__ == "__main__":
    md_input_file = "example.md"  
    html_output_file = "example.html"  

    convert_md_to_html(md_input_file, html_output_file)
