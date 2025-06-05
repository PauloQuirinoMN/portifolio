import flet as ft
from partils.sidebar import Sidebar
from partils.content import MainConteudo

paleta = {
    "bege": "#EBE7B7",
    "azul claro": "#029b99",
    "azul medio": "#001f21",
    "laranjinha": "#de4f15",
    "amarelim": "#ecc039",
}


class App:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.bgcolor = paleta['bege']
        self.page.padding = 20
        self.main()


    def main(self):
        self.sidebar = Sidebar(col={'xs':0, 'md': 5, 'lg': 4, 'xxl': 3})
        self.content = MainConteudo(col={'xs':12, 'md': 7, 'lg': 8, 'xxl': 9})
        
        layout = ft.ResponsiveRow(
            columns=12,
            expand=True,
            spacing=0,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Column(
                    col=4,
                    controls=[self.sidebar],
                    spacing=12, 
                    expand=True,
                    scroll=ft.ScrollMode.AUTO,
                ),
                ft.Column(
                    col=8,
                    controls=[self.content],
                    spacing=12,
                    expand=True,
                )
            ],       
        )
        
        self.page.add(layout)

if __name__ == '__main__':
    ft.app(target=App, assets_dir='assets')