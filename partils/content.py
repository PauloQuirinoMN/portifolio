import flet as ft
from typing import List, Dict, Union

paleta = {
    "verdemuitoescuro": "#111b21",
    "azul claro": "#6994ae",
    "azul medio": "#274e61",
    "morronzinho": "#444e21",
    "gelo": "#99a67e",
}

class ProjetoItem(ft.Container):
    def __init__(self, titulo: str, descricao: str, url: str, **kwargs):
        super().__init__(**kwargs)
        self.titulo = titulo
        self.descricao = descricao
        self.url = url

        self.padding = ft.padding.all(10)
        self.bgcolor = paleta["gelo"]
        self.border_radius = ft.border_radius.all(15)
        self.content = ft.Column(
            controls=[
                ft.Text(value=self.titulo , style=ft.TextThemeStyle.LABEL_LARGE, color=paleta["verdemuitoescuro"]),
                ft.Text(value=self.descricao, style=ft.TextThemeStyle.BODY_MEDIUM, color=paleta["verdemuitoescuro"]),
                ft.TextButton(
                    content=ft.Row(
                        [
                            ft.Text(value="VER AO VIVO", theme_style=ft.TextThemeStyle.BODY_LARGE, color=paleta["morronzinho"]),
                            ft.Icon(name=ft.Icons.ARROW_FORWARD_IOS, size=14, color=paleta["morronzinho"])
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
        # self.image = ft.DecorationImage(
        #     src="images/Equipamento.jpeg",
        #     fit=ft.ImageFit.FILL,
        #     repeat=ft.ImageRepeat.NO_REPEAT,
        #     opacity=0.9,
        # # )
        # self.shadow = ft.BoxShadow(
        #     color=ft.Colors.WHITE12, 
        #     offset=ft.Offset(x=0, y=-60),
        #     spread_radius=-30,
        # )
        self.content = ft.ResponsiveRow(
            expand=True,
            columns=12,
            vertical_alignment=ft.CrossAxisAlignment.END,
            controls=[
                ft.Container(
                    # bgcolor=paleta["gelo"],
                    col={"md":12, "lg":8},
                    padding=ft.padding.all(40),
                    content=ft.Column(
                        controls=[
                            ft.Text(value=' "Analisar dados é extrair lições do passado para agir com precisão no presente e construir decisões mais inteligentes no futuro." ', theme_style=ft.TextThemeStyle.HEADLINE_LARGE, color=paleta["azul claro"], size=25, text_align=ft.TextAlign.START),
                            ft.Text(
                                spans=[
                                    ft.TextSpan(text="< "),
                                    ft.TextSpan(text="code", style=ft.TextStyle(color=paleta["morronzinho"])),
                                    ft.TextSpan(text=" >",),


                                    ft.TextSpan(
                                        text="desenvolvimento front e back-end, interface gráfica para WEB, DESKTOP e MOBILE com foco em Ciência e análise de Dados.",
                                        style=ft.TextStyle(color=paleta["azul medio"], size=15), 
                                    ),
                                    ft.TextSpan(text="</"),
                                    ft.TextSpan(text="code", style=ft.TextStyle(color=paleta["morronzinho"])),
                                    ft.TextSpan(text=" >",),
                                ]
                            ),
                            ft.Container(height=100),
                            # ft.ElevatedButton(
                            #     bgcolor=paleta["azul medio"],
                            #     content=ft.Text(value="Explore agora", color=paleta["gelo"], width=ft.FontWeight.BOLD),
                            #     url="#",
                            #     style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0)),
                            # )
                        ],
                        spacing=30,
                        alignment=ft.MainAxisAlignment.START,
                        horizontal_alignment=ft.CrossAxisAlignment.START
                    )
                ),
                ft.Container(
                    col={"md":12, "lg":4},
                    content=ft.Image(
                    src="images/eueu.png",
                    fit=ft.ImageFit.COVER,
                    repeat=ft.ImageRepeat.NO_REPEAT,
                    )
                )
            ],
            alignment=ft.CrossAxisAlignment.START,
        )

class Experencia(ft.Container):
    def __init__(self):
        super().__init__()
        self.conteudos()

    def conteudos(self):
        self.bgcolor = ft.Colors.TRANSPARENT
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
                                color=paleta["azul medio"],
                                weight=ft.FontWeight.W_900,
                                size=16,
                            )
                        ),
                        ft.TextSpan(
                            text="Anos de experiência",
                            style=ft.TextStyle(
                                color=paleta["gelo"],
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
                                color=paleta["azul medio"],
                                weight=ft.FontWeight.W_900,
                                size=16,
                            )
                        ),
                        ft.TextSpan(
                            text="Linguagens de programação",
                            style=ft.TextStyle(
                                color=paleta["gelo"],
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
                                color=paleta["azul medio"],
                                weight=ft.FontWeight.W_900,
                                size=16,
                            )
                        ),
                        ft.TextSpan(
                            text="Projetos",
                            style=ft.TextStyle(
                                color=paleta["gelo"],
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
                                color=paleta["azul medio"],
                                weight=ft.FontWeight.W_900,
                                size=16,
                            )
                        ),
                        ft.TextSpan(
                            text="Corações felizes",
                            style=ft.TextStyle(
                                color=paleta["gelo"],
                                weight=ft.FontWeight.W_900,
                                size=12,
                            )
                        )
                    ]
                )
            ],
            expand=True
        )

class PricosItem(ft.Container):
    def __init__(self, preco:int, url:str, items_included: List[Dict[str, Union[str, bool]]], **kawrgs):
        super().__init__(**kawrgs)
        self.preco = preco
        self.url = url
        self.items_included = items_included
        self.bgcolor=ft.Colors.PRIMARY_CONTAINER
        self.padding=ft.padding.symmetric(vertical=20, horizontal=50)
        self.border_radius = ft.border_radius.all(20)
        self.content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=30,
            controls=[
                    ft.Text(value="Pagamento por hora", theme_style=ft.TextThemeStyle.BODY_LARGE),
                    ft.Text(
                        spans=[
                            ft.TextSpan(text='R$', style=ft.TextStyle(color=ft.Colors.BLACK)),
                            ft.TextSpan(text=f"{self.preco}", style=ft.TextStyle(color=ft.Colors.PRIMARY, weight=ft.FontWeight.BOLD, size=50)),
                            ft.TextSpan(text='/hora', style=ft.TextStyle(color=ft.Colors.BLACK)),  
                        ]
                    ),
                    ft.Column(
                        controls=[
                            ft.Row(
                                [
                                    ft.Icon(name=ft.Icons.CHECK if item['is_included'] else ft.Icons.CLOSE, color=ft.Colors.PRIMARY),
                                    ft.Text(value=item['title'], theme_style=ft.TextThemeStyle.BODY_MEDIUM)
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                            ) for item in self.items_included
                        ]
                    ),
                    ft.TextButton(
                        content=ft.Row(
                            controls=[
                                ft.Text(value="QUERO ESTE", theme_style=ft.TextThemeStyle.BODY_LARGE, color=ft.Colors.PRIMARY),
                                ft.Icon(name=ft.Icons.ARROW_FORWARD_IOS, size=14, color=ft.Colors.PRIMARY),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                        url=self.url,
                    )
            ]
        )

class TestemunhaItem(ft.Container):
    def __init__(self, usuario: str, job: str, testemunho:str, image_src: str = 'images/testimonial-default.jpg', **kwargs):
        super(). __init__()
        self.usuario = usuario
        self.job = job
        self.testemunho = testemunho
        self.image_src = image_src

        self.bgcolor = paleta["gelo"]
        self.padding = ft.padding.all(30)
        self.margin = ft.margin.only(top=20)
        self.width = 300
        self.content = ft.Stack(
            controls=[
                ft.Column(
                    spacing=0,
                    controls=[
                        ft.Text(value=f"{self.usuario}", theme_style=ft.TextThemeStyle.LABEL_LARGE),
                        ft.Text(value=self.job, theme_style=ft.TextThemeStyle.BODY_LARGE),

                        ft.Container(height=20),
                        ft.Text(
                            value=self.testemunho,
                            theme_style=ft.TextThemeStyle.BODY_MEDIUM
                        ),
                        ft.Container(height=20),
                        ft.Container(
                            content=ft.Row(
                                controls=[
                                    ft.Icon(name=ft.Icons.STAR, color=ft.Colors.AMBER, size=16),
                                    ft.Icon(name=ft.Icons.STAR, color=ft.Colors.AMBER, size=16),
                                    ft.Icon(name=ft.Icons.STAR, color=ft.Colors.AMBER, size=16),
                                    ft.Icon(name=ft.Icons.STAR, color=ft.Colors.AMBER, size=16),
                                    ft.Icon(name=ft.Icons.STAR, color=ft.Colors.AMBER, size=16),
                                ],
                                tight=True,
                            ),
                            bgcolor=ft.Colors.TRANSPARENT,
                            padding=ft.padding.symmetric(vertical=5, horizontal=10),
                            border_radius=ft.border_radius.all(50),
                        )
                    ],
                ),

                ft.Image(
                    src=self.image_src,
                    border_radius=ft.border_radius.all(100),
                    width=100,
                    top=0,
                    right=0,
                    offset=ft.Offset(x=0, y=-0.5),
                ),
            ]  
        )


testemunhas = ft.Row(
    scroll=ft.ScrollMode.HIDDEN,
    controls=[
        TestemunhaItem(usuario='Paulo Neto', job='Cientista de dados', testemunho="O melhor trabalho que eu ja vi", image_src='images/testimonial-1-280x280.jpg'),
        TestemunhaItem(usuario='Quirino', job='Analista de dados', testemunho="siplesmente incrível", image_src='images/testimonial-2-280x280.jpg'),
        TestemunhaItem(usuario='Maciel eu', job='Desenvolvedor', testemunho="perfeito"),
        TestemunhaItem(usuario='Maciel eu', job='Desenvolvedor', testemunho="perfeito", image_src='images/testimonial-3-280x280.jpg'),
    ]
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

precos = ft.ResponsiveRow(
    expand=True,
    columns=12,
    spacing=30,
    run_spacing=30,
    controls=[
        PricosItem(
            col={'xs': 12, 'lg': 4},
            preco=20,
            url="",
            items_included=[
                {'title': 'Prototipagem', 'is_included': True},
                {'title': 'Desenvolvimento WEB', 'is_included': True},
                {'title': 'Aplicativos multiplataforma', 'is_included': False},
                {'title': 'Manutenção por 12 meses', 'is_included': False},
            ]   
        ),
         PricosItem(
            col={'xs': 12, 'lg': 4},
            preco=100,
            url="",
            items_included=[
                {'title': 'Prototipagem', 'is_included': True},
                {'title': 'Desenvolvimento WEB', 'is_included': True},
                {'title': 'Aplicativos multiplataforma', 'is_included': True},
                {'title': 'Manutenção por 12 meses', 'is_included': False},
            ]
            
        ),
         PricosItem(
            col={'xs': 12, 'lg': 4},
            preco=200,
            url="",
            items_included=[
                {'title': 'Prototipagem', 'is_included': True},
                {'title': 'Desenvolvimento WEB', 'is_included': True},
                {'title': 'Aplicativos multiplataforma', 'is_included': True},
                {'title': 'Manutenção por 12 meses', 'is_included': True},
            ]
        )
    ]
)

logos = ft.Container(
    padding=ft.padding.all(30),
    opacity=0.6,
    content=ft.ResponsiveRow(
        controls=[
            ft.Image(
                src="images/brand-1-464x512.png",
                col={'xs': 6, 'lg': 3, 'xl': 2},
            ),
            ft.Image(
                src="images/brand-2-458x512.png",
                col={'xs': 6, 'lg': 3, 'xl': 2},
            ),
            ft.Image(
                src="images/brand-3-456x512.png",
                col={'xs': 6, 'lg': 3, 'xl': 2},
            ),
            ft.Image(
                src="images/brand-1-464x512.png",
                col={'xs': 6, 'lg': 3, 'xl': 2},
            ),
        ],
        spacing=30,
        run_spacing=30,
    )
)

footer = ft.Container(
    bgcolor=ft.Colors.SECONDARY_CONTAINER,
    opacity=0.2,
    padding=ft.padding.all(20),
    border_radius=ft.border_radius.all(10),
    content=ft.ResponsiveRow(
        columns=12,
        controls=[
            ft.Text(
                col={'xs':12, 'md':6},
                value="© 2025 todos os direitos reservados",
                theme_style=ft.TextThemeStyle.BODY_MEDIUM
            ),

            ft.Text(
                col={'xs':12, 'md':6},
                spans=[
                    ft.TextSpan(text="Email: "),
                    ft.TextSpan(text="pauloqneto@gmail.com", url='mailto:pauloqneto@gmail.com'),
                ],
                theme_style=ft.TextThemeStyle.BODY_MEDIUM,
                text_align=ft.TextAlign.END
                
            )
        ],
    )
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
                ft.Row(controls=[ft.Text(value="Preços", size=20, color=ft.Colors.WHITE, font_family=ft.FontWeight.BOLD, text_align=ft.alignment.center_left)], alignment=ft.MainAxisAlignment.START),
                precos,
                ft.Row(controls=[ft.Text(value="Recomendações", size=20, color=ft.Colors.WHITE, font_family=ft.FontWeight.BOLD, text_align=ft.alignment.center_left)], alignment=ft.MainAxisAlignment.START),  
                testemunhas, 
                logos,
                footer,
            ],
            spacing=10,
            expand=True,
            scroll=ft.ScrollMode.AUTO,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
        
 