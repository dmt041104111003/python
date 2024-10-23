def merge_products(A, B):  
    existing = set(A)  
    return [product not in existing and existing.add(product) or False for product in B]