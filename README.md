# ATS Resume Builder - Claude AI Skill

A comprehensive Claude AI skill for creating ATS (Applicant Tracking System) optimized resumes. This skill enables Claude to interview users, generate professional resumes in Markdown format, and convert them to PDF.

## 🎯 Features

- **Interactive Interview Mode**: Claude conducts a structured interview to collect professional information
- **Resume Parsing**: Parse existing resumes and enhance them for ATS optimization
- **ATS Optimization**: Generate resumes with best practices for passing Applicant Tracking Systems
- **PDF Conversion**: Automatically convert Markdown resumes to professionally formatted PDFs
- **Customizable Templates**: Use structured templates that highlight achievements and skills

## 📁 Repository Structure

This repository follows the standard Claude skills directory structure:

```
ats-resume-claude-skill/
├── .claude/
│   └── skills/
│       └── ats-resume-builder/
│           ├── SKILL.md             # Complete skill instructions for Claude AI
│           ├── requirements.txt     # Python dependencies
│           └── scripts/
│               └── convert_to_pdf.py  # PDF conversion script
├── README.md                         # This file
└── EXAMPLE.md                        # Usage examples
```

The skill is organized in the `.claude/skills/` directory following Claude's standard skill structure, making it easy to integrate into any project.

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. Clone this repository:
```bash
git clone https://github.com/Anilinfo2015/ats-resume-claude-skill.git
cd ats-resume-claude-skill
```

2. Install required dependencies:
```bash
pip install -r .claude/skills/ats-resume-builder/requirements.txt
```

### Usage

#### Step 1: Create Your Resume with Claude

Interact with Claude AI and ask it to help you create an ATS-optimized resume. Claude will:
1. Interview you to collect your professional information
2. Generate a structured Markdown resume following ATS best practices
3. Save the resume as `resume.md`

#### Step 2: Convert to PDF

Once you have your Markdown resume, convert it to PDF:

```bash
python .claude/skills/ats-resume-builder/scripts/convert_to_pdf.py resume.md
```

Or specify a custom output name:

```bash
python .claude/skills/ats-resume-builder/scripts/convert_to_pdf.py resume.md -o my_resume.pdf
```

For verbose output:

```bash
python .claude/skills/ats-resume-builder/scripts/convert_to_pdf.py resume.md -o my_resume.pdf -v
```

## 📝 How It Works

### 1. Interview Process

Claude will systematically collect:
- Personal information (name, contact details, links)
- Professional summary and career objectives
- Work experience with quantifiable achievements
- Education and certifications
- Technical and soft skills
- Projects and accomplishments
- Awards and achievements

### 2. ATS Optimization

The generated resume follows ATS best practices:
- ✅ Simple, clean formatting without complex layouts
- ✅ Standard section headers
- ✅ Action verbs and quantifiable achievements
- ✅ Relevant keywords for your industry
- ✅ Consistent formatting and structure
- ✅ Standard fonts and proper spacing

### 3. PDF Generation

The conversion script creates professional PDFs with:
- Clean, ATS-friendly formatting
- Standard Arial/Helvetica fonts
- Proper margins and spacing
- Section headers with clear hierarchy
- Easy-to-parse structure for ATS systems

## 🛠️ Script Options

The `convert_to_pdf.py` script supports the following options:

```bash
python .claude/skills/ats-resume-builder/scripts/convert_to_pdf.py [-h] [-o OUTPUT] [-v] input

Arguments:
  input                 Path to the input Markdown file

Options:
  -h, --help           Show help message and exit
  -o, --output OUTPUT  Path to the output PDF file (default: input name with .pdf extension)
  -v, --verbose        Enable verbose output
```

## 📚 Examples

### Example 1: Basic Conversion
```bash
python .claude/skills/ats-resume-builder/scripts/convert_to_pdf.py resume.md
# Creates resume.pdf in the same directory
```

### Example 2: Custom Output Location
```bash
python .claude/skills/ats-resume-builder/scripts/convert_to_pdf.py resume.md -o ~/Documents/john_doe_resume.pdf
```

### Example 3: Verbose Mode
```bash
python .claude/skills/ats-resume-builder/scripts/convert_to_pdf.py resume.md -v
# Shows detailed progress of the conversion process
```

## 🎓 Best Practices

When creating your resume with this skill:

1. **Be Specific**: Use concrete numbers and metrics (e.g., "Increased sales by 25%")
2. **Use Action Verbs**: Start bullet points with strong verbs (Developed, Implemented, Led)
3. **Tailor Content**: Customize your resume for each job application
4. **Keep It Concise**: Aim for 1-2 pages for most positions
5. **Proofread**: Ensure there are no spelling or grammar errors
6. **Include Keywords**: Use industry-specific terms from job descriptions

## 🔧 Dependencies

- `markdown>=3.4.0` - Markdown to HTML conversion
- `weasyprint>=68.0` - HTML to PDF rendering (security patched)
- `Pillow>=10.2.0` - Image processing support (security patched)
- `cffi>=1.15.0` - Foreign function interface

## 📄 License

This project is open source and available for use in creating professional resumes.

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests
- Improve documentation

## 💡 Tips for Success

- **Review the SKILL.md**: Located at `.claude/skills/ats-resume-builder/SKILL.md`, it contains comprehensive instructions for Claude
- **Iterate**: Don't hesitate to refine your resume multiple times
- **Test ATS Compatibility**: Use online ATS checkers to verify your resume
- **Keep It Updated**: Regularly update your resume with new achievements
- **Get Feedback**: Have others review your resume before submitting

## 📞 Support

For issues or questions:
1. Check the SKILL.md documentation in `.claude/skills/ats-resume-builder/SKILL.md`
2. Review the script help: `python .claude/skills/ats-resume-builder/scripts/convert_to_pdf.py --help`
3. Open an issue on GitHub

## 🔧 Using as a Claude Skill

This repository is structured as a proper Claude skill. To use it:

1. **For Claude Code/Projects**: Simply clone this repository and the skill will be available in the `.claude/skills/` directory
2. **For Standalone Use**: The skill can be copied into any project's `.claude/skills/` directory
3. **Metadata**: The SKILL.md file includes YAML frontmatter with name and description for Claude to discover and use the skill

### Claude Skill Structure

The skill follows the standard Claude directory structure:
- **`.claude/skills/ats-resume-builder/`**: Skill root directory
- **`SKILL.md`**: Main skill instructions with YAML frontmatter
- **`scripts/`**: Supporting Python scripts for PDF conversion
- **`requirements.txt`**: Python dependencies

---

**Note**: This skill is designed to work with Claude AI and follows best practices for creating ATS-optimized resumes. The generated PDFs are compatible with most Applicant Tracking Systems.
