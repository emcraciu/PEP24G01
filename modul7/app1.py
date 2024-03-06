from modul7.categorii import Haine, Accesorii, Incaltaminte


class Shop:
    main_menu_options = {1: 'Categorii', 2: 'Produse', 3: 'Iesire'}
    products_menu_options = {1: 'Adaugare', 2: 'Vizualizare', 3: 'Iesire la meniul principal'}
    user_select_message = f'Alege optiune:'
    product_select_message = f'Introduceti optiunea:'
    product_mapping = {'Haine': Haine, 'Accesorii': Accesorii, 'Incaltaminte': Incaltaminte}
    stoc = []
    user_input = None
    status = None

    def print_main_menu(self):
        menu = 'Bun venit la magazinul Pycharm: \n'
        options = '\n'.join([f'\t{key}. {value}' for key, value in self.main_menu_options.items()])
        print(menu + options + '\n')

    def get_user_option(self, message, menu):
        while True:
            try:
                option = int(input(message))
                if option in menu:
                    break
            except:
                pass
            print('Nu este o valoare corecta pentru meniu')
        return option

    def print_categories(self):
        print("=" * 40)
        print(" CATEGORII ".center(40, "="))
        print("=" * 40)
        print("\n".join(set([f"---\t{cat.__class__.__name__}" for cat in self.stoc])))

    def print_products(self):
        print(" PRODUSE ".center(40, "="))
        print("=" * 40)
        options = '\n'.join([f'\t{key}. {value}' for key, value in self.products_menu_options.items()])
        print(options + '\n')

    def add_product(self):
        categorie = input('Introduceti numele categoriei:')
        produs = input('Introduceti numele produsului:')
        pret = input('Introduceti pret:')
        stoc = input('Introduceti stoc:')
        prod_class = self.product_mapping[categorie.capitalize()]
        product = prod_class(produs, pret, stoc)
        self.stoc.append(product)

    def show_stock(self):
        for obj in self.stoc:  # type: Haine
            print(obj.__class__.__name__)
            print('=' * 30)
            print(obj.nume)
            print(obj.pret)
            print(obj.stoc)

    def remove_prod(self):
        product, price, qty = input('give product, price, quantity: ').split(',')
        price = int(price)
        qty = int(qty)
        stock = self.stoc[product][1] - qty
        self.stoc.update({product: (price, stock)})

    def reducere(self):
        product, procent = input('give product, sale discount: ').split(',')
        procent = int(procent)
        new_price = self.stoc[product][0] - ((procent / 100) * self.stoc[product][0])
        self.stoc.update({product: (new_price, self.stoc[product][1])})

    def start(self):
        self.print_main_menu()
        option = self.get_user_option(self.user_select_message, self.main_menu_options)
        if option == 1:
            self.print_categories()
        elif option == 2:
            self.print_products()
            option2 = self.get_user_option(self.product_select_message, self.products_menu_options)
            if option2 == 1:
                self.add_product()
            elif option2 == 2:
                self.show_stock()


if __name__ == "__main__":
    s = Shop()
    # s.print_main_menu()
    # s.get_user_option(f'Alege optiune:', Shop.main_menu_options)
    s.stoc.append(Haine(nume='tricouri', pret=100, stoc=200))
    s.stoc.append(Haine(nume='pantaloni', pret=120, stoc=250))
    s.stoc.append(Accesorii(nume='bratara', pret=10, stoc=1000))
    s.start()
