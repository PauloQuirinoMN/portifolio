import flet as ft

class MainConteudo(ft.Container):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.expand = True
        self.content = ft.Column(
            controls=[
                ft.Text(value="Olá mundo!", color=ft.Colors.WHITE, size=50)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
        
 