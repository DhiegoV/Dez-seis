
class Menu:

    def __init__(self, nome, sistema=None, submenus=None, acoes=None):
        self.nome = nome
        self.sistema = sistema
        self.submenus = submenus
        self.acoes = acoes
        self.pai = None

        if self.submenus:
            for submenu in self.submenus.values():
                submenu.pai = self
                submenu.sistema = self.sistema

    def mostrar_arvore_menus(self, profundidade=0):
        print('\t'*profundidade, self.nome,
              sep='')
        profundidade += 1

        if self.submenus:
            for submenu in self.submenus.values():
                submenu.mostrar_arvore_menus(profundidade)

    def navegar(self):
        existem_submenus = bool(self.submenus)
        existem_acoes = bool(self.acoes)

        if not existem_submenus and not existem_acoes:
            print('<vazio>')
            self.pai.navegar()

        if self.pai:
            print('\\', self.pai.nome)

        if existem_submenus:
            for comando, submenu in self.submenus.items():
                print(comando, submenu)

        if existem_acoes:
            for comando, acao in self.acoes.items():
                print(comando, acao['nome'])

        desejo = input()
        if existem_submenus and desejo in self.submenus.keys():
            self.submenus[desejo].navegar()
        elif existem_acoes and desejo in self.acoes.keys():
            metodo = 'self.sistema.'+self.acoes[desejo]['cmd']
            print('metodo =', metodo)
            exec(metodo, globals(), locals())
        elif desejo == '\\':
            self.pai.navegar()
        else:
            print('caractere inválido!')

    def __str__(self):
        return self.nome
