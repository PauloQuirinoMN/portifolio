import flet as ft
from partils.sidebar import Sidebar
from partils.content import MainConteudo

class App:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.bgcolor = ft.Colors.BLACK
        self.page.padding = 30
        self.main()


    def main(self):
        self.sidebar = Sidebar()
        self.content = MainConteudo()
        
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