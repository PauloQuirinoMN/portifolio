import flet as ft
from partils.sidebar import Sidebar
from partils.content import MainConteudo

class App:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.bgcolor = ft.Colors.BLACK
        self.main()


    def main(self):
        self.sidebar = Sidebar()
        self.content = MainConteudo()
        self.bgcolor = ft.Colors.BLACK

        layout = ft.ResponsiveRow(
            columns=12,
            controls=[
                ft.Column(
                    col={"sm":12, "md":4},
                    controls=[self.sidebar],
                ),
                ft.Column(
                    col={"sm":12, "md": 8},
                    controls=[self.content],
                )
            ],
            expand=True,
        )

        self.page.add(layout)

if __name__ == '__main__':
    ft.app(target=App, assets_dir='assets')