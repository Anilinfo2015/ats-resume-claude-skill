#!/usr/bin/env python3
"""
ATS Resume Builder - PDF Converter
Converts Markdown resumes to ATS-friendly PDF format with professional formatting
"""

import argparse
import sys
import os
from pathlib import Path

# Import local modules
try:
    from resume_parser import ResumeParser
    from pdf_builder import ResumePDFBuilder
except ImportError as e:
    print(f"Error: Failed to import modules: {e}")
    print("Make sure all script files are in the same directory")
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


def main():
    """
    Main function to handle command-line arguments and execute conversion.
    """
    parser = argparse.ArgumentParser(
        description='Convert Markdown resume to ATS-friendly PDF format',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python convert_to_pdf.py resume.md
  python convert_to_pdf.py resume.md -o my_resume.pdf
  python convert_to_pdf.py input.md --output output.pdf

The script will create an ATS-optimized PDF with:
- Professional formatting and alignment
- Proper font sizes and line heights
- Clean structure for ATS systems
- Optimized spacing and margins
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
        print(f"  Loaded {len(markdown_content)} characters")

    # Step 2: Parse Markdown into structured sections
    if args.verbose:
        print("Step 2: Parsing resume structure...")
    try:
        parser_obj = ResumeParser(markdown_content)
        sections = parser_obj.get_sections()
        if args.verbose:
            print(f"  Parsed {len(sections)} sections")
    except Exception as e:
        print(f"Error parsing markdown: {e}")
        sys.exit(1)

    # Step 3: Build PDF
    if args.verbose:
        print("Step 3: Building PDF with professional formatting...")
    try:
        builder = ResumePDFBuilder(sections)
        builder.build(str(output_path))
        print(f"PDF successfully created: {output_path}")
    except Exception as e:
        print(f"Error creating PDF: {e}")
        if args.verbose:
            import traceback
            traceback.print_exc()
        sys.exit(1)

    if args.verbose:
        print("\nResume conversion complete!")
        print(f"Your ATS-friendly resume is ready: {output_path}")


if __name__ == "__main__":
    main()
