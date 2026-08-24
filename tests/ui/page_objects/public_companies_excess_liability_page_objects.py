import re

from playwright.sync_api import Page, expect


class Public_Company_Excess_Liability:
    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.base_url = base_url
        self.header_nav = page.locator("#hs_menu_wrapper_module_1527184808535133_mjfm_header_main_menu")
        self.excess_liability_page = self.header_nav.get_by_role("menuitem", name="Excess Liability")
        self.policy_features = page.locator("h2").filter(has_text="Policy features")
        self.policy_features_list = page.locator("h2").filter(has_text="Policy features").locator("xpath=following-sibling::ul[1]")

        self.h1 = page.locator("h1").first
        self.h1_paragraph = page.locator("h1 + p")
        self.capacity = page.locator("p").filter(has_text="Capacity:")
        self.attachment = page.locator("p").filter(has_text="Attachment:")
        self.eligibility = page.locator("p").filter(has_text="Eligibility:")
        self.download_excess_do_sell_sheet = page.get_by_role("link", name="Download Excess D&O Sell Sheet")
        self.our_excess_plus_endorsement = page.get_by_role("link", name="Our Excess Plus™ Endorsement")
        self.our_excess_plus_endorsement_paragraph = page.locator("h3").filter(has_text="Our Excess Plus™ Endorsement").locator("xpath=following-sibling::p[1]")
        self.how_excess_plus_works = page.locator("h4").filter(has_text="How Excess Plus™ Works")        
        self.how_excess_plus_works_list = page.locator("h4").filter(has_text="How Excess Plus™ Works:").locator("xpath=following-sibling::ul[1]")
        self.excess_plus_benefits = page.locator("h4").filter(has_text="Excess Plus™ Benefits")
        self.excess_plus_benefits_list = page.locator("h4").filter(has_text="Excess Plus™ Benefits:").locator("xpath=following-sibling::ul[1]")
        self.download_excess_plus_sell_sheet = page.get_by_role("link", name="Download Excess Plus™ Sell Sheet")

    def navigate_to_excess_liability_page(self):
        self.excess_liability_page.click()
        self.page.wait_for_load_state("networkidle")

    def verify_excess_liability_h1(self):
        expect(self.h1).to_be_visible(timeout=5000)
        self.page.wait_for_load_state("networkidle")

    def verify_h1_paragraph(self):
        expect(self.h1_paragraph).to_be_visible(timeout=5000)
        self.page.wait_for_load_state("networkidle")

    def verify_policy_features(self):
        expect(self.policy_features).to_be_visible(timeout=5000)

        bullet_point_texts = [
            "One-page",
            "Market-leading erosion language",
            "Shareholder Derivative Demand Investigations",
            "Excess Flex™"
        ]

        for text in bullet_point_texts:
            expect(self.policy_features_list).to_contain_text(text)


    def verify_capacity_attachment_eligibility_and_download_button(self):
        expect(self.capacity).to_be_visible(timeout=5000)
        expect(self.attachment).to_be_visible(timeout=5000)
        expect(self.eligibility).to_be_visible(timeout=5000)
        expect(self.download_excess_do_sell_sheet).to_be_visible(timeout=5000)
        self.download_excess_do_sell_sheet.click()

        self.page.wait_for_timeout(2000)

        with self.page.context.expect_page() as new_page_info:
            self.download_excess_do_sell_sheet.click()

        new_page = new_page_info.value
        new_page.wait_for_load_state("networkidle")

        expected_url = "https://www.oldrepublicpro.com/hubfs/2025%20Sell%20Sheets/Excess%20Mgmt%20Liability%20Sell%20Sheet.pdf"
        assert new_page.url == expected_url, f"Expected URL: {expected_url}, but got: {new_page.url}"

    def verify_our_excess_plus_endorsement_link_and_paragraph(self):
        expect(self.our_excess_plus_endorsement).to_be_visible(timeout=5000)
        expect(self.our_excess_plus_endorsement_paragraph).to_be_visible(timeout=5000)

    def verify_how_excess_plus_works_and_bullet_points(self):
        expect(self.how_excess_plus_works).to_be_visible(timeout=5000)
        expect(self.how_excess_plus_works_list).to_be_visible(timeout=5000)
        self.page.wait_for_load_state("networkidle")

    def verify_excess_plus_benefits_and_bullet_points(self):
        expect(self.excess_plus_benefits).to_be_visible(timeout=5000)
        expect(self.excess_plus_benefits_list).to_be_visible(timeout=5000)
        self.page.wait_for_load_state("networkidle")

    def verify_download_excess_plus_sell_sheet_button(self):
        expect(self.download_excess_plus_sell_sheet).to_be_visible(timeout=5000)
        expect(self.download_excess_plus_sell_sheet).to_be_enabled(timeout=5000)

        expected_url = "https://www.oldrepublicpro.com/hubfs/2025%20Sell%20Sheets/Excess%20PLUS%20Solutions.pdf"

        with self.page.context.expect_page() as new_page_info:
            self.download_excess_plus_sell_sheet.click()

        new_page = new_page_info.value
        new_page.wait_for_load_state("networkidle")

        assert new_page.url == expected_url, f"Expected URL: {expected_url}, but got: {new_page.url}"

    def get_performance_metrics(self):
        # Scroll to trigger LCP finalization
        self.page.evaluate("window.scrollBy(0, 100)")
        self.page.wait_for_timeout(500)
    
        metrics = self.page.evaluate("""() => {
            const nav = performance.getEntriesByType('navigation')[0];
            const paint = performance.getEntriesByType('paint');
            const fcp = paint.find(p => p.name === 'first-contentful-paint');
            const lcp = performance.getEntriesByType('largest-contentful-paint').slice(-1)[0];
            const cls = performance.getEntriesByType('layout-shift').reduce((sum, e) => sum + e.value, 0);
            return {
                load_time: nav ? nav.loadEventEnd - nav.startTime : null,
                first_contentful_paint: fcp ? fcp.startTime : null,
                largest_contentful_paint: lcp ? lcp.startTime : null,
                cumulative_layout_shift: cls
            };
        }""")
    
        print(f"\n📊 Performance Metrics — Public Companies D&O Page")
        print(f"   Load Time:                  {metrics['load_time']:.0f}ms")
        print(f"   First Contentful Paint:     {metrics['first_contentful_paint']:.0f}ms")
        print(f"   Largest Contentful Paint:   {f'{metrics["largest_contentful_paint"]:.0f}ms' if metrics['largest_contentful_paint'] is not None else 'N/A (headless)'}")
        print(f"   Cumulative Layout Shift:    {metrics['cumulative_layout_shift']:.4f}")
    
        return metrics