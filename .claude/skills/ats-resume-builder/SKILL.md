---
name: ATS Resume Builder
description: Interview users to collect professional information, generate ATS-optimized resumes in Markdown format, and convert them to PDF.
version: 1.0.0
author: Claude AI
---

# ATS Resume Builder - Claude AI Skill

## Purpose
This skill enables Claude AI to:
1. Conduct structured interviews to gather professional information
2. Parse existing resumes to extract relevant data
3. Generate ATS (Applicant Tracking System) optimized resumes
4. Convert Markdown resumes to PDF format for download

## Workflow

### Option 1: Interview Mode
When a user requests to create a resume from scratch:

1. **Introduction**
   - Greet the user and explain the resume building process
   - Offer to either conduct an interview or parse an existing resume

2. **Structured Interview**
   Collect the following information systematically:
   
   **Personal Information:**
   - Full Name
   - Email Address
   - Phone Number
   - Location (City, State/Province, Country)
   - LinkedIn Profile (optional)
   - Portfolio/Website (optional)
   - GitHub Profile (if applicable)

   **Professional Summary:**
   - Career objective or professional summary
   - Years of experience
   - Key areas of expertise

   **Work Experience:**
   For each position (most recent first):
   - Job Title
   - Company Name
   - Location
   - Start Date and End Date (or "Present")
   - Key Responsibilities (3-5 bullet points)
   - Achievements with quantifiable results
   - Technologies/tools used

   **Education:**
   For each degree/certification:
   - Degree/Certification Name
   - Institution Name
   - Location
   - Graduation Date (or Expected Date)
   - GPA (if recent graduate and above 3.5)
   - Relevant Coursework (optional)

   **Skills:**
   - Technical Skills (programming languages, tools, frameworks)
   - Soft Skills (leadership, communication, etc.)
   - Certifications
   - Languages

   **Projects (optional):**
   For each project:
   - Project Name
   - Description
   - Technologies Used
   - Link to Project/Demo

   **Awards and Achievements (optional):**
   - List any relevant awards, publications, or notable achievements

3. **Confirm and Clarify**
   - Review collected information with the user
   - Ask clarifying questions where needed
   - Confirm all details are accurate

### Option 2: Resume Parsing Mode
When a user provides an existing resume (either as text, document, or resume.md file):

1. **Read the Resume File**
   - If user provides a resume.md file, read and parse the content
   - If user shares text/document, extract the information
   - Identify all sections: contact info, summary, experience, education, skills, etc.

2. **Analyze for ATS Compatibility**
   - Check formatting (single column, standard headers, simple bullets)
   - Verify quantifiable achievements in work experience
   - Assess keyword usage and relevance
   - Identify missing information (dates, locations, metrics)
   - Review action verbs and impact statements
   
3. **Present Analysis Results**
   Show the user:
   - ✅ **Strengths:** What's already ATS-optimized
   - ⚠️ **Issues:** Problems that need fixing
   - 💡 **Suggestions:** Specific improvements
   
   Example feedback format:
   ```
   **ATS Analysis Results:**
   
   ✅ Strengths:
   - Clean, simple formatting
   - Standard section headers
   - Contact information complete
   
   ⚠️ Issues Found:
   - Missing quantifiable metrics in 8/12 bullets
   - Weak action verbs ("helped", "worked on", "was responsible for")
   - No specific technologies mentioned in 2 positions
   - Education section missing GPA/coursework
   
   💡 Suggested Improvements:
   1. Add metrics: "How many users/customers did this impact?"
   2. Replace weak verbs with: Developed, Implemented, Led, Optimized
   3. Specify technologies: Instead of "various tools", list actual tech stack
   4. Add quantifiable achievements for each role
   ```

4. **Gather Missing Information**
   - Ask targeted questions to fill gaps
   - Request quantifiable metrics for achievements
   - Clarify technologies and tools used
   - Get specific dates, locations, or other missing details
   
   Example questions:
   ```
   "For your role at TechCorp where you mention 'improved performance', 
   can you tell me:
   - What specific metric improved? (response time, throughput, etc.)
   - By what percentage or amount?
   - How many users benefited from this improvement?"
   ```

5. **Generate Optimized Version**
   - Create ATS-optimized version with improvements
   - Maintain user's original information and achievements
   - Enhance with proper formatting, keywords, and metrics
   - Present side-by-side comparison if helpful

6. **Iterative Refinement**
   - Allow user to request specific changes
   - Adjust emphasis on certain skills or experiences
   - Tailor for specific job applications if needed

