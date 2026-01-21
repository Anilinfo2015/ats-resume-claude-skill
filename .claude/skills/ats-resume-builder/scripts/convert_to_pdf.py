#!/usr/bin/env python3
"""
ATS Resume Builder - PDF Converter
Converts Markdown resumes to ATS-friendly PDF format
"""

import argparse
import sys
import os
from pathlib import Path

try:
    import markdown
    from weasyprint import HTML, CSS
except ImportError as e:
    print(f"Error: Required package not found: {e}")
    print("\nPlease install required packages:")
    print("  pip install markdown weasyprint")
    sys.exit(1)


def load_markdown_file(markdown_path):
    """
    Load and read the Markdown file.
    
    Args:
        markdown_path: Path to the Markdown file
        
    Returns:
        String containing the Markdown content
    """
    try:
        with open(markdown_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: File not found: {markdown_path}")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)


def convert_markdown_to_html(markdown_content):
    """
    Convert Markdown content to HTML.
    
    Args:
        markdown_content: String containing Markdown content
        
    Returns:
        String containing HTML content
    """
    # Use markdown with extra extensions for better formatting
    html_content = markdown.markdown(
        markdown_content,
        extensions=['extra', 'nl2br', 'sane_lists']
    )
    return html_content


def create_styled_html(html_content):
    """
    Wrap HTML content with ATS-friendly styling.
    
    Args:
        html_content: String containing HTML content
        
    Returns:
        Complete HTML document with CSS styling
    """
    styled_html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Resume</title>
        <style>
            /* ATS-Friendly Resume Styling - Industry Standards for Google, Meta, Facebook */
            @page {{
                size: letter;
                margin: 0.75in;  /* Standard: 0.5-1 inch, using 0.75 for balance */
            }}
            
            body {{
                font-family: 'Arial', 'Helvetica', sans-serif;  /* ATS-safe fonts */
                font-size: 11pt;  /* Body text: 10-12pt, using 11pt for readability */
                line-height: 1.15;  /* Industry standard: 1.0-1.15 */
                color: #000000;  /* Black text only for ATS */
                max-width: 8.5in;
                margin: 0 auto;
                background: white;
            }}
            
            h1 {{
                font-size: 18pt;  /* Name: 16-18pt */
                font-weight: bold;
                margin: 0 0 8pt 0;
                color: #000000;
                text-align: center;
                text-transform: uppercase;
                letter-spacing: 1pt;
            }}
            
            h2 {{
                font-size: 14pt;  /* Section headings: 14-16pt */
                font-weight: bold;
                margin: 16pt 0 8pt 0;  /* 16pt spacing between sections */
                padding-bottom: 4pt;
                border-bottom: 2px solid #000000;
                color: #000000;
                text-transform: uppercase;
                letter-spacing: 0.5pt;
            }}
            
            h3 {{
                font-size: 12pt;  /* Sub-headings */
                font-weight: bold;
                margin: 10pt 0 4pt 0;
                color: #000000;
            }}
            
            p {{
                margin: 4pt 0;
                line-height: 1.15;  /* Consistent with body */
            }}
            
            strong {{
                font-weight: bold;
                color: #000000;
            }}
            
            ul {{
                margin: 4pt 0 8pt 0;
                padding-left: 20pt;
                line-height: 1.15;
            }}
            
            li {{
                margin-bottom: 6pt;  /* 6-8pt spacing after bullets */
                line-height: 1.15;
            }}
            
            hr {{
                border: none;
                border-top: 1px solid #cccccc;
                margin: 8pt 0;
            }}
            
            a {{
                color: #0066cc;
                text-decoration: none;
            }}
            
            /* Contact information styling */
            p:first-of-type {{
                text-align: center;
                font-size: 10pt;
                margin: 4pt 0 12pt 0;
            }}
            
            /* Section spacing */
            h2 + h3 {{
                margin-top: 8pt;
            }}
            
            /* Professional experience company/title */
            h3 + p {{
                margin-top: 2pt;
            }}
            
            /* Avoid page breaks in the middle of sections */
            h2, h3 {{
                page-break-after: avoid;
            }}
            
            ul {{
                page-break-inside: avoid;
            }}
            
            /* Skills section - compact formatting */
            h2:contains("SKILLS") + p {{
                margin: 2pt 0;
            }}
        </style>
    </head>
    <body>
        {html_content}
    </body>
    </html>
    """
    return styled_html


def convert_html_to_pdf(html_content, output_path):
    """
    Convert HTML content to PDF.
    
    Args:
        html_content: String containing complete HTML document
        output_path: Path where the PDF should be saved
    """
    try:
        # Create PDF from HTML
        HTML(string=html_content).write_pdf(output_path)
        print(f"✓ PDF successfully created: {output_path}")
    except Exception as e:
        print(f"Error converting to PDF: {e}")
        sys.exit(1)


def main():
    """
    Main function to handle command-line arguments and execute conversion.
    """
    parser = argparse.ArgumentParser(
        description='Convert Markdown resume to ATS-friendly PDF format',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python .claude/skills/ats-resume-builder/scripts/convert_to_pdf.py resume.md
  python .claude/skills/ats-resume-builder/scripts/convert_to_pdf.py resume.md -o my_resume.pdf
  python .claude/skills/ats-resume-builder/scripts/convert_to_pdf.py input.md --output output.pdf

The script will create an ATS-optimized PDF with:
- Clean, professional formatting
- Standard fonts (Arial/Helvetica)
- Proper section headers and spacing
- Easy-to-parse structure for ATS systems
        """
    )
    
    parser.add_argument(
        'input',
        help='Path to the input Markdown file'
    )
    
    parser.add_argument(
        '-o', '--output',
        help='Path to the output PDF file (default: same name as input with .pdf extension)',
        default=None
    )
    
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='Enable verbose output'
    )
    
    args = parser.parse_args()
    
    # Determine output path
    if args.output:
        output_path = args.output
    else:
        # Use the same name as input but with .pdf extension
        input_path = Path(args.input)
        output_path = input_path.with_suffix('.pdf')
    
    if args.verbose:
        print(f"Input file: {args.input}")
        print(f"Output file: {output_path}")
        print()
    
    # Step 1: Load Markdown file
    if args.verbose:
        print("Step 1: Loading Markdown file...")
    markdown_content = load_markdown_file(args.input)
    if args.verbose:
        print(f"  ✓ Loaded {len(markdown_content)} characters")
    
    # Step 2: Convert Markdown to HTML
    if args.verbose:
        print("Step 2: Converting Markdown to HTML...")
    html_content = convert_markdown_to_html(markdown_content)
    if args.verbose:
        print("  ✓ Conversion complete")
    
    # Step 3: Apply styling
    if args.verbose:
        print("Step 3: Applying ATS-friendly styling...")
    styled_html = create_styled_html(html_content)
    if args.verbose:
        print("  ✓ Styling applied")
    
    # Step 4: Generate PDF
    if args.verbose:
        print("Step 4: Generating PDF...")
    convert_html_to_pdf(styled_html, output_path)
    
    if args.verbose:
        print("\n✓ Resume conversion complete!")
        print(f"  Your ATS-friendly resume is ready: {output_path}")


if __name__ == "__main__":
    main()
