
from playwright.sync_api import Page, expect


class Employment_Practices_Liability:
        def __init__(self, page: Page, base_url: str):
                self.page = page
                self.base_url = base_url
                self.header_nav = page.locator("#hs_menu_wrapper_module_1527184808535133_mjfm_header_main_menu")
                self.epl_page = self.header_nav.get_by_role("menuitem", name="Employment-Practices Liability")
                self.epl_applications_title = page.locator("h2", has_text="EPL Applications")


        def navigate_to_epl_page(self):
                self.page.wait_for_timeout(1000)
                self.epl_page.hover()
                self.epl_page.click()
                self.page.wait_for_load_state("networkidle")

        def verify_page_title_and_headers(self):
                # Verifies that the page has the correct title and headers
                expect(self.page).to_have_title("EPL | Employment-Practices Liability | Old Republic Professional")
                expect(self.page.locator("h1")).to_have_text("Employment-Practices Liability")

        def verify_applications_and_forms_title_and_text(self):
                row = self.page.locator("tr").filter(has_text="ORUG-103")

                expect(row).to_contain_text("ORUG-103")
                expect(row).to_contain_text("New-Business Application")
                expect(row).to_contain_text("1/2017")
                expect(row.get_by_role("link", name="Word Processor")).to_be_visible()
                expect(row.get_by_role("link", name="PDF")).to_be_visible()

                # Verifies the links for the Word Processor and PDF versions of the application
                self.verify_download_link(
                        row.get_by_role("link", name="Word Processor"),
                        "https://www.orprofessional.com/hubfs/documents/epl/ORUG-103-APP.docx"
                )
                self.verify_download_link(
                        row.get_by_role("link", name="PDF"),
                        "https://www.orprofessional.com/hubfs/documents/epl/ORUG-103-APP.pdf"
                )