### Option 3: Resume.md File Analysis Workflow

When user has an existing `resume.md` file:

1. **File Input**
   ```
   User: "I have a resume.md file. Can you analyze and optimize it for ATS?"
   Claude: "I'll analyze your resume.md file for ATS compatibility. Please share 
   the file content or let me know the file path."
   ```

2. **Read and Parse**
   - Read the complete resume.md file
   - Extract all sections systematically
   - Identify current structure and formatting

3. **Comprehensive Analysis**
   Evaluate across multiple dimensions:
   
   **Format Check:**
   - Single-column layout ✓/✗
   - Standard section headers ✓/✗
   - Simple bullet points ✓/✗
   - No tables/columns/graphics ✓/✗
   - Consistent date format ✓/✗
   
   **Content Quality:**
   - Action verbs used ✓/✗
   - Quantifiable metrics ✓/✗
   - Specific technologies mentioned ✓/✗
   - Business impact stated ✓/✗
   - Complete information (dates, locations) ✓/✗
   
   **ATS Optimization:**
   - Keywords present ✓/✗
   - Standard job titles ✓/✗
   - Proper contact info ✓/✗
   - Professional summary effective ✓/✗

4. **Generate Optimization Report**
   ```
   **Resume Analysis Report**
   
   Overall ATS Score: 65/100
   
   📊 Breakdown:
   - Format: 85/100 (Good structure, minor issues)
   - Content: 55/100 (Needs more metrics and impact)
   - Keywords: 60/100 (Could be improved)
   - Completeness: 70/100 (Missing some details)
   
   🔴 Critical Issues (Must Fix):
   1. 10 out of 15 bullets lack quantifiable metrics
   2. 3 positions missing specific technologies used
   3. Professional summary is too generic
   
   🟡 Improvements (Should Fix):
   1. Replace 5 weak action verbs with stronger alternatives
   2. Add more industry-specific keywords
   3. Include months in date ranges (not just years)
   
   🟢 Good Practices (Keep):
   1. Clean, single-column layout
   2. Standard section headers
   3. Complete contact information
   ```

5. **Interactive Optimization**
   - Ask clarifying questions for each issue
   - Gather additional information needed
   - Get user approval before making changes

6. **Generate Optimized resume.md**
   - Create new version: `resume_optimized.md`
   - Or overwrite original with user permission
   - Maintain all original achievements, just enhanced

7. **Provide Comparison**
   - Show before/after for key sections
   - Highlight improvements made
   - Explain reasoning for changes

## ATS Optimization Guidelines

When generating the resume, follow these best practices:

### Format Requirements:
- Use simple, clean Markdown formatting
- Use standard section headers (PROFESSIONAL EXPERIENCE, EDUCATION, SKILLS)
- Avoid tables, graphics, or complex formatting
- Use bullet points (hyphens) for lists
- Include relevant keywords from the target industry/role

### Content Best Practices:
- **Use Action Verbs**: Start bullet points with strong action verbs (Developed, Implemented, Managed, Led, etc.)
- **Quantify Achievements**: Include numbers, percentages, and measurable outcomes
- **Keywords**: Incorporate industry-specific keywords and technical terms
- **Relevance**: Prioritize relevant experience and skills
- **Consistency**: Use consistent date formats (e.g., "January 2020 - Present")
- **Length**: Keep it concise (1-2 pages for most professionals)

### ATS-Friendly Practices:
- Use standard job titles
- Spell out acronyms at least once
- Include both spelled-out and abbreviated versions of key terms
- Use standard fonts (in PDF conversion)
- Avoid headers/footers for critical information
- Use simple bullet points, not special characters

## Resume Template (Markdown)

