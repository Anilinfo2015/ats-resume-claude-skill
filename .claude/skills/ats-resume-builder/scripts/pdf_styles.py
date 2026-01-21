"""
ATS Resume PDF Styling Configuration
Defines all styling parameters for professional ATS-compliant resume formatting
"""

class PDFStyles:
    """ATS-compliant resume styling constants"""

    # Page Setup
    PAGE_FORMAT = 'letter'
    PAGE_WIDTH = 8.5
    PAGE_HEIGHT = 11.0
    MARGIN_TOP = 0.5
    MARGIN_BOTTOM = 0.5
    MARGIN_LEFT = 0.5
    MARGIN_RIGHT = 0.5

    # Fonts
    # ATS-safe: stick to a standard, embedded font (FPDF core font)
    FONT_FAMILY = 'Helvetica'
    FONT_NAME_SIZE = 24
    FONT_SUBTITLE_SIZE = 12
    FONT_SECTION_SIZE = 16
    FONT_SUBSECTION_SIZE = 13
    FONT_BODY_SIZE = 12

    # Line Heights (balanced for readability and compactness)
    # Slightly tight leading keeps the resume to 1–2 pages while remaining readable.
    LINE_HEIGHT_NAME = FONT_NAME_SIZE * 1.25 / 72
    LINE_HEIGHT_SUBTITLE = FONT_SUBTITLE_SIZE * 1.30 / 72
    LINE_HEIGHT_SECTION = FONT_SECTION_SIZE * 1.40 / 72
    LINE_HEIGHT_SUBSECTION = 16 * 1.35 / 72
    LINE_HEIGHT_BODY = FONT_BODY_SIZE * 1.35 / 72
    LINE_HEIGHT_BULLET = FONT_BODY_SIZE * 1.35 / 72

    # Spacing (in inches) - Optimized for clean separation
    SPACE_BEFORE_SECTION = 0.12
    SPACE_AFTER_SECTION_TITLE = 0.06
    SPACE_AFTER_SUBSECTION = 0.04
    SPACE_AFTER_BULLET = 0.02
    SPACE_AFTER_PARAGRAPH = 0.05
    BULLET_INDENT = 0.15
    BULLET_TEXT_INDENT = 0.30

    # Section Header Styling
    SECTION_HEADER_COLOR = (0, 0, 0)
    SECTION_HEADER_UNDERLINE = True
    # Width values are interpreted by pdf_builder.py (converted to a PDF line width)
    SECTION_HEADER_UNDERLINE_WIDTH = 1.0

    # Subsection underline styling (thinner than section)
    SUBSECTION_HEADER_UNDERLINE = True
    SUBSECTION_HEADER_UNDERLINE_WIDTH = 0.4

    # Table styling
    # Simple table look: clean grid lines (drawn as one rectangle per cell).
    TABLE_BORDER = 1
    TABLE_LINE_WIDTH = 0.01  # inches
    TABLE_COL_GAP = 0.0       # keep grid aligned
    TABLE_CELL_MARGIN = 0.02  # inches padding inside cells (if supported by fpdf)

    # Text Colors
    TEXT_COLOR = (0, 0, 0)
    # Classic hyperlink blue (readable on white, prints reasonably)
    LINK_COLOR = (0, 102, 204)

    # Border / rule color (light gray) for section lines and tables
    BORDER_COLOR = (170, 170, 170)

    # Column widths (for text layout)
    USABLE_WIDTH = PAGE_WIDTH - MARGIN_LEFT - MARGIN_RIGHT

    @staticmethod
    def get_y_position_after(current_y, height):
        """Calculate next Y position after content"""
        return current_y + height

    @staticmethod
    def get_section_spacing():
        """Get spacing before a new section"""
        return PDFStyles.SPACE_BEFORE_SECTION

    @staticmethod
    def get_bullet_x_positions():
        """Get X positions for bullet and text"""
        return {
            'bullet': PDFStyles.MARGIN_LEFT + PDFStyles.BULLET_INDENT,
            'text': PDFStyles.MARGIN_LEFT + PDFStyles.BULLET_TEXT_INDENT
        }
