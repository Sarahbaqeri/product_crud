

class Products:
    products_list=[]
    def __init__(self,product_Id,category_Id,title,short_description,description,slug,permalink,IsAvailable,sku,price,regular_price,sale_price,manage_stock,stock_quantity,IsVisible,date_created_gmt,date_modified_gmt):
        self.product_Id=product_Id
        self.category_Id=category_Id
        self.title=title
        self.short_description=short_description
        self.description=description
        self.slug=slug
        self.permalink=permalink
        self.IsAvailable=IsAvailable
        self.sku=sku
        self.price=price
        self.regular_price=regular_price
        self.sale_price=sale_price
        self.manage_stock=manage_stock
        self.date=date_created_gmt
        self.IsVisible=IsVisible
        self.date_created_gmt=date_created_gmt
        self.date_modofied_gmt=date_modified_gmt
        

    def __repr__(self):
        return f'Products({self.title},{self.short_description},{self.price},{self.regular_price},{self.sale_price},{self.description},{self.sku},{self.permalink},{self.IsAvailable},{self.IsVisible},{self.manage_stock},{self.date_created_gmt},{self.date_modofied_gmt})'
    
        
    def create(self):
        self.products_list.append(self.title)
        return self.title + self.short_description + self.price + self.description
        
    
    def read(self):
        for item in self.products_list:
            print(item)
        
    
    def update(self):
        new_title=input('enter your new product title :')
        for item in self.products_list:
            if item==new_title:
                print('product is already exist ')
            else:
                self.products_list.append(new_title)
                
                
    def delete(self,name):
        self.products_list.remove(name)
        if name not in self.products_list:
            print('this product is not exist') 
    
    