import flet as ft

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
                                ft.PieChartSection(value=self.valor, color=ft.Colors.WHITE, radius=5),    
                                ft.PieChartSection(value=1 - self.valor, color=ft.Colors.BLACK26, radius=5),
                            ],
                            sections_space=0,
                            center_space_color=ft.Colors.BLACK12,
                            height=70,
                        ),
                        ft.Container(
                            content=ft.Text(value=f'{self.valor:.0%}', theme_style=ft.TextThemeStyle.BODY_MEDIUM, color=ft.Colors.WHITE),
                            alignment=ft.alignment.center,
                            height=70,
                        )
                    ]
                ),
                ft.Text(value=self.titulo, theme_style=ft.TextThemeStyle.BODY_LARGE, color=ft.Colors.WHITE)
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
                        ft.Text(self.titulo, theme_style=ft.TextThemeStyle.BODY_LARGE, color=ft.Colors.WHITE),
                        ft.Text(f'{self.valor:.0%}', theme_style=ft.TextThemeStyle.BODY_MEDIUM, color=ft.Colors.WHITE),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
                ft.ProgressBar(self.valor, color=ft.Colors.PRIMARY, bgcolor=ft.Colors.BLACK26),
                ft.Divider(height=10, color=ft.Colors.BLACK12)
            ]
        )