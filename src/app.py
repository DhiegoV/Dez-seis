
from src.Sistema import Sistema
from src.util.Menu import Menu


main = Menu(
    'principal',
    Sistema(),
    submenus=dict(
        A=Menu(
            'amigos',
            acoes=dict(
                l=dict(nome='listar amigos', cmd='sistema')  # compile(sistema.listar_usuarios()
            )
        ),
        C=Menu(
            'configurações',
            submenus=dict(
                C=Menu(
                    'conta',
                    acoes=dict(
                        r=dict(nome='remover conta', cmd='remover_conta()')

                    )
                )
            )
        )
    )
)

# main.mostrar_arvore_menus()

main.navegar()
