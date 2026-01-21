"""
ATS Resume PDF Builder
Creates professionally formatted ATS-compliant resume PDFs
"""

from fpdf import FPDF
from pdf_styles import PDFStyles

import re


class ResumePDFBuilder:
    """Build ATS-compliant resume PDF with proper formatting"""

    def __init__(self, sections):
        self.sections = sections
        self.pdf = None
        self.current_y = PDFStyles.MARGIN_TOP

    def build(self, output_path):
        """Build complete resume PDF"""
        self.pdf = FPDF(
            format=PDFStyles.PAGE_FORMAT,
            unit='in'
        )
        self.pdf.add_page()
        self.pdf.set_auto_page_break(auto=True, margin=PDFStyles.MARGIN_BOTTOM)

        # Set margins
        self.pdf.set_left_margin(PDFStyles.MARGIN_LEFT)
        self.pdf.set_right_margin(PDFStyles.MARGIN_RIGHT)
        self.pdf.set_top_margin(PDFStyles.MARGIN_TOP)

        # Set text color
        r, g, b = PDFStyles.TEXT_COLOR
        self.pdf.set_text_color(r, g, b)

        # Process sections
        for section in self.sections:
            if section['type'] == 'title':
                self._add_title(section)
            elif section['type'] == 'section':
                self._add_section(section)

        # Save PDF
        self.pdf.output(output_path)

    def _set_text_color(self, rgb):
        r, g, b = rgb
        self.pdf.set_text_color(r, g, b)

    def _split_link_segments(self, text: str):
        """Split text into (segment, is_link) pairs for URL/email substrings."""
        if not text:
            return []

        # Conservative URL/email detection (good enough for resume contact lines)
        pattern = re.compile(
            r'(?P<url>https?://\S+|www\.\S+|\b(?:linkedin\.com|github\.com)\S*)'
            r'|(?P<email>[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,})'
        )

        segments = []
        last = 0
        for m in pattern.finditer(text):
            if m.start() > last:
                segments.append((text[last:m.start()], False))

            link = m.group(0)

            # Trim common trailing punctuation from detected links
            trailing = ''
            while link and link[-1] in ').,;]':
                trailing = link[-1] + trailing
                link = link[:-1]

            if link:
                segments.append((link, True))
            if trailing:
                segments.append((trailing, False))

            last = m.end()

        if last < len(text):
            segments.append((text[last:], False))
        return segments

    def _write_centered_segments(self, segments, line_height, font_size, font_style=''):
        """Write a single line centered, coloring only link segments."""
        if not segments:
            return

        self.pdf.set_font(PDFStyles.FONT_FAMILY, font_style, font_size)
        widths = [self.pdf.get_string_width(t) for (t, _is_link) in segments]
        total_w = sum(widths)

        usable = PDFStyles.USABLE_WIDTH
        start_x = PDFStyles.MARGIN_LEFT + max(0, (usable - total_w) / 2)
        y = self.pdf.get_y()

        x = start_x
        for (seg_text, is_link), w in zip(segments, widths):
            self._set_text_color(PDFStyles.LINK_COLOR if is_link else PDFStyles.TEXT_COLOR)
            self.pdf.set_xy(x, y)
            self.pdf.cell(w, line_height, seg_text, align='L')
            x += w

        # Move to next line
        self._set_text_color(PDFStyles.TEXT_COLOR)
        self.pdf.set_xy(PDFStyles.MARGIN_LEFT, y + line_height)

    def _safe_cell(self, x, y, w, h, text, font_size, font_style='', align='L'):
        """Safely add cell with position management"""
        self.pdf.set_xy(x, y)
        self.pdf.set_font(PDFStyles.FONT_FAMILY, font_style, font_size)
        self.pdf.cell(w, h, text, align=align, new_y='NEXT')
        return self.pdf.get_y()

    def _safe_multi_cell(self, w, h, text, font_size, font_style='', align='L'):
        """Safely add multi_cell with proper handling"""
        self.pdf.set_font(PDFStyles.FONT_FAMILY, font_style, font_size)
        self.pdf.multi_cell(w, h, text, align=align, new_x='LMARGIN', new_y='NEXT')
        return self.pdf.get_y()

    def _add_title(self, section):
        """Add resume title section"""
        width = PDFStyles.USABLE_WIDTH

        # Name
        self._safe_multi_cell(width, PDFStyles.LINE_HEIGHT_NAME,
                              section['title'], PDFStyles.FONT_NAME_SIZE, 'B', 'C')

        # Contact info: color only the actual URL/email substring, not the entire line
        for item in section['content']:
            if item['type'] != 'paragraph':
                continue

            raw = item['text']

            # If the line uses pipes, render as centered segments so only link parts are blue
            if '|' in raw:
                parts = [p.strip() for p in raw.split('|')]
                # If too wide, fall back to printing each part on its own line
                # (still with link-only coloring)
                joined = ' | '.join(parts)
                approx_w = self.pdf.get_string_width(joined)
                if approx_w > width:
                    for p in parts:
                        segments = self._split_link_segments(p)
                        self._write_centered_segments(segments, PDFStyles.LINE_HEIGHT_SUBTITLE, PDFStyles.FONT_SUBTITLE_SIZE, '')
                else:
                    segments = []
                    for idx, p in enumerate(parts):
                        if idx > 0:
                            segments.append((' | ', False))
                        segments.extend(self._split_link_segments(p))
                    self._write_centered_segments(segments, PDFStyles.LINE_HEIGHT_SUBTITLE, PDFStyles.FONT_SUBTITLE_SIZE, '')
            else:
                segments = self._split_link_segments(raw)
                # If no link detected, keep default centered multi-cell
                if not any(is_link for (_t, is_link) in segments):
                    self._safe_multi_cell(width, PDFStyles.LINE_HEIGHT_SUBTITLE,
                                          raw, PDFStyles.FONT_SUBTITLE_SIZE, '', 'C')
                else:
                    self._write_centered_segments(segments, PDFStyles.LINE_HEIGHT_SUBTITLE, PDFStyles.FONT_SUBTITLE_SIZE, '')

        # Add spacing after title section
        self.pdf.ln(PDFStyles.SPACE_BEFORE_SECTION)

    def _add_section(self, section):
        """Add resume section with proper formatting"""
        width = PDFStyles.USABLE_WIDTH

        # Add spacing before section
        self.pdf.ln(PDFStyles.SPACE_BEFORE_SECTION)

        # Section title
        self._safe_multi_cell(width, PDFStyles.LINE_HEIGHT_SECTION,
                              section['title'], PDFStyles.FONT_SECTION_SIZE, 'B', 'L')

        # Underline for section title (positioned below text with proper clearance)
        x = PDFStyles.MARGIN_LEFT
        y = self.pdf.get_y() - 0.05  # 0.05" above current position
        if hasattr(PDFStyles, 'BORDER_COLOR'):
            r, g, b = PDFStyles.BORDER_COLOR
            self.pdf.set_draw_color(r, g, b)
        self.pdf.set_line_width(PDFStyles.SECTION_HEADER_UNDERLINE_WIDTH / 144)
        self.pdf.line(x, y, PDFStyles.PAGE_WIDTH - PDFStyles.MARGIN_RIGHT, y)

        # Add spacing after section title
        self.pdf.ln(PDFStyles.SPACE_AFTER_SECTION_TITLE)

        # Section content
        for item in section['content']:
            if item['type'] == 'subsection':
                self._add_subsection(item)
            elif item['type'] == 'bullet':
                self._add_bullet(item['text'])
            elif item['type'] == 'paragraph':
                self._add_paragraph(item['text'])
            elif item['type'] == 'table':
                self._add_table(item)

    def _add_table(self, table):
        """Render a table section"""
        if not table.get('rows') and not table.get('headers'):
            return

        # Calculate column widths
        # Simple approach: equal width based on max columns in header or first row
        num_cols = 0
        if table.get('headers'):
            num_cols = len(table['headers'])
        elif table.get('rows'):
            num_cols = len(table['rows'][0])
            
        if num_cols == 0:
            return

        gap = getattr(PDFStyles, 'TABLE_COL_GAP', 0)
        total_gap = gap * (num_cols - 1)
        usable_for_cells = max(0, PDFStyles.USABLE_WIDTH - total_gap)

        # Use 30% for first column (Categories) and 70% for second (Skills) if 2 columns
        # Otherwise equal distribution
        col_widths = []
        if num_cols == 2:
            col_widths = [usable_for_cells * 0.3, usable_for_cells * 0.7]
        else:
            col_widths = [usable_for_cells / num_cols] * num_cols

        # Use consistent font for table
        self.pdf.set_font(PDFStyles.FONT_FAMILY, '', PDFStyles.FONT_BODY_SIZE)
        line_height = PDFStyles.LINE_HEIGHT_BODY

        # Table stroke should be thin but visible
        if hasattr(PDFStyles, 'TABLE_LINE_WIDTH'):
            try:
                self.pdf.set_line_width(PDFStyles.TABLE_LINE_WIDTH)
            except Exception:
                pass

        # Add a touch of padding inside cells when supported (fpdf2)
        prev_cell_margin = None
        if hasattr(self.pdf, 'get_cell_margin') and hasattr(self.pdf, 'set_cell_margin'):
            try:
                prev_cell_margin = self.pdf.get_cell_margin()
                self.pdf.set_cell_margin(getattr(PDFStyles, 'TABLE_CELL_MARGIN', 0.02))
            except Exception:
                prev_cell_margin = None

        # Helper to draw a row
        def draw_row(cells, is_header=False):
            row_y = self.pdf.get_y()

            # Check page break (keep a small buffer so rows don't get split awkwardly)
            if row_y > (PDFStyles.PAGE_HEIGHT - PDFStyles.MARGIN_BOTTOM - 0.35):
                self.pdf.add_page()
                row_y = self.pdf.get_y()

            start_x = PDFStyles.MARGIN_LEFT
            current_x = start_x
            max_y = row_y

            # First pass: write text for each cell (no borders), track max Y.
            cell_boxes = []
            for idx, cell_text in enumerate(cells):
                if idx >= len(col_widths):
                    break

                style = 'B' if (is_header or (num_cols == 2 and idx == 0)) else ''
                self.pdf.set_font(PDFStyles.FONT_FAMILY, style, PDFStyles.FONT_BODY_SIZE)

                cell_x = current_x
                cell_y = row_y
                cell_w = col_widths[idx]

                self.pdf.set_xy(cell_x, cell_y)
                # Write cell text without borders so borders can be drawn as clean rectangles later
                self.pdf.multi_cell(cell_w, line_height, cell_text, border=0, align='L')

                cell_end_y = self.pdf.get_y()
                if cell_end_y > max_y:
                    max_y = cell_end_y

                cell_boxes.append((cell_x, cell_y, cell_w))
                current_x += cell_w + gap

            # Second pass: draw one clean rectangle per cell using the row height
            row_h = max_y - row_y
            if getattr(PDFStyles, 'TABLE_BORDER', 0):
                if hasattr(PDFStyles, 'BORDER_COLOR'):
                    r, g, b = PDFStyles.BORDER_COLOR
                    self.pdf.set_draw_color(r, g, b)
                for (cell_x, cell_y, cell_w) in cell_boxes:
                    try:
                        self.pdf.rect(cell_x, cell_y, cell_w, row_h)
                    except Exception:
                        pass

            # Move to start of next row
            self.pdf.set_xy(start_x, max_y)

        # Draw Headers
        if table.get('headers'):
            draw_row(table['headers'], is_header=True)

        # Draw Rows
        for row in table['rows']:
            draw_row(row, is_header=False)
            
        self.pdf.ln(PDFStyles.SPACE_AFTER_PARAGRAPH)

        # Restore previous cell margin if we changed it
        if prev_cell_margin is not None and hasattr(self.pdf, 'set_cell_margin'):
            try:
                self.pdf.set_cell_margin(prev_cell_margin)
            except Exception:
                pass

    def _add_subsection(self, subsection):
        """Add subsection (job title, etc.)"""
        width = PDFStyles.USABLE_WIDTH

        # Subsection title (bold)
        self._safe_multi_cell(width, PDFStyles.LINE_HEIGHT_SUBSECTION,
                              subsection['title'], PDFStyles.FONT_SUBSECTION_SIZE, 'B', 'L')

        # Underline for subsection title (thin)
        if getattr(PDFStyles, 'SUBSECTION_HEADER_UNDERLINE', False):
            x = PDFStyles.MARGIN_LEFT
            y = self.pdf.get_y() - 0.04
            if hasattr(PDFStyles, 'BORDER_COLOR'):
                r, g, b = PDFStyles.BORDER_COLOR
                self.pdf.set_draw_color(r, g, b)
            self.pdf.set_line_width(getattr(PDFStyles, 'SUBSECTION_HEADER_UNDERLINE_WIDTH', 0.4) / 144)
            self.pdf.line(x, y, PDFStyles.PAGE_WIDTH - PDFStyles.MARGIN_RIGHT, y)

        self.pdf.ln(PDFStyles.SPACE_AFTER_SUBSECTION)

        # Add bullets/items under subsection
        for item in subsection['items']:
            if item['type'] == 'bullet':
                self._add_bullet(item['text'])

    def _add_bullet(self, text):
        """Add a single bullet point with proper indentation"""
        # Ensure we have space for at least one line of bullet text to avoid orphaned bullets
        space_needed = PDFStyles.LINE_HEIGHT_BULLET
        if self.pdf.get_y() + space_needed > (PDFStyles.PAGE_HEIGHT - PDFStyles.MARGIN_BOTTOM):
            self.pdf.add_page()

        x_pos = PDFStyles.get_bullet_x_positions()
        y_before = self.pdf.get_y()

        # Add bullet character
        self.pdf.set_font(PDFStyles.FONT_FAMILY, '', PDFStyles.FONT_BODY_SIZE)
        self.pdf.set_xy(x_pos['bullet'], y_before)
        self.pdf.cell(0.15, PDFStyles.LINE_HEIGHT_BULLET, '-', align='L')

        # Add bullet text (keep black; ATS-friendly and avoids partial-color complexity in wrapped text)
        self._set_text_color(PDFStyles.TEXT_COLOR)
        bullet_width = PDFStyles.USABLE_WIDTH - PDFStyles.BULLET_TEXT_INDENT
        self.pdf.set_xy(x_pos['text'], y_before)
        self.pdf.multi_cell(
            w=bullet_width,
            h=PDFStyles.LINE_HEIGHT_BULLET,
            text=text,
            align='L',
            new_x='LMARGIN',
            new_y='NEXT'
        )

        # Add small spacing after bullet
        self.pdf.ln(PDFStyles.SPACE_AFTER_BULLET)

    def _add_paragraph(self, text):
        """Add a paragraph with proper spacing"""
        width = PDFStyles.USABLE_WIDTH
        self._set_text_color(PDFStyles.TEXT_COLOR)
        self._safe_multi_cell(width, PDFStyles.LINE_HEIGHT_BODY,
                              text, PDFStyles.FONT_BODY_SIZE, '', 'L')
        self.pdf.ln(PDFStyles.SPACE_AFTER_PARAGRAPH)
