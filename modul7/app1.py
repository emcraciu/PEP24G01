from modul7.categorii import Haine, Accesorii


class Shop:
    main_menu_options = {1: 'Categorii', 2: 'Produse', 3: 'Iesire'}
    user_select_message = f'Alege optiune:'
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

    def adauga_prod(self):
        produs, pret, stoc = input('give product, price, stoc: ').split(',')
        pret = int(pret)
        stoc = int(stoc)
        self.stoc.update({produs: (pret, stoc)})

    def show_stock(self):
        print(self.stoc)

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


if __name__ == "__main__":
    s = Shop()
    # s.print_main_menu()
    # s.get_user_option(f'Alege optiune:', Shop.main_menu_options)
    s.stoc.append(Haine(nume='tricouri', pret=100, stoc=200))
    s.stoc.append(Haine(nume='pantaloni', pret=120, stoc=250))
    s.stoc.append(Accesorii(nume='bratara', pret=10, stoc=1000))
    s.start()
