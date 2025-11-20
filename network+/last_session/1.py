import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# آدرس صفحه موبایل‌ها در دیجیکالا
url = "https://www.digikala.com/search/category-mobile-phone/"

# تابعی برای استخراج اطلاعات از یک صفحه
def get_product_info(page_url):
    response = requests.get(page_url)
    soup = BeautifulSoup(response.text, 'parser.html')
    
    products = []

    # پیدا کردن تمام محصولات
    product_cards = soup.find_all('div', class_='product-card')

    for card in product_cards:
        name = card.find('a', class_='product-card-title')
        price = card.find('div', class_='product-card-price')
        
        if name and price:
            product_name = name.get_text(strip=True)
            product_price = price.get_text(strip=True)
            
            # تلاش برای پیدا کردن لینک جزئیات محصول (برای مشخصات بیشتر)
            product_link = "https://www.digikala.com" + name['href']
            
            # استخراج مشخصات اضافی
            product_details = get_product_details(product_link)
            
            products.append({
                'name': product_name,
                'price': product_price,
                'link': product_link,
                'details': product_details
            })
            
    return products

# تابعی برای استخراج مشخصات دقیق از صفحه محصول
def get_product_details(product_url):
    response = requests.get(product_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # این بخش بستگی به ساخت.ار صفحه محصول دارد و ممکن است نیاز به تغییر داشته باشد
    details_section = soup.find('div', class_='product-detail-section')
    details = {}

    if details_section:
        specs = details_section.find_all('div', class_='specs-item')
        for spec in specs:
            try:
                title = spec.find('div', class_='specs-title').get_text(strip=True)
                value = spec.find('div', class_='specs-value').get_text(strip=True)
                details[title] = value
            except AttributeError:
                continue

    return details

# استخراج اطلاعات از چندین صفحه
def scrape_all_pages(start_page=1, num_pages=5):
    all_products = []
    for page_num in range(start_page, start_page + num_pages):
        page_url = f"{url}?page={page_num}"
        print(f"در حال استخراج اطلاعات از صفحه {page_num}...")
        products = get_product_info(page_url)
        all_products.extend(products)
        time.sleep(1)  # برای جلوگیری از ارسال درخواست زیاد به سایت
    return all_products

# ذخیره داده‌ها در فایل CSV
def save_to_csv(products, filename="digikala_mobile_products.csv"):
    df = pd.DataFrame(products)
    df.to_csv(filename, index=False)
    print(f"داده‌ها با موفقیت در فایل {filename} ذخیره شد.")

# استخراج اطلاعات و ذخیره در فایل
if __name__ == "__main__":
    all_products = scrape_all_pages(start_page=1, num_pages=5)
    save_to_csv(all_products)
