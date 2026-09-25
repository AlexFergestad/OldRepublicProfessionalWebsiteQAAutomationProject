from playwright.sync_api import Page, expect

from conftest import page


class Public_Company_Excess_Side_A:

    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.base_url = base_url
        self.header_nav = page.locator("#hs_menu_wrapper_module_1527184808535133_mjfm_header_main_menu")

        self.excess_side_a_page = self.header_nav.get_by_role("menuitem", name="Excess Side-A Only")
        self.title = page.locator("h1")
        self.policy_features = page.locator("h2").filter(has_text="Policy features (ORUG-92):")
        self.capacity = page.locator("p").filter(has_text="Capacity:")
        self.eligibility = page.locator("strong").filter(has_text="Eligibility:")

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
        expect(self.policy_features).to_contain_text("Policy features (ORUG-92):")
    
        policy_features_list = self.policy_features.locator("xpath=following-sibling::ul[1]")
        expect(policy_features_list.locator("li")).to_have_count(4)

        


