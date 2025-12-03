from playwright.sync_api import sync_playwright

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://www.kinoaero.cz/")
        page.wait_for_timeout(2000)

        film = page.locator("div.program__movie-name").first.inner_text().strip()
        print("Jméno filmu:", film)

        page.goto("https://www.csfd.cz/")
        page.wait_for_selector("input.tt-input")
        page.fill("input.tt-input", film)
       
        page.click(".btn-search")
        page.click('.film-title-name')

        rating = page.locator("div.film-rating-average").first.inner_text().strip()
        print("Hodnocení na CSFD:", rating)

        input("Zmáčkni Enter pro zavření prohlížeče")
        browser.close()

if __name__ == "__main__":
    main()
