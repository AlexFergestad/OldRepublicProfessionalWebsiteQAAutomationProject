"""Page Object Model for Job Details Page"""

from playwright.sync_api import Page, expect

from conftest import page

class JobDetailsPage:
    """Page Object for individual job detail pages"""
    
    def __init__(self, page: Page):
        self.page = page
        
        # Locators
        self.job_title_h2 = page.locator("h2").first
        self.job_description_heading = page.locator("h3").filter(has_text="Job Description").first
        self.job_description_paragraph = page.locator("h3:has-text('Job Description') + p").first
        self.job_requirements_heading = page.locator("h3").filter(has_text="Job Requirements").first
        self.job_requirements_list = page.locator("h3:has-text('Job Requirements') ~ ul").first
        self.application_email = page.get_by_role("link", name="applications@oldrepublicpro.com")
        self.about_orpro_heading = page.locator("h3:has-text('About Old Republic Professional')").first
        self.about_orpro_paragraph = page.locator("h3:has-text('About Old Republic Professional') + p").first

        # Culture section locators
        self.culture_heading = page.locator("h3:has-text('Culture')").first
        self.culture_paragraph = page.locator("h3:has-text('Culture') + p").first
    
    def verify_job_title_visible(self):
        """Verify the job title is visible and return the text"""
        expect(self.job_title_h2).to_be_visible(timeout=10000)
        return self.job_title_h2.text_content().strip()
    
    def verify_job_description_section(self):
        """Verify job description section exists and has content"""
        # Verify heading
        expect(self.job_description_heading).to_be_visible(timeout=5000)
        assert self.job_description_heading.text_content().strip() == "Job Description"
        
        # Verify paragraph
        expect(self.job_description_paragraph).to_be_visible(timeout=5000)
        paragraph_text = self.job_description_paragraph.text_content()
        assert "Old Republic Professional" in paragraph_text
        
        return paragraph_text
    
    def verify_job_requirements_section(self):
        """Verify job requirements section exists"""
        expect(self.job_requirements_heading).to_be_visible(timeout=5000)
        return self.job_requirements_heading.text_content().strip()
    
    def verify_job_requirements_section(self):
        """Verify job requirements paragraphs before the bullet list"""
    
        # 1. Verify heading
        expect(self.job_requirements_heading).to_be_visible(timeout=5000)
        print("✅ Job Requirements heading")
        
        # 2. Get all paragraphs
        paragraphs = self.page.locator(
            "//h3[contains(text(), 'Job Requirements')]/following-sibling::p"
        ).all()
        
        assert len(paragraphs) >= 3, f"Expected at least 3 paragraphs, found {len(paragraphs)}"
        
        # 3. Verify Paragraph 1: Degree
        para1_text = paragraphs[0].text_content()
        assert "Pursuing a bachelor's degree" in para1_text
        assert "2 years of undergraduate" in para1_text
        print(f"✅ Para 1: Bachelor's degree requirement")
        
        # 4. Verify Paragraph 2: Majors
        para2_text = paragraphs[1].text_content()
        assert "Preferred majors" in para2_text
        majors = ["Risk Management", "Business", "Finance", "Accounting"]
        for major in majors:
            assert major in para2_text, f"Missing major: {major}"
        print(f"✅ Para 2: Preferred majors ({', '.join(majors)})")
        
        # 5. Verify Paragraph 3: Intro
        para3_text = paragraphs[2].text_content()
        assert "desired candidate" in para3_text or "characteristics" in para3_text
        print(f"✅ Para 3: Intro to characteristics")
        
        # 6. Verify list
        list_items = self.job_requirements_list.locator("li").all()
        assert len(list_items) == 6, f"Expected 6 items, found {len(list_items)}"
        
        expected_keywords = [
            "Self-starter",
            "organizational skills", 
            "curiosity",
            "communication skills",
            "analytical mind",
            "attention to detail"
        ]
        
        full_list_text = self.job_requirements_list.text_content()
        for keyword in expected_keywords:
            assert keyword in full_list_text, f"Missing keyword: {keyword}"
        
        print(f"✅ List: {len(list_items)} characteristics verified")
        
        return {
            "paragraphs": len(paragraphs),
            "list_items": len(list_items),
            "verified": True
        }
    
    def verify_about_orpro_section(self):
        """Verify About Old Republic Professional section"""
    
        # Verify heading
        expect(self.about_orpro_heading).to_be_visible(timeout=5000)
        heading_text = self.about_orpro_heading.text_content().strip()
        assert heading_text == "About Old Republic Professional", \
            f"Expected 'About Old Republic Professional', got '{heading_text}'"
        print("✅ About Old Republic Professional heading")
        
        # Verify paragraph
        expect(self.about_orpro_paragraph).to_be_visible(timeout=5000)
        para_text = self.about_orpro_paragraph.text_content()
        
        # Verify key information is present
        expected_content = [
            "Old Republic Professional",
            "ORPRO",
            "established in December 1983",
            "Old Republic International Corporation",
            "NYSE: ORI",
            "Fortune 500",
            "Directors and Officers liability insurance",
            "Lawyers Professional liability insurance",
            "40 years"
        ]
        
        for content in expected_content:
            assert content in para_text, f"Missing expected content: '{content}'"
        
        print("✅ About Old Republic Professional paragraph verified")
        print(f"   Content includes: established 1983, NYSE: ORI, Fortune 500, D&O insurance, 40+ years")
        
        return {
            "heading": heading_text,
            "paragraph_length": len(para_text),
            "verified": True
        } 

    def verify_culture_section(self):
        # Verify Culture Heading
        expect(self.culture_heading).to_be_visible(timeout=5000)
        heading_text = self.culture_heading.text_content().strip()
        assert heading_text == "Culture", f"Expected 'Culture', got '{heading_text}'"
        print("✅ Culture heading")
        
        # Verify paragraph
        expect(self.culture_paragraph).to_be_visible(timeout=5000)
        para_text = self.culture_paragraph.text_content()
        
        # Verify culture values
        culture_values = [
            "Work-life balance",
            "collaborative",
            "professional",
            "passionate",
            "open-minded",
            "entrepreneurial"
        ]

        print("\n✅ Culture values:")
        for value in culture_values:
            assert value in para_text, f"Missing culture value: {value}"
            print(f"   ✓ {value}")
        
        # Verify employee benefits
        expected_benefits = [
            "competitive wages",
            "BCBS medical",
            "FSA/HSA",
            "long-term disability",
            "dental",
            "vision",
            "fertility and family building benefits",
            "Employee Assistance Program",
            "paid time off",
            "PTO",
            "paid holidays",
            "Paid Leave of Absence",
            "401(k)",
            "Profit-Sharing Plan",
            "529 Education Savings Plan",
            "Gym Network 360",
            "pet insurance",
            "commuting reimbursement",
            "tuition reimbursement"
        ]
        
        found_benefits = []
        missing_benefits = []
        
        for benefit in expected_benefits:
            if benefit in para_text:
                found_benefits.append(benefit)
            else:
                missing_benefits.append(benefit)
        
        print(f"\n✅ Employee benefits ({len(found_benefits)}/{len(expected_benefits)}):")
        for benefit in found_benefits[:10]:  # Show first 10
            print(f"   ✓ {benefit}")
        if len(found_benefits) > 10:
            print(f"   ... and {len(found_benefits) - 10} more")
        
        # Verify all benefits are present
        assert len(found_benefits) == len(expected_benefits), \
            f"Expected all {len(expected_benefits)} benefits, found {len(found_benefits)}. Missing: {missing_benefits}"
        
        if missing_benefits:
            print(f"\n⚠️  Missing benefits: {', '.join(missing_benefits)}")
        
        return {
            "heading": heading_text,
            "culture_values": len(culture_values),
            "benefits_found": len(found_benefits),
            "benefits_total": len(expected_benefits),
            "paragraph_length": len(para_text),
            "verified": True
        }
    

    def verify_application_email_visible(self):
        """Verify the application email link is visible"""
        expect(self.application_email).to_be_visible(timeout=5000)
        href = self.application_email.get_attribute("href")
        assert "mailto:applications@oldrepublicpro.com" in href
        return href