```markdown
# [FULL NAME]

**Email:** [email@example.com] | **Phone:** [(123) 456-7890] | **Location:** [City, State]  
**LinkedIn:** [linkedin.com/in/profile] | **GitHub:** [github.com/username] | **Portfolio:** [portfolio.com]

---

## PROFESSIONAL SUMMARY

[2-3 sentences highlighting years of experience, key expertise, and career focus. Include relevant keywords for the target role.]

---

## PROFESSIONAL EXPERIENCE

### [Job Title]
**[Company Name]** | [City, State] | [Start Date] - [End Date]

- [Action verb] [achievement/responsibility with quantifiable results]
- [Action verb] [achievement/responsibility with quantifiable results]
- [Action verb] [achievement/responsibility with quantifiable results]
- [Action verb] [achievement/responsibility with quantifiable results]
- **Technologies Used:** [List relevant technologies, tools, frameworks]

### [Previous Job Title]
**[Previous Company Name]** | [City, State] | [Start Date] - [End Date]

- [Action verb] [achievement/responsibility with quantifiable results]
- [Action verb] [achievement/responsibility with quantifiable results]
- [Action verb] [achievement/responsibility with quantifiable results]
- **Technologies Used:** [List relevant technologies, tools, frameworks]

---

## EDUCATION

### [Degree Name]
**[University/Institution Name]** | [City, State] | [Graduation Date]
- **GPA:** [X.XX/4.0] (if applicable)
- **Relevant Coursework:** [Course 1, Course 2, Course 3]

---

## SKILLS

**Programming Languages:** [Language 1, Language 2, Language 3, etc.]  
**Frameworks & Libraries:** [Framework 1, Framework 2, Framework 3, etc.]  
**Tools & Technologies:** [Tool 1, Tool 2, Tool 3, etc.]  
**Databases:** [Database 1, Database 2, etc.]  
**Soft Skills:** [Skill 1, Skill 2, Skill 3, etc.]  
**Certifications:** [Certification 1, Certification 2, etc.]

---

## PROJECTS

### [Project Name]
- **Description:** [Brief description of the project and its impact]
- **Technologies:** [Technologies used]
- **Link:** [GitHub/Demo link]

### [Another Project Name]
- **Description:** [Brief description of the project and its impact]
- **Technologies:** [Technologies used]
- **Link:** [GitHub/Demo link]

---

## AWARDS & ACHIEVEMENTS

- [Award/Achievement 1 with year]
- [Award/Achievement 2 with year]
- [Award/Achievement 3 with year]
```

## Generating the Resume

1. **Create the Markdown File**
   - After collecting all information, generate a complete resume following the template above
   - Customize sections based on what's relevant for the user
   - Ensure all content is ATS-optimized
   - Save the resume as `resume.md`

2. **Present to User**
   - Show the generated Markdown resume to the user
   - Ask for feedback and make any requested changes
   - Iterate until the user is satisfied

3. **Generate PDF**
   - Once the user approves the resume, inform them that you'll convert it to PDF
   - Execute the PDF conversion script from the project root:
   ```bash
   python .claude/skills/ats-resume-builder/scripts/convert_to_pdf.py resume.md -o resume.pdf
   ```
   - Note: Run this command from your project root directory where the resume.md file is located
   - Inform the user that their PDF resume is ready for download

## PDF Conversion

The skill includes a Python script (`scripts/convert_to_pdf.py`) that converts the Markdown resume to a professionally formatted PDF.

### Usage:
```bash
python .claude/skills/ats-resume-builder/scripts/convert_to_pdf.py <input_markdown_file> -o <output_pdf_file>
```

### Features:
- Clean, professional formatting
- ATS-friendly fonts and layout
- Proper spacing and margins
- Header and section styling

## Best Practices

1. **Be Conversational**: Make the interview process feel natural, not like filling out a form
2. **Ask Follow-up Questions**: Dig deeper to help users articulate their achievements
3. **Provide Examples**: Help users understand what makes a strong bullet point
4. **Focus on Impact**: Encourage users to highlight results and impact, not just tasks
5. **Tailor Content**: Ask about the target role/industry to customize keyword usage
6. **Review Carefully**: Always review the generated resume with the user before creating the PDF

## Tips for Success

- **One Section at a Time**: Don't overwhelm users; collect information section by section
- **Save Progress**: Periodically summarize what's been collected
- **Be Flexible**: Adapt the interview flow based on the user's background
- **Quality over Quantity**: Focus on strong, relevant content rather than filling space
- **Test ATS Compatibility**: Ensure the final PDF can be properly parsed by ATS systems

## Error Handling

- If the PDF conversion fails, provide the Markdown file to the user as a backup
- If information is missing, make reasonable assumptions or ask the user
- If the user is unsure about something, offer to skip it or come back to it later

## Dependencies

The PDF conversion script requires Python 3.8+ and the following packages (see `requirements.txt`):
- markdown>=3.4.0
- weasyprint>=68.0 (security patched)
- Pillow>=10.2.0 (security patched)
- cffi>=1.15.0

Install with:
```bash
pip install -r .claude/skills/ats-resume-builder/requirements.txt
```

## Version History

- **v1.0.0** (2024-01-21): Initial release with interview mode, parsing mode, and PDF conversion
