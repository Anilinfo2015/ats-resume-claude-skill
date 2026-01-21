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
│           ├── scripts/
│           │   └── convert_to_pdf.py  # PDF conversion script
│           ├── resources/
│           │   └── ats-resume-template.md  # Comprehensive ATS template
│           └── examples/
│               ├── README.md         # Examples guide
│               ├── input-senior-engineer.md    # Sample senior-level input
│               ├── output-senior-engineer.md   # Sample senior-level output
│               ├── input-entry-level.md        # Sample entry-level input
│               ├── output-entry-level.md       # Sample entry-level output
│               └── before-after-comparison.md  # Transformation example
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

## 📚 Complete Tutorial: How to Use This Skill

### Tutorial 1: Creating Your First Resume

#### Step 1: Start a Conversation with Claude

Open a chat with Claude AI (Claude Code, Claude.ai, or any Claude interface) and say:

```
"I need help creating an ATS-optimized resume for a [Job Title] position. 
Can you interview me to build my resume?"
```

#### Step 2: The Interview Process

Claude will guide you through a structured interview, asking about:

1. **Personal Information** (5 minutes)
   - Name, email, phone, location
   - LinkedIn, GitHub, portfolio links
   - Example question: *"What's your full name and best email address?"*

2. **Professional Summary** (10 minutes)
   - Years of experience and expertise
   - Key achievements and career focus
   - Example question: *"What are your top 3 technical skills?"*

3. **Work Experience** (20-30 minutes per job)
   - Job title, company, dates
   - Responsibilities and achievements
   - Technologies used
   - Example question: *"Can you quantify the impact? For example, how many users did your work affect?"*

4. **Education** (5-10 minutes)
   - Degrees, institutions, dates
   - GPA (if relevant), honors, coursework
   - Example question: *"What was your major and graduation date?"*

5. **Skills** (10 minutes)
   - Technical skills by category
   - Soft skills and methodologies
   - Example question: *"What programming languages are you most proficient in?"*

6. **Additional Sections** (10-15 minutes)
   - Projects, certifications, awards
   - Languages, volunteer work
   - Example question: *"Do you have any personal projects or open-source contributions?"*

**Total Time: 60-90 minutes for a complete resume**

#### Step 3: Review and Refine

Claude will show you the generated resume in Markdown format. You can:

```
"Can you make the second bullet point in my current job more impactful?"
"Add more emphasis on my leadership experience"
"The dates for my education are incorrect - I graduated in May 2020"
```

#### Step 4: Convert to PDF

Once you're satisfied, Claude will save the resume as `resume.md` and instruct you to run:

```bash
python .claude/skills/ats-resume-builder/scripts/convert_to_pdf.py resume.md
```

Your ATS-optimized PDF will be ready! 🎉

---

### Tutorial 2: Updating an Existing Resume

#### Step 1: Provide Your Current Resume

```
"I have an existing resume. Can you help me optimize it for ATS?"
```

Then share your resume (copy-paste text, upload file, or describe it).

#### Step 2: Claude Analyzes Your Resume

Claude will:
- Extract all information
- Identify ATS issues (formatting, keywords, metrics)
- Suggest improvements

#### Step 3: Collaborative Improvement

Claude will ask:
```
"I notice your work experience bullets don't include quantifiable metrics. 
For your role at TechCorp, can you tell me:
- How many users did your application serve?
- What performance improvements did you achieve?
- How large was your team?"
```

#### Step 4: Generate Optimized Version

Claude creates an ATS-optimized version with:
- ✅ Quantifiable achievements
- ✅ Strong action verbs
- ✅ Proper formatting
- ✅ Keyword optimization

---

### Tutorial 3: Tailoring Resume for Specific Job

#### Step 1: Share Job Description

```
"I'm applying for this position. Can you tailor my resume to match?
[Paste job description]"
```

#### Step 2: Keyword Analysis

Claude will:
- Extract key requirements from job posting
- Identify relevant experience in your background
- Suggest keyword integration

#### Step 3: Customized Resume

Claude generates a version that:
- Emphasizes relevant experience
- Includes job-specific keywords naturally
- Highlights matching skills and achievements
- Maintains ATS optimization

---

### Tutorial 4: Different Experience Levels

#### For Recent Graduates / Entry Level:

**Focus Areas:**
- Education (place first)
- Academic projects
- Internships and part-time work
- Relevant coursework
- Technical skills
- Certifications

**Example Conversation:**
```
User: "I just graduated and only have internship experience"
Claude: "That's perfect! Let's focus on your education and projects. 
Tell me about your most impressive academic or personal project..."
```

#### For Mid-Level Professionals (3-7 years):

**Focus Areas:**
- Professional experience
- Technical expertise
- Team collaboration
- Career progression
- Certifications and learning

**Example Conversation:**
```
User: "I have 5 years of experience as a software engineer"
Claude: "Great! Let's highlight your growth. Can you tell me about 
a project where you took on increased responsibility?"
```

#### For Senior-Level (8+ years):

**Focus Areas:**
- Leadership and mentoring
- Strategic decisions
- Business impact
- Team size and scope
- Industry recognition

**Example Conversation:**
```
User: "I'm a senior engineer who's led multiple teams"
Claude: "Excellent! Let's emphasize your leadership. How many 
people have you managed, and what were the results?"
```

---

### Tutorial 5: Common Use Cases

#### Use Case 1: Career Change

```
User: "I'm transitioning from teaching to software development"
Claude: "Let's focus on transferable skills! Tell me about:
- Any coding bootcamps or self-study
- Personal projects you've built
- How your teaching experience relates (communication, mentoring)"
```

