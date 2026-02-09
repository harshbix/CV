from playwright.sync_api import sync_playwright
import os

def generate_pdf():
    html_path = os.path.abspath("index.html")
    pdf_path = os.path.abspath("CV.pdf")
    
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(f"file:///{html_path}")
        page.pdf(path=pdf_path, format="A4", print_background=True)
        browser.close()
        print(f"PDF generated at: {pdf_path}")

if __name__ == "__main__":
    generate_pdf()
