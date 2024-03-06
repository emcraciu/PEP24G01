class Shop:
    main_menu_options = {1: 'Categorii', 2: 'Produse', 3: 'Iesire'}
    stoc = {}
    user_input = None
    status = None

    def print_main_menu(self):
        menu = 'Bun venit la magazinul Pycharm: \n'
        # user_select_message = f'Alege optiune:'
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
        print(self.menu)
        self.user_input = input(self.user_select_message)
        while self.user_input != '5':
            if self.user_input == '1':
                self.show_stock()
            elif self.user_input == '2':
                self.adauga_prod()
            elif self.user_input == '3':
                self.remove_prod()
            elif self.user_input == '4':
                self.reducere()
            print(self.menu)
            self.user_input = input(self.user_select_message)


if __name__ == "__main__":
    s = Shop()
    s.print_main_menu()
    s.get_user_option(f'Alege optiune:', Shop.main_menu_options)
