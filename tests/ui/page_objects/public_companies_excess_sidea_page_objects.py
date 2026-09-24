from playwright.sync_api import Page, expect


class Public_Company_Excess_Side_A:

    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.base_url = base_url
        self.header_nav = page.locator("#hs_menu_wrapper_module_1527184808535133_mjfm_header_main_menu")

        self.excess_side_a_page = self.header_nav.get_by_role("menuitem", name="Excess Side-A Only")
        self.title = page.locator("h1")
        self.policy_features = page.locator("h2:has-text('Policy Features (ORUG-92):')")

    def navigate_to_excess_side_a_page(self):
        self.page.wait_for_timeout(1000)
        self.excess_side_a_page.hover()
        self.excess_side_a_page.click()
        self.page.wait_for_load_state("networkidle")

    def verify_page_title_and_header(self):
        # Verifies that the page has the correct title and header
        expect(self.page).to_have_title("Excess Side-A D&O | Public Company D&O | Old Republic Professional")
        expect(self.page.locator("h1")).to_contain_text("Excess Side-A")

    def verify_policy_features_bullet_points(self):
        # Verifies that the page has the correct policy features bullet point list, capacity, and eligibility text
        expect(self.policy_features).to_contain_text("Policy Features (ORUG-92):")
        expect(self.page.locator("ul li")).to_have_count(5)
        expect(self.page.locator("ul li").nth(0)).to_contain_text("One-page streamlined")
        expect(self.page.locator("ul li").nth(1)).to_contain_text("Independent Director Liability")
        expect(self.page.locator("ul li").nth(2)).to_contain_text("DIC into DIC feature")
        expect(self.page.locator("ul li").nth(3)).to_contain_text("Double reinstatement")


