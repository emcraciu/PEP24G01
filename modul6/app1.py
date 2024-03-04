
class Shop:
    stoc = {}
    user_input = None
    status = None

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

    def adauga_prod(self, produs, pret, stoc):
        self.stoc.update({produs: (pret, stoc)})

    def set_status(self, status):
        self.status = status

    def show_stock(self):
        print(self.stoc)

    def start(self):

        print('''   
        Meniu:
               1. Vizualizare stoc
               2. Adaugare produs
               3. Stergere produs
               4. Iesire
        ''')
        self.user_input = input(f'Alege optiune:\n')
        while self.user_input != '4':
            if self.user_input == '1':
                self.show_stock()
            elif self.user_input == '2':
                produs, pret, stoc = input('give product, price, stoc').split(',')
                self.adauga_prod(produs, pret, stoc)
            elif self.user_input == '3':
                pass
                ## implement
            print('''   
            Meniu:
                   1. Vizualizare stoc
                   2. Adaugare produs
                   3. Stergere produs
                   4. Iesire
            ''')
            self.user_input = input(f'Alege optiune:\n')



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
