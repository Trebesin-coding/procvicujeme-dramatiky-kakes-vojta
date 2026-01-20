from playwright.sync_api import sync_playwright

def main():

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://xkcd.com/")

        comic = page.locator('#comic img')
        comic.screenshot()
        print("Děkuju za screenshot")

        for i in range(3):
            comic = page.locator('#comic img')
            comic.screenshot(path=f'comic_{i+1}.png')

            print(f"Another one {i+1}")

            page.click('a[rel="next"]')
            page.wait_for_timeout(1000)

        page.wait_for_timeout(4000)
        browser.close()
        

if __name__ == "__main__":
    main()