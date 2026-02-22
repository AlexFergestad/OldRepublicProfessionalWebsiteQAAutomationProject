from playwright.sync_api import Page, expect


class CareersPage:
    """Page Object for the Careers page"""

    def __init__(self, page: Page, base_url: str):
            self.page = page
            self.base_url = base_url
            self.url = f"{base_url}/careers"
            
            # Locators for careers page elements
            self.underwriting_analyst_intern_link = page.get_by_role(
                "link", 
                name="Underwriting Analyst Intern"
            ).first
            self.linkedin_share_button = page.get_by_role("button", name="Share").first
            self.careers_heading = page.get_by_role("heading", level=1).first
        
    def navigate(self):
            """Navigate to the careers page"""
            self.page.goto(self.url)
            self.page.wait_for_load_state("networkidle")
        
    def click_underwriting_analyst_intern_job(self):
            """Click on the Underwriting Analyst Intern job listing"""
            expect(self.underwriting_analyst_intern_link).to_be_visible(timeout=5000)
            self.underwriting_analyst_intern_link.click()
            self.page.wait_for_load_state("networkidle")
            self.page.wait_for_timeout(1000)