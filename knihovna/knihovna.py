from playwright.sync_api import sync_playwright
import os, json

path = os.path.join(os.path.dirname(__file__), "Knihovna.json")

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.databazeknih.cz")
        page.wait_for_timeout(2000)

        pop_knihy = []
        pop_knihy2 = page.locator("div.book").all()
        for item in pop_knihy2[:3]:
            title = item.locator(".title").inner_text()
            
            pop_knihy.append({
                "title": title.strip(),
            })
            print(f"Popular bok : {title}")

        autori = []
        nova_kniha = page.locator("div.nbox_book a").all()

        for i in range (min(3, len(nova_kniha))):
            nova_kniha[i].click()
            page.wait_for_timeout(2000)

            autor = page.locator(".autor a").inner_text()
            autori.append(autor.strip())
            print(f"Autoři: {autor}")

            page.go_back()
            page.wait_for_timeout(2000)

        data = {
            "popular_books": pop_knihy,
            "new_books": autori
        }
        with open (path, mode="w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        
        page.wait_for_timeout(3000)
        browser.close()

if __name__ == "__main__":
    main()