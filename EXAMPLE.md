# Example: Using the ATS Resume Builder Skill

This example demonstrates how to use the ATS Resume Builder Claude AI Skill.

## Quick Demo

### Step 1: Create a Resume Markdown File

You can either:
1. Ask Claude to interview you and create a resume
2. Create a resume manually following the template in SKILL.md

Here's a minimal example (`demo_resume.md`):

```markdown
# JANE SMITH

**Email:** jane.smith@email.com | **Phone:** (555) 987-6543 | **Location:** Austin, TX  
**LinkedIn:** linkedin.com/in/janesmith | **GitHub:** github.com/janesmith

---

## PROFESSIONAL SUMMARY

Software Engineer with 3+ years of experience in web development and cloud technologies. 
Passionate about creating scalable solutions and improving user experiences.

---

## PROFESSIONAL EXPERIENCE

### Software Engineer
**ABC Tech Company** | Austin, TX | June 2021 - Present

- Developed RESTful APIs serving 50,000+ daily users
- Reduced page load time by 35% through code optimization
- Collaborated with cross-functional teams on 10+ projects
- **Technologies Used:** Python, JavaScript, React, AWS

---

## EDUCATION

### Bachelor of Science in Computer Science
**University of Texas** | Austin, TX | May 2021
- **GPA:** 3.7/4.0

---

## SKILLS

**Programming Languages:** Python, JavaScript, TypeScript, SQL  
**Frameworks:** React, Node.js, Django, Express  
**Tools:** Git, Docker, AWS, PostgreSQL
```

### Step 2: Convert to PDF

```bash
python scripts/convert_to_pdf.py demo_resume.md
```

This creates `demo_resume.pdf` with professional formatting.

### Step 3: Review and Customize

Open the PDF and verify:
- ✅ All information is correctly formatted
- ✅ Sections are clearly separated
- ✅ Font and spacing are professional
- ✅ Content is ATS-friendly

## Using with Claude

### Example Conversation

**You:** "I need help creating an ATS-optimized resume. Can you interview me?"

**Claude:** "I'd be happy to help you create an ATS-optimized resume! Let's start with your basic information. What is your full name?"

**You:** "Jane Smith"

**Claude:** "Great! Now, what's your email address?"

[Continue the interview process...]

### After the Interview

Once Claude generates your resume:

1. Claude will save it as `resume.md`
2. Claude will tell you to run: `python scripts/convert_to_pdf.py resume.md`
3. You'll get a professional `resume.pdf`

## Advanced Usage

### Custom Output Name

```bash
python scripts/convert_to_pdf.py resume.md -o jane_smith_resume_2026.pdf
```

### Verbose Mode (See Progress)

```bash
python scripts/convert_to_pdf.py resume.md -v
```

Output:
```
Input file: resume.md
Output file: resume.pdf

Step 1: Loading Markdown file...
  ✓ Loaded 2543 characters
Step 2: Converting Markdown to HTML...
  ✓ Conversion complete
Step 3: Applying ATS-friendly styling...
  ✓ Styling applied
Step 4: Generating PDF...
✓ PDF successfully created: resume.pdf
```

## Tips for Best Results

1. **Follow the Template**: Use the structure provided in SKILL.md
2. **Be Specific**: Include numbers and measurable achievements
3. **Use Keywords**: Include relevant technical terms for your field
4. **Keep It Clean**: Avoid complex formatting in Markdown
5. **Proofread**: Check for typos before converting to PDF

## Troubleshooting

### Error: Required package not found

```bash
pip install -r requirements.txt
```

### PDF Not Generated

1. Check that the Markdown file exists
2. Verify Python 3.8+ is installed
3. Ensure all dependencies are installed
4. Try running with `-v` flag to see detailed errors

## Next Steps

1. Review the full instructions in `SKILL.md`
2. Read the comprehensive documentation in `README.md`
3. Start creating your resume with Claude!

---

**Happy resume building!** 🎉
