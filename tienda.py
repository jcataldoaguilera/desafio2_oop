from producto import Producto

class Tienda:
    def __init__(self, nombre, delivery):
        self.__nombre = nombre
        self.__productos = []
        self.__delivery = delivery
        
    def ingreso_productos(self, producto):
        for prod in self.__productos:
            if prod.get_nombre() == producto.get_nombre():
                prod.mod_stock(producto.get_stock())
                return self.__productos.append(producto)
            
    def listar_productos(self):
        productos = ""
        for prod in self.__productos:
            productos += f"Nombre: {prod.get_nombre()}, Precio: ${prod.get_precio()}\n"
            productos += self.info_adicional(prod)
        return productos
    
    def info_adicional(self, producto):
        return ""
    

class Supermercado(Tienda):
    def info_adicional(self, producto):
        if producto.get_stock() < 10:
            return "(Pocos productos disponibles)\n"
        return ""
    
    
class Farmacia(Tienda):
    def info_adicional(self, producto):
        if producto.get_precio() > 15000:
            return " (Envío gratis al solicitar este producto)\n"
        return ""
    
    
class Restaurante(Tienda):
    pass