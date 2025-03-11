import flet as ft

class SidebarCabecalho():
    ...
class SidebarConteudo():
    ...
class SidebarRodape():
    ...

class Sidebar(ft.Container):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.expand = True
        self.bgcolor = ft.Colors.BACKGROUND
        self.content = ft.Column(
            controls=[
                SidebarCabecalho(),
                SidebarConteudo(),
                SidebarRodape(),
            ]
        )