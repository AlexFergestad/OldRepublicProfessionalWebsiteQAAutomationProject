

def navigate_to_epl_page(self):
        self.page.wait_for_timeout(1000)
        self.epl_page.hover()
        self.epl_page.click()
        self.page.wait_for_load_state("networkidle")