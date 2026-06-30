import re

from playwright.sync_api import Page, expect

class Public_Company_Products:
    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.base_url = base_url
        self.productsPage = page.locator("#hs_menu_wrapper_module_1527184808535133_mjfm_header_main_menu").get_by_role("menuitem", name="Products")
        self.url = f"{base_url}/business-insurance-public-company/directors-and-officers-liability/products"
        self.products_h1 = page.locator("h1")
        self.primary_tradtional_d_and_o_title = page.locator("h3").first
        self.excess_liability_title = page.locator("h3").filter(has_text=re.compile("excess liability", re.IGNORECASE)).first
        self.lead_side_a_title = page.locator("h3").filter(has_text=re.compile(r"lead side[\s-]a", re.IGNORECASE)).first
        self.excess_side_a_title = page.locator("h3").filter(has_text=re.compile(r"excess side[\s-]a", re.IGNORECASE)).first

    def navigate_to_products_page(self):
        self.productsPage.click()
        self.page.wait_for_load_state("networkidle")

    def verify_products_h1(self):
        expect(self.products_h1).to_have_text("Public Company Directors & Officers Liability Underwriting Products")
        expect(self.products_h1).to_be_visible()

    def verify_primary_traditional_d_and_o_bullet_point(self):
        expect(self.primary_tradtional_d_and_o_title).to_contain_text("traditional")
        expect(self.primary_tradtional_d_and_o_title).to_be_visible()

        # Scope to the Primary D&O section to avoid matching other sections
        primary_do_links = self.page.locator("h3").filter(has_text="traditional").locator("xpath=following-sibling::ul[1]")
        expect(primary_do_links.get_by_role("link", name="Product Highlights (PDF)")).to_be_visible()
        expect(primary_do_links.get_by_role("link", name="Policy form ORUG-95")).to_be_visible()
    
    def verify_excess_liability_bullet_point(self):
        expect(self.excess_liability_title).to_contain_text("Excess Liability")
        expect(self.excess_liability_title).to_be_visible()

        # Scope to the Excess Liability section to avoid matching other sections
        self.excess_liability_links = self.page.locator("h3").filter(has_text=re.compile("excess liability", re.IGNORECASE)).locator("xpath=following-sibling::ul[1]")
        expect(self.excess_liability_links.get_by_role("link", name="Product Highlights (PDF)")).to_be_visible()
        expect(self.excess_liability_links.get_by_role("link", name="Policy form ORUG-91")).to_be_visible()
        expect(self.excess_liability_links.get_by_role("link", name="Excess Plus Highlights (PDF)")).to_be_visible()     
        expect(self.excess_liability_links.get_by_role("link", name="Excess Plus endorsement")).to_be_visible()
    
    def verify_lead_side_a_bullet_point(self):
        expect(self.lead_side_a_title).to_contain_text("Lead Side-A")
        expect(self.lead_side_a_title).to_be_visible()

        # Scope to the Lead Side A section to avoid matching other sections
        self.lead_side_a_links = self.page.locator("h3").filter(has_text=re.compile(r"lead side[\s-]a", re.IGNORECASE)).locator("xpath=following-sibling::ul[1]")
        expect(self.lead_side_a_links.get_by_role("link", name="Product Highlights (PDF)")).to_be_visible()
        expect(self.lead_side_a_links.get_by_role("link", name="Policy form ORUG-93")).to_be_visible()

    def verify_excess_side_a_bullet_point(self):
        expect(self.excess_side_a_title).to_contain_text("Excess Side-A")
        expect(self.excess_side_a_title).to_be_visible()

        self.excess_side_a_links = self.page.locator("h3").filter(has_text=re.compile(r"excess side[\s-]a", re.IGNORECASE)).locator("xpath=following-sibling::ul[1]")
        expect(self.excess_side_a_links.get_by_role("link", name="Product Highlights (PDF)")).to_be_visible()
        expect(self.excess_side_a_links.get_by_role("link", name="Policy form ORUG-92")).to_be_visible()
    
    