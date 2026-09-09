from playwright.sync_api import Page, expect


class Public_Company_Lead_Side_A:

    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.base_url = base_url
        self.header_nav = page.locator("#hs_menu_wrapper_module_1527184808535133_mjfm_header_main_menu")
        
        self.lead_side_a_page = self.header_nav.get_by_role("menuitem", name="Lead Side-A Only")
        self.lead_side_a_page_title = page.locator("h1").filter(has_text="A-Sure")
        self.download_lead_side_a = page.get_by_role("link", name="Download Lead Side-A").filter(has_text="Sell Sheet")
        self.download_policy_forms = page.locator("a:has-text(\"Download Policy Forms\")")

    def navigate_to_lead_side_a_page(self):
        self.page.wait_for_timeout(1000)
        self.lead_side_a_page.hover()
        self.lead_side_a_page.click()
        self.page.wait_for_load_state("networkidle")

    def verify_lead_side_a_page_title_and_headers(self):
        expect(self.lead_side_a_page_title).to_be_visible(timeout=5000)

    def verify_download_buttons(self):
        expect(self.download_lead_side_a).to_be_visible(timeout=5000)
        self.download_lead_side_a.click()
        self.page.wait_for_load_state("networkidle")

        # self.page.go_back()

        expect(self.download_policy_forms).to_be_visible(timeout=5000)
        self.download_policy_forms.click()
        # self.page.go_back()





