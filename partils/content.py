import flet as ft

class Banner(ft.Container):
    def __init__(self):
        super().__init__(self)
        self.expand = True
        self.banner()

    def banner(self):         
        self.expand = True
        self.image = ft.DecorationImage(
            src="images/bg.jpg",
            fit=ft.ImageFit.COVER,
            repeat=ft.ImageRepeat.NO_REPEAT,
            opacity=0.5,
        )
        self.content = ft.ResponsiveRow(
            columns=12,
            vertical_alignment=ft.CrossAxisAlignment.END,
            controls=[
                ft.Container(
                    col={"md":12, "lg":8},
                    padding=ft.padding.all(50),
                    content=ft.Column(
                        controls=[
                            ft.Text(value="Descubra meu incrível portifílo", theme_style=ft.TextThemeStyle.HEADLINE_LARGE, color=ft.Colors.WHITE),
                            ft.Text(
                                spans=[
                                    ft.TextSpan(text="< "),
                                    ft.TextSpan(text="code", style=ft.TextStyle(color=ft.Colors.YELLOW)),
                                    ft.TextSpan(text=" >",),


                                    ft.TextSpan(
                                        text="Eu desenvolvo aplicativos IOS e Android, softwares para macOS, Windowns e Linux, Álem de site responsivos",
                                        style=ft.TextStyle(color=ft.Colors.WHITE), 
                                    ),
                                    ft.TextSpan(text="</"),
                                    ft.TextSpan(text="code", style=ft.TextStyle(color=ft.Colors.YELLOW)),
                                    ft.TextSpan(text=" >",),
                                ],
                                theme_style=ft.TextThemeStyle.BODY_MEDIUM,
                            ),
                            ft.ElevatedButton(
                                bgcolor=ft.Colors.BLUE_400,
                                content=ft.Text(value="Explore agora", color=ft.Colors.BLACK, width=ft.FontWeight.BOLD),
                                url="#",
                                style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0)),
                            )
                        ],
                        spacing=30,
                        alignment=ft.MainAxisAlignment.CENTER,
                    )
                ),
                ft.Container(
                    col={"md":12, "lg":4},
                    content=ft.Image(
                        src="images/face-2.png",
                        width=20,
                        # scale=ft.Scale(scale=1.8, alignment=ft.alignment.bottom_center)
                    )
                )
            ]
        )

class Experencia(ft.Container):
    def __init__(self):
        super().__init__(self)
        self.expand = True
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
        
 