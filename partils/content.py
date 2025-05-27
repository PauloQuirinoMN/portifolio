import flet as ft


class ProjetoItem(ft.Container):
    def __init__(self, titulo: str, descricao: str, url: str, **kwargs):
        super().__init__(**kwargs)
        self.titulo = titulo
        self.descricao = descricao
        self.url = url

        self.padding = ft.padding.all(10)
        self.bgcolor = ft.Colors.WHITE24
        self.border_radius = ft.border_radius.all(15)
        self.content = ft.Column(
            controls=[
                ft.Text(value=self.titulo , style=ft.TextThemeStyle.LABEL_LARGE),
                ft.Text(value=self.descricao, style=ft.TextThemeStyle.BODY_MEDIUM),
                ft.TextButton(
                    content=ft.Row(
                        [
                            ft.Text(value="VER AO VIVO", theme_style=ft.TextThemeStyle.BODY_LARGE, color=ft.Colors.PRIMARY),
                            ft.Icon(name=ft.Icons.ARROW_FORWARD_IOS, size=14, color=ft.Colors.PRIMARY)
                        ],
                        tight=True,
                    ),
                    url=self.url 
                )
            ]
        )

class Banner(ft.Container):
    def __init__(self):
        super().__init__()
        self.banner()

    def banner(self):         
        self.expand = True
        self.margin = ft.margin.only(top=15)
        self.image = ft.DecorationImage(
            src="images/bg.jpg",
            fit=ft.ImageFit.COVER,
            repeat=ft.ImageRepeat.NO_REPEAT,
            opacity=0.9,
        )
        self.shadow = ft.BoxShadow(
            color=ft.Colors.WHITE10,  
            offset=ft.Offset(x=0, y=-60),
            spread_radius=-30,
        )
        self.content = ft.ResponsiveRow(
            expand=True,
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
                    fit=ft.ImageFit.COVER,
                    repeat=ft.ImageRepeat.NO_REPEAT,
                    )
                )
            ]
        )

class Experencia(ft.Container):
    def __init__(self):
        super().__init__()
        self.conteudos()

    def conteudos(self):
        self.padding = ft.padding.symmetric(vertical=20)
        self.expand = True
        self.content = ft.ResponsiveRow(
            columns=12,
            controls=[
                ft.Text(
                    col={"xs":6, "md":3},
                    spans=[
                        ft.TextSpan(
                            text=" 1 + ",
                            style=ft.TextStyle(
                                color=ft.Colors.PRIMARY,
                                weight=ft.FontWeight.W_900,
                                size=16,
                            )
                        ),
                        ft.TextSpan(
                            text="Anos de experiência",
                            style=ft.TextStyle(
                                color=ft.Colors.WHITE,
                                weight=ft.FontWeight.W_900,
                                size=12,
                            )
                        )
                    ]
                ),


                ft.Text(
                    col={"xs":6, "md":3},
                    spans=[
                        ft.TextSpan(
                            text=" 2 + ",
                            style=ft.TextStyle(
                                color=ft.Colors.PRIMARY,
                                weight=ft.FontWeight.W_900,
                                size=16,
                            )
                        ),
                        ft.TextSpan(
                            text="Linguagens de programação",
                            style=ft.TextStyle(
                                color=ft.Colors.WHITE,
                                weight=ft.FontWeight.W_900,
                                size=12,
                            )
                        )
                    ]
                ),


                ft.Text(
                    col={"xs":6, "md":3},
                    spans=[
                        ft.TextSpan(
                            text=" 5 + ",
                            style=ft.TextStyle(
                                color=ft.Colors.PRIMARY,
                                weight=ft.FontWeight.W_900,
                                size=16,
                            )
                        ),
                        ft.TextSpan(
                            text="Projetos",
                            style=ft.TextStyle(
                                color=ft.Colors.WHITE,
                                weight=ft.FontWeight.W_900,
                                size=12,
                            )
                        )
                    ]
                ),

                ft.Text(
                    col={"xs":6, "md":3},
                    spans=[
                        ft.TextSpan(
                            text=" 10k + ",
                            style=ft.TextStyle(
                                color=ft.Colors.PRIMARY,
                                weight=ft.FontWeight.W_900,
                                size=16,
                            )
                        ),
                        ft.TextSpan(
                            text="Corações felizes",
                            style=ft.TextStyle(
                                color=ft.Colors.WHITE,
                                weight=ft.FontWeight.W_900,
                                size=12,
                            )
                        )
                    ]
                )
            ],
            expand=True
        )


projetos = ft.ResponsiveRow(
    expand=True,
    columns=12,
    controls=[
        ProjetoItem(titulo="Calculadora Iphone", descricao="Design como a calculadora do Iphone", url="", col={"xs": 12, "md": 6, "lg": 4}),
        ProjetoItem(titulo="Projeto dois", descricao="projeto segundo", url="", col={"xs": 12, "md": 6, "lg": 4}),
        ProjetoItem(titulo="Treceiro projeto", descricao="Terceiro projeto", url="", col={"xs": 12, "md": 6, "lg": 4}),
        ProjetoItem(titulo="4º projetinho", descricao="quarto projeto", url="", col={"xs": 12, "md": 6, "lg": 4}),
        ProjetoItem(titulo="cinco ", descricao="com esse são cinco", url="", col={"xs": 12, "md": 6, "lg": 4}),
    ]
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
                ft.Row(controls=[ft.Text(value="Projetos", size=20, color=ft.Colors.WHITE, font_family=ft.FontWeight.BOLD, text_align=ft.alignment.center_left)], alignment=ft.MainAxisAlignment.START),
                projetos,
            ],
            spacing=10,
            expand=True,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
        
 