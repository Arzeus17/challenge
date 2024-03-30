import requests
import csv

# Enlisto los términos de búsqueda
search_terms = ["iPhone", "Samsung Galaxy", "Google Pixel", "Xiaomi Redmi", "Huawei P30"]

# Inicializo lista para almacenar todos los ítems de todas las búsquedas
all_items = []

# Itero sobre cada término de búsqueda
for search_term in search_terms:
    # Realizo solicitud GET a la API de Mercado Libre para el término de búsqueda actual
    response = requests.get(f"https://api.mercadolibre.com/sites/MLA/search?q={search_term}&limit=50")
    data = response.json()

    # Proceso cada resultado de la búsqueda actual
    for result in data.get('results', []):
        item_id = result.get('id')
        if item_id:
            # Realizo solicitud GET para obtener detalles del ítem actual
            item_response = requests.get(f"https://api.mercadolibre.com/items/{item_id}")
            item_data = item_response.json()
            
            # Selecciono campos de interés y agregarlos a la lista de ítems
            item_info = {
                'Search Term': search_term,
                'Title': item_data.get('title'),
                'Price': item_data.get('price'),
                'Condition': item_data.get('condition'),
                'Sold Quantity': item_data.get('sold_quantity'),
                'Location': item_data.get('seller_address', {}).get('city', ''),
                'Discount': item_data.get('discount'),
                'Seller Rating': item_data.get('seller_rating'),
                'Seller Sales Completed': item_data.get('seller_sales_completed'),
                'Seller Username': item_data.get('seller_username'),
                'Seller Location': item_data.get('seller_location'),
                'Color': item_data.get('color'),
                'Seller Address': item_data.get('seller_address'),
                'Payment Methods': item_data.get('payment_methods'),
                'Description': item_data.get('description')
            }
            all_items.append(item_info)

# Escribo los resultados en un archivo CSV
with open('testMeLi.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Search Term', 'Title', 'Price', 'Condition', 'Sold Quantity', 'Location', 'Discount', 'Seller Rating', 'Seller Sales Completed', 'Seller Username', 'Seller Location', 'Color', 'Seller Address', 'Payment Methods', 'Description']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for item in all_items:
        writer.writerow(item)

print("Proceso completado. Los resultados se han guardado en 'testMeLi.csv'.")