**Result:** Resume emphasizes transferable skills and new technical abilities.

#### Use Case 2: Re-entering Workforce

```
User: "I took 2 years off for family reasons"
Claude: "No problem. We'll focus on:
- Your strong experience before the gap
- Any freelance work or learning during the gap
- Skills that remained relevant
We won't highlight the gap, just present your experience professionally."
```

#### Use Case 3: Multiple Roles at Same Company

```
User: "I've been promoted twice at my current company"
Claude: "That's a great sign of growth! We'll show:
- Each role as a separate entry with dates
- Clear progression in responsibilities
- Increased scope and impact with each promotion"
```

---

### Tutorial 6: Tips for Best Results

#### DO: Provide Specific Details

❌ Bad: "I worked on improving the website"
✅ Good: "I optimized the checkout page by implementing lazy loading, which reduced load time from 5 seconds to 1.2 seconds and increased conversion rate by 23%"

#### DO: Quantify Everything

Ask yourself:
- How many? (users, projects, team members)
- How much? (money saved, revenue increased)
- By what percentage? (performance improvement, cost reduction)
- How fast? (time saved, efficiency gained)

#### DO: Use the STAR Method

When describing achievements:
- **Situation:** What was the problem?
- **Task:** What did you need to do?
- **Action:** What did you do?
- **Result:** What was the quantifiable outcome?

**Example:**
```
"Our API was slow (Situation), needed to improve response time (Task), 
implemented caching and query optimization (Action), reduced response 
time by 60% from 800ms to 320ms (Result)"
```

#### DON'T: Be Vague or Generic

❌ Avoid:
- "Responsible for..."
- "Helped with..."
- "Worked on various projects..."
- "Good at..."

✅ Instead:
- "Developed..."
- "Led..."
- "Implemented..."
- "Achieved..."

---

### Tutorial 7: ATS Optimization Checklist

After Claude generates your resume, verify:

#### ✅ Format
- [ ] Single-column layout
- [ ] Standard fonts (Arial, Calibri, Helvetica)
- [ ] No graphics, images, or special characters
- [ ] Simple bullet points (- or •)
- [ ] Consistent date format (Month Year – Month Year)

#### ✅ Content
- [ ] Every bullet starts with strong action verb
- [ ] Each achievement includes quantifiable metric
- [ ] Technologies/tools explicitly mentioned
- [ ] Keywords from job description included
- [ ] No spelling or grammar errors

#### ✅ Sections
- [ ] Professional summary (2-3 sentences)
- [ ] Work experience (reverse chronological)
- [ ] Education
- [ ] Skills (categorized)
- [ ] Certifications/Projects (if applicable)

#### ✅ Contact Information
- [ ] Email (professional address)
- [ ] Phone number
- [ ] Location (City, State)
- [ ] LinkedIn profile
- [ ] GitHub (for technical roles)

---

### Tutorial 8: Understanding the PDF Conversion

#### Basic Conversion

```bash
python .claude/skills/ats-resume-builder/scripts/convert_to_pdf.py resume.md
```

**Creates:** `resume.pdf` in the same directory

#### Custom Output Location

```bash
python .claude/skills/ats-resume-builder/scripts/convert_to_pdf.py resume.md -o ~/Documents/JohnDoe_Resume_2024.pdf
```

**Creates:** PDF with custom name in specified location

#### Verbose Mode (See What's Happening)

```bash
python .claude/skills/ats-resume-builder/scripts/convert_to_pdf.py resume.md -v
```

**Shows:**
```
Step 1: Loading Markdown file...
  ✓ Loaded 4523 characters
Step 2: Converting Markdown to HTML...
  ✓ Conversion complete
Step 3: Applying ATS-friendly styling...
  ✓ Styling applied
Step 4: Generating PDF...
✓ PDF successfully created: resume.pdf
```

#### What the Script Does

1. **Loads** your Markdown resume
2. **Converts** to HTML
3. **Applies** ATS-friendly styling:
   - Font: Arial 11pt (body), 14pt (headings), 18pt (name)
   - Line spacing: 1.15
   - Margins: 0.75 inches
   - Black text on white background
4. **Generates** professional PDF

---

### Tutorial 9: Troubleshooting

#### Problem: "Required package not found"

**Solution:**
```bash
pip install -r .claude/skills/ats-resume-builder/requirements.txt
```

#### Problem: PDF looks different than expected

**Solution:**
- Check that Markdown uses standard headers (# ## ###)
- Avoid tables, complex formatting
- Use simple bullet points (-)
- Test with template from `resources/ats-resume-template.md`

#### Problem: Claude doesn't find the skill

**Solution:**
- Ensure repository is in your project directory
- Check that `.claude/skills/ats-resume-builder/SKILL.md` exists
- Verify YAML frontmatter in SKILL.md

#### Problem: ATS not parsing resume correctly

**Solution:**
- Use .docx format instead of PDF (some ATS prefer this)
- Remove any remaining special characters
- Ensure section headers are standard
- Test with online ATS checkers

---

### Tutorial 10: Next Steps

#### After Creating Your Resume

1. **Test with ATS Checkers**
   - Jobscan.co
   - ResumeWorded.com
   - TopResume ATS checker

2. **Get Human Feedback**
   - Ask colleagues in your field
   - Share with mentors
   - Post in professional communities

3. **Tailor for Each Application**
   - Adjust keywords for each job
   - Emphasize most relevant experience
   - Keep multiple versions

4. **Keep It Updated**
   - Add new achievements monthly
   - Update skills as you learn
   - Refine bullets based on feedback

5. **Track Results**
   - Note which version gets most responses
   - A/B test different approaches
   - Refine based on interview feedback

---

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
