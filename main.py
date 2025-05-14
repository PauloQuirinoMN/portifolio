import flet as ft
from partils.sidebar import Sidebar
from partils.content import MainConteudo

class App:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.bgcolor = ft.Colors.BLACK
        self.page.padding = 0
        self.main()


    def main(self):
        self.sidebar = Sidebar()
        self.content = MainConteudo()
        self.bgcolor = ft.Colors.BLACK

        layout = ft.ResponsiveRow(
            expand=True,
            spacing=0,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,    
            columns=12,
            controls=[
                ft.Column(
                    col={"xs": 12, "md": 4, "lg": 4},
                    controls=[self.sidebar],
                    spacing=0, 
                    expand=True,
                ),
                ft.Column(
                    col={"xs": 12, "md": 8, "lg": 8},
                    controls=[self.content],
                    spacing=0,
                    expand=True,
                )
            ],    
        )
        

        self.page.add(layout)

if __name__ == '__main__':
    ft.app(target=App, assets_dir='assets')