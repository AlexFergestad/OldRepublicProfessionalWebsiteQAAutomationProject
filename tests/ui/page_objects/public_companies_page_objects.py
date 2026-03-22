from playwright.sync_api import Page, expect

class Public_Company_Liability_Overview:
    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.base_url = base_url
        self.url = f"{base_url}/business-insurance-public-company"
        
        # Text Locators
        self.page_heading = page.locator("h1").first
        self.overview_paragraphs = page.locator("div.constrain > p")
    
    def navigate(self):
        """Navigate to the Public Companies page"""
        self.page.goto(self.url)
        self.page.wait_for_load_state("networkidle")
    
    def verify_page_heading(self):
        """Verify the main page heading"""
        expect(self.page_heading).to_be_visible(timeout=5000)
        expect(self.page_heading).to_have_text("Public-Company Liability Overview")
        
        heading_text = self.page_heading.text_content()
        print(f"✅ Heading: {heading_text}")
        
        return heading_text
    
    def verify_overview_paragraph1(self):
        """Verify overview section paragraphs contain key information"""
        # Verify we have paragraphs
        paragraphs = self.overview_paragraphs.all()
        assert len(paragraphs) >= 4, f"Expected at least 4 paragraphs, found {len(paragraphs)}"
        
        # Get first paragraph
        first_para = self.overview_paragraphs.nth(0)
        expect(first_para).to_be_visible(timeout=5000)

        # Grab text once — used for both assertions and return value
        content = first_para.text_content()
        
        # Verify key facts in first paragraph
        key_facts = [
            "Directors and Officers liability insurance",
            "40 years",
            "NASDAQ 100 Index",
            "60 percent of the NASDAQ Biotechnology Index"
        ]
        
        for fact in key_facts:
            assert fact in content, (
                f"\nKey fact not found: '{fact}'\n"
                f"Content says instead:\n  '{content[:200]}...'"
            )
        
        print(f"✅ Overview paragraphs verified ({len(paragraphs)} paragraphs, {len(key_facts)} key facts)")
        
        return paragraphs

    def verify_overview_paragraph2(self):
        """Verify the second overview paragraph contains key information"""
        second_para = self.overview_paragraphs.nth(1)
        expect(second_para).to_be_visible(timeout=5000)
        
        # Grab text once — used for both assertions and return value
        content = second_para.text_content()

        # Checks for key concepts, not exact wording, this is best practice
        key_facts = [
            "Corporate directors and officers",
            "ever-expanding array of risk",
            "insurance carrier partner"
        ]

        for fact in key_facts:
            assert fact in content, (
                f"\nKey fact not found: '{fact}'\n"
                f"Content says instead:\n  '{content[:200]}...'"
            )

        print(f"✅ Second overview paragraph verified with key facts")
        
        return second_para.text_content()

    def verify_overview_paragraph3(self):
        """Verify the third overview paragraph contains key information"""
        third_para = self.overview_paragraphs.nth(2)
        expect(third_para).to_be_visible(timeout=5000)
        
        # Grab text once — used for both assertions and return value
        content = third_para.text_content()

        # Checks for key concepts, not exact wording, this is best practice
        # Key facts: short, meaningful phrases
        key_facts = [
            "20 years' experience",
            "D&O underwriting",
            "initial public offerings",
            "bankruptcies",
            "turnarounds",
            "public and private company risks"
        ]

        for fact in key_facts:
            assert fact in content, (
                f"\nKey fact not found: '{fact}'\n"
                f"Content says instead:\n  '{content[:200]}...'"
            )


        print(f"✅ Third overview paragraph verified with key facts")
        
        return third_para.text_content()

    def verify_last_part_of_paragraph(self):
    
    def verify_heading_and_paragraphs(self):
        """Verify both heading and paragraphs"""
        self.verify_page_heading()
        self.verify_overview_paragraph1()
        self.verify_overview_paragraph2()
        self.verify_overview_paragraph3()
        
        return True

