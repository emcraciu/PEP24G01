class Shop:
    stoc = {}
    user_input = None
    status = None
    menu = '''   
        Meniu:
               1. Vizualizare stoc
               2. Adaugare produs
               3. Stergere produs
               4. Reducere
               5. Iesire
        '''
    user_select_message = f'Alege optiune:\n'

    # def modif_stoc(self):
    #     print('''
    #     Meniu:
    #            1. Vizualizare stoc
    #            2. Adaugare produs
    #            3. Stergere produs
    #            4. Iesire
    #     ''')
    #     self.user_input = input(f'Alege optiune:\n')
    #     if self.user_input == '2':
    #         produs, pret, stoc = input('give product, price, stoc').split(',')
    #         self.adauga_prod(produs, pret, stoc)
    def adauga_prod(self):
        produs, pret, stoc = input('give product, price, stoc: ').split(',')
        pret = int(pret)
        stoc = int(stoc)
        self.stoc.update({produs: (pret, stoc)})

    # def set_status(self, status):
    #     self.status = status

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


s = Shop()
s.start()

# t = Shop()
# Shop.adauga_prod(s, 'unt', 5, 100)
# s.adauga_prod('unt', 5, 100)
# t.adauga_prod('unt', 6, 100)
# s.set_status('open')
# t.set_status('closed')
# s.modif_stoc()
# print(f'Ai ales: {s.user_input}')
# print(s.stoc)
# print(t.stoc)
# print(s.show_stock())
# print(t.status)
