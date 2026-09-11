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


        expect(self.download_policy_forms).to_be_visible(timeout=5000)
        self.download_policy_forms.click()

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



