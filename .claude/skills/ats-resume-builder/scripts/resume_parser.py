"""
Resume Markdown Parser
Parses markdown resume content into structured data
"""

import re


class ResumeParser:
    """Parse markdown resume into structured sections"""

    def __init__(self, markdown_content):
        self.content = markdown_content
        self.sections = []
        self.parse()

    def parse(self):
        """Parse markdown content into sections"""
        lines = self.content.split('\n')
        current_section = None

        for i, line in enumerate(lines):
            # Skip empty lines at start
            if not line.strip() and not current_section:
                continue

            # Main title (H1)
            if line.startswith('# '):
                if current_section:
                    self.sections.append(current_section)
                current_section = {
                    'type': 'title',
                    'title': self.clean_text(line[2:].strip()),
                    'content': []
                }

            # Section header (H2)
            elif line.startswith('## '):
                if current_section:
                    self.sections.append(current_section)
                current_section = {
                    'type': 'section',
                    'title': self.clean_text(line[3:].strip()),
                    'content': []
                }

            # Subsection header (H3)
            elif line.startswith('### '):
                if current_section and current_section['type'] in ['title', 'section']:
                    current_section['content'].append({
                        'type': 'subsection',
                        'title': self.clean_text(line[4:].strip()),
                        'items': []
                    })

            # Table rows
            elif line.strip().startswith('|'):
                # Check for separator line |---|
                if re.match(r'^[\|\s\-:]+$', line.strip()):
                    continue

                cells = [c.strip() for c in line.strip().split('|') if c.strip()]
                if not cells:
                    continue

                if current_section:
                    # Check if we are already building a table
                    last_item = current_section['content'][-1] if current_section['content'] else None

                    # If previous item was a paragraph that looks like a header (and we are now processing a row),
                    # convert that previous paragraph into a table header.
                    # This happens because the parser reads line-by-line. The header row is read as a 'paragraph' first,
                    # then the separator line comes (which we skip), and then this row.
                    
                    # However, since we just skipped the separator, the header is likely the LAST item added.
                    
                    if last_item and last_item['type'] == 'paragraph' and not getattr(last_item, 'is_table_header', False):
                         # If we just saw a separator line (implied by context usually, but here we process linearly)
                         # Actually, standard MD tables are: Header \n Separator \n Row.
                         # When we hit Separator, we do `continue`.
                         # So when we hit Row 1, the Header is sitting in `current_section['content']` as a paragraph (or whatever it parsed as).
                         # We need to retroactively bundle it.
                         pass
                    
                    # Simplified approach:
                    # If the last item is a Table, append to it.
                    # If the last item is NOT a Table, create a new Table.
                    # BUT we might have a header row sitting as a 'paragraph' or similar just before us.
                    # Let's check if the PREVIOUS line was a separator.
                    
                    is_new_table = True
                    if current_section['content'] and current_section['content'][-1]['type'] == 'table':
                        is_new_table = False
                    
                    if is_new_table:
                        # Check if we should grab the previous element as a header
                        # This matches standard MD table syntax
                        header_row = []
                        if current_section['content'] and i > 0 and '---' in lines[i-1]:
                             # If line i-1 was separator, then lines[i-2] was header
                             # But lines[i-2] is already parsed into current_section['content'][-1]
                             prev_item = current_section['content'][-1]
                             # If it was parsed as a paragraph (which it likely was if it started with |)
                             # Wait, the parser logic: "elif line.strip().startswith('|'):" checks for pipes.
                             # If the header had pipes, it would have entered THIS block.
                             pass

                # Let's rethink.
                # If a line starts with |, it comes here.
                # If it's a separator, we skip it.
                # If it's data (header OR row), we process it.
                
                # We need to distinguish Header from Row.
                # The only way to know if a row is a header is if the NEXT line is a separator.
                # But we are iterating forward.
                
                # So:
                # 1. If line starts with |, it's a "Table Row Candidate".
                # 2. Look ahead to see if next line is separator. If so, this is Header.
                # 3. If previous line was separator. If so, this is Row 1.
                
                is_separator = re.match(r'^[\|\s\-:]+$', line.strip())
                if is_separator:
                     continue
                
                # It's a row (either header or body)
                cells = [self.clean_text(c) for c in line.strip().split('|') if c.strip()]
                
                # Determine if this row is a header
                is_header = False
                if i + 1 < len(lines):
                    next_line = lines[i+1].strip()
                    if next_line.startswith('|') and re.match(r'^[\|\s\-:]+$', next_line):
                        is_header = True
                
                if current_section:
                    last_content = current_section['content'][-1] if current_section['content'] else None
                    
                    if last_content and last_content['type'] == 'table':
                         # Append to existing table
                         last_content['rows'].append(cells)
                    else:
                        # Start new table
                        # If this is a header, we initialize with headers. If not, just rows.
                        new_table = {
                            'type': 'table',
                            'headers': cells if is_header else None,
                            'rows': [] if is_header else [cells]
                        }
                        current_section['content'].append(new_table)

            # Bullet points
            elif line.startswith('- ') or line.startswith('* '):
                bullet_text = self.clean_text(line[2:].strip())
                if current_section:
                    if current_section['content'] and current_section['content'][-1]['type'] == 'subsection':
                        current_section['content'][-1]['items'].append({
                            'type': 'bullet',
                            'text': bullet_text
                        })
                    else:
                        current_section['content'].append({
                            'type': 'bullet',
                            'text': bullet_text
                        })

            # Paragraph text (non-empty lines that aren't headers or bullets)
            elif line.strip() and not line.startswith('|'):
                if current_section:
                    current_section['content'].append({
                        'type': 'paragraph',
                        'text': self.clean_text(line.strip())
                    })

        # Add last section
        if current_section:
            self.sections.append(current_section)

    @staticmethod
    def clean_text(text):
        """Remove markdown formatting from text"""
        # Fix common Unicode characters that break standard PDF encoding
        replacements = {
            '\u2013': '-',  # en dash
            '\u2014': '-',  # em dash
            '\u2018': "'",  # left single quote
            '\u2019': "'",  # right single quote
            '\u201c': '"',  # left double quote
            '\u201d': '"',  # right double quote
            '\u2022': '-',  # bullet
        }
        for char, replacement in replacements.items():
            text = text.replace(char, replacement)

        # Remove bold (**text**)
        text = re.sub(r'\*\*(.*?)\*\*', r'\1', text)
        # Remove italic (*text*)
        text = re.sub(r'\*(.*?)\*', r'\1', text)
        # Remove links [text](url)
        text = re.sub(r'\[(.*?)\]\(.*?\)', r'\1', text)
        # Handle Unicode for ASCII-safe PDF
        try:
            text = text.encode('ascii', 'replace').decode('ascii')
        except:
            text = text.encode('utf-8', 'replace').decode('utf-8', 'replace')
        return text.strip()

    def get_sections(self):
        """Return parsed sections"""
        return self.sections
