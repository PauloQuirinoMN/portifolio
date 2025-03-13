import flet as ft

class SkillRing(ft.Container):
    def __init__(self, **kwargs):
        super.__init__(**kwargs)
        self.content = ft.Column(
                    controls=[
                        ft.Stack(
                            controls=[
                                ft.PieChart(
                                    sections=[
                                        ft.PieChartSection(value=100, color=ft.Colors.PRIMARY, radius=5),
                                         ft.PieChartSection(value=0, color=ft.Colors.BLACK26, radius=5),
                                    ],
                                    sections_space=0,
                                    center_space_color=ft.Colors.BLACK12,
                                    height=70,
                                ),
                                ft.Container(
                                    content=ft.Text(value='100%', theme_style=ft.TextThemeStyle.BODY_MEDIUM),
                                    alignment=ft.alignment.center,
                                    height=70,
                                )
                            ]
                        ),
                        ft.Text(value='Português', theme_style=ft.TextThemeStyle.BODY_LARGE)
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    expand=True,
                )