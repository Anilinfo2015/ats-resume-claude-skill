#!/usr/bin/env python3
"""ATS Resume Builder - HTML Converter

Converts a Markdown resume to a self-contained HTML file.

Examples:
  python convert_to_html.py resume.md
  python convert_to_html.py resume.md -o resume.html
  python convert_to_html.py resume.md --no-style
"""

import argparse
import sys
from pathlib import Path


def load_markdown_file(markdown_path: str) -> str:
    try:
        with open(markdown_path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: File not found: {markdown_path}")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)


DEFAULT_CSS = """
:root { color-scheme: light; }
html, body { margin: 0; padding: 0; }
body {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif;
  font-size: 12pt;
  line-height: 1.35;
  color: #111;
  background: #fff;
}
main {
  max-width: 900px;
  margin: 32px auto;
  padding: 0 20px;
}
h1 { font-size: 22pt; margin: 0 0 10px; }
h2 { font-size: 14pt; margin: 18px 0 8px; border-bottom: 1px solid #ddd; padding-bottom: 4px; }
h3 { font-size: 12pt; margin: 12px 0 6px; }
p { margin: 6px 0; }
ul { margin: 6px 0 6px 20px; padding: 0; }
li { margin: 2px 0; }
a { color: inherit; text-decoration: none; }
table { width: 100%; border-collapse: collapse; margin: 10px 0; }
th, td { border: 1px solid #ddd; padding: 6px 8px; text-align: left; vertical-align: top; }
th { background: #f7f7f7; }
@media print {
  main { margin: 0; max-width: none; padding: 0; }
  a { text-decoration: none; }
}
""".strip()


def convert_markdown_to_html(markdown_text: str) -> str:
    try:
        import markdown as md
    except ImportError:
        print("Error: Missing dependency 'markdown'.")
        print("Install it with: pip install -r .claude/skills/ats-resume-builder/requirements.txt")
        sys.exit(1)

    return md.markdown(
        markdown_text,
        extensions=[
            "tables",
            "fenced_code",
            "sane_lists",
            "toc",
        ],
        output_format="html5",
    )


def build_html_document(title: str, body_html: str, include_style: bool) -> str:
    style_block = f"<style>\n{DEFAULT_CSS}\n</style>" if include_style else ""

    return "\n".join(
        [
            "<!doctype html>",
            '<html lang="en">',
            "<head>",
            '  <meta charset="utf-8">',
            '  <meta name="viewport" content="width=device-width, initial-scale=1">',
            f"  <title>{title}</title>",
            f"  {style_block}" if style_block else "",
            "</head>",
            "<body>",
            "  <main>",
            body_html,
            "  </main>",
            "</body>",
            "</html>",
        ]
    ).strip() + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Convert Markdown resume to HTML",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python convert_to_html.py resume.md
  python convert_to_html.py resume.md -o resume.html
  python convert_to_html.py resume.md --no-style
        """,
    )

    parser.add_argument("input", help="Path to the input Markdown file")
    parser.add_argument(
        "-o",
        "--output",
        help="Path to the output HTML file (default: same name as input with .html extension)",
        default=None,
    )
    parser.add_argument(
        "--title",
        help="HTML document title (default: derived from filename)",
        default=None,
    )
    parser.add_argument(
        "--no-style",
        action="store_true",
        help="Disable default embedded CSS styling",
    )
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose output")

    args = parser.parse_args()

    input_path = Path(args.input)
    output_path = Path(args.output) if args.output else input_path.with_suffix(".html")
    title = args.title or input_path.stem

    if args.verbose:
        print(f"Input file: {input_path}")
        print(f"Output file: {output_path}")

    markdown_content = load_markdown_file(str(input_path))
    body_html = convert_markdown_to_html(markdown_content)
    full_html = build_html_document(title=title, body_html=body_html, include_style=not args.no_style)

    try:
        output_path.write_text(full_html, encoding="utf-8")
    except Exception as e:
        print(f"Error writing output file: {e}")
        sys.exit(1)

    print(f"HTML successfully created: {output_path}")


if __name__ == "__main__":
    main()
