import flet as ft

paleta = {
    "bege": "#EBE7B7",
    "azul claro": "#029b99",
    "azul medio": "#001f21",
    "laranjinha": "#de4f15",
    "amarelim": "#ecc039",
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
                                ft.PieChartSection(value=self.valor, color=paleta["azul medio"], radius=7),    
                                ft.PieChartSection(value=1 - self.valor, color=ft.Colors.BLACK38, radius=7),
                            ],
                            sections_space=0,
                            center_space_color=paleta["bege"],
                            height=70,
                        ),
                        ft.Container(
                            content=ft.Text(value=f'{self.valor:.0%}', theme_style=ft.TextThemeStyle.BODY_MEDIUM, color=paleta["laranjinha"]),
                            alignment=ft.alignment.center,
                            height=70,
                        )
                    ]
                ),
                ft.Text(value=self.titulo, theme_style=ft.TextThemeStyle.BODY_LARGE, color=paleta["azul medio"])
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
                        ft.Text(self.titulo, theme_style=ft.TextThemeStyle.BODY_LARGE, color=paleta["azul medio"]),
                        ft.Text(f'{self.valor:.0%}', theme_style=ft.TextThemeStyle.BODY_MEDIUM, color=paleta["laranjinha"]),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
                ft.ProgressBar(self.valor, color=paleta["azul medio"], bgcolor=ft.Colors.BLACK38, bar_height=7),
            ]
        )