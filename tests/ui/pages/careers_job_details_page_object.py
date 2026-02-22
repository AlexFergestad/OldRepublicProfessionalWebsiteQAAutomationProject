"""Page Object Model for Job Details Page"""

from playwright.sync_api import Page, expect

class JobDetailsPage:
    """Page Object for individual job detail pages"""
    
    def __init__(self, page: Page):
        self.page = page
        
        # Locators
        self.job_title_h2 = page.locator("h2").first
        self.job_description_heading = page.locator("h3").filter(has_text="Job Description").first
        self.job_description_paragraph = page.locator("h3:has-text('Job Description') + p").first
        self.job_requirements_heading = page.locator("h3").filter(has_text="Job Requirements").first
        self.application_email = page.get_by_role("link", name="applications@oldrepublicpro.com")
    
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
    
    def verify_job_requirements_list(self):
        """Verify the job requirements list is visible and has items"""
        requirements_list = self.page.locator("h3:has-text('Job Requirements') + ul").first
        expect(requirements_list).to_be_visible(timeout=5000)
        items = requirements_list.locator("li")
        expect(items).to_have_count_greater_than(0, timeout=5000)
        return [item.text_content().strip() for item in items.all()]
    
    def verify_application_email_visible(self):
        """Verify the application email link is visible"""
        expect(self.application_email).to_be_visible(timeout=5000)
        href = self.application_email.get_attribute("href")
        assert "mailto:applications@oldrepublicpro.com" in href
        return href
