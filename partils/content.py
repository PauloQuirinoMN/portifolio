import flet as ft

class MainConteudo(ft.Container):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.expand = True
        self.bgcolor = ft.Colors.AMBER
        self.content = ft.Column(
            controls=[
                ft.Text(value="Olá mundo!", color=ft.Colors.WHITE, size=50)
            ],
            expand=True,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
        
 