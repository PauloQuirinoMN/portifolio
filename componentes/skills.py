import flet as ft

class SkillRing(ft.Container):
    def __init__(self, titulo=str, valor=float):
        self.titulo = titulo
        self.valor = valor

        super().__init__()
        self.expand = True
        self.content = ft.Column(
            controls=[
                ft.Stack(
                    controls=[
                        ft.PieChart(
                            sections=[
                                ft.PieChartSection(value=self.valor, color=ft.Colors.PRIMARY, radius=5),    
                                ft.PieChartSection(value=1 - self.valor, color=ft.Colors.BLACK26, radius=5),
                            ],
                            sections_space=0,
                            center_space_color=ft.Colors.BLACK12,
                            height=70,
                        ),
                        ft.Container(
                            content=ft.Text(value=f'{self.valor:.0%}', theme_style=ft.TextThemeStyle.BODY_MEDIUM),
                            alignment=ft.alignment.center,
                            height=70,
                        )
                    ]
                ),
                ft.Text(value=self.titulo, theme_style=ft.TextThemeStyle.BODY_LARGE)
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )