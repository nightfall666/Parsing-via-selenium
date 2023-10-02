from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import openpyxl

driver = webdriver.Chrome()
driver.get("https://iotvega.com/product")

productElements = driver.find_elements(By.CLASS_NAME, 'product-name')
priceElements = driver.find_elements(By.CLASS_NAME, 'price_item')


productNames = []
productPrices = []

for productElement, priceElement in zip(productElements, priceElements):
    productNames.append(productElement.text)
    productPrices.append(priceElement.text)

driver.quit()

data = {'Название продукта': productNames, 'Цена продукта': productPrices}
df = pd.DataFrame(data)

# Задание ширины столбцов
file_path = 'products.xlsx'
with pd.ExcelWriter(file_path, engine='openpyxl') as writer:
    df.to_excel(writer, sheet_name='Sheet1', index=False)
    workbook = writer.book
    worksheet = writer.sheets['Sheet1']
    worksheet.column_dimensions['A'].width = 30
    worksheet.column_dimensions['B'].width = 15