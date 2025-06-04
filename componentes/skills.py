import flet as ft

paleta = {
    "verdemuitoescuro": "#111b21",
    "azul claro": "#6994ae",
    "azul medio": "#274e61",
    "morronzinho": "#444e21",
    "gelo": "#99a67e",
}

class Skill(ft.Container):
    def __init__(self, titulo=str, valor=float):
        super().__init__()
        self.titulo = titulo
        self.valor = valor


class SkillRing(Skill):
    def __init__(self, titulo=str, valor=float):
        super().__init__(titulo, valor)
        self.expand = True
        self.content = ft.Column(
            controls=[
                ft.Stack(
                    controls=[
                        ft.PieChart(
                            sections=[
                                ft.PieChartSection(value=self.valor, color=paleta["azul medio"], radius=5),    
                                ft.PieChartSection(value=1 - self.valor, color=ft.Colors.BLACK38, radius=5),
                            ],
                            sections_space=0,
                            center_space_color=paleta["verdemuitoescuro"],
                            height=50,
                        ),
                        ft.Container(
                            content=ft.Text(value=f'{self.valor:.0%}', theme_style=ft.TextThemeStyle.BODY_MEDIUM, color=paleta["gelo"]),
                            alignment=ft.alignment.center,
                            height=50,
                        )
                    ]
                ),
                ft.Text(value=self.titulo, theme_style=ft.TextThemeStyle.BODY_LARGE, color=paleta["gelo"])
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )



class SkillProgressbar(Skill):
    def __init__(self, titulo=str, valor=float):
        super().__init__(titulo, valor)
        self.expand = True
        self.content = ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.Text(self.titulo, theme_style=ft.TextThemeStyle.BODY_LARGE, color=paleta["gelo"]),
                        ft.Text(f'{self.valor:.0%}', theme_style=ft.TextThemeStyle.BODY_MEDIUM, color=paleta["gelo"]),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
                ft.ProgressBar(self.valor, color=paleta["azul medio"], bgcolor=ft.Colors.BLACK38),
            ]
        )