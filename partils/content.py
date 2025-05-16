import flet as ft

class Banner(ft.Container):
    def __init__(self):
        super().__init__(self)
        self.bgcolor = ft.Colors.GREEN
        self.expand = True
        self.banner()

    def banner(self):
        self.expand = True
        self.content = ft.Column(
            controls=[
                ft.Text(value="Banner aqui")
            ],
            expand=True,
        )

class Experencia(ft.Container):
    def __init__(self):
        super().__init__(self)
        self.expand = True
        self.bgcolor = ft.Colors.BLUE
        self.conteudos()

    def conteudos(self):
        self.content = ft.Row(
            controls=[
                ft.Text(value="Experiência 1= aqui"),
                ft.Text(value="Experiência 2= aqui")
            ],
            expand=True
        )

class MainConteudo(ft.Container):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bgcolor = ft.Colors.AMBER
        self.expand = True
        
        instancia_banner = Banner()
        instancia_experiencia = Experencia()
        
        self.content = ft.Column(
            controls=[
                instancia_banner,
                instancia_experiencia,
            ],
            expand=True,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
        
 