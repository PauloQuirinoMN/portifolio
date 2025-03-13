import flet as ft

class SidebarCabecalho(ft.Container):
    """
    Cabeçalho da barra lateral.
    Aceita quaisquer argumentos válidos para ft.Container.

    """
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)
        self.expand = True
        self.alignment = ft.alignment.center
        self.padding = ft.padding.symmetric(vertical=20, horizontal=40)
        self.content = ft.Column(
            controls=[
                ft.Image(
                    src='images/face-1.jpg',
                    border_radius=ft.border_radius.all(100),
                    width=100,
                    badge=ft.Badge(small_size=10)
                ),
                ft.Text(value='Paulo Quirino', theme_style=ft.TextThemeStyle.BODY_LARGE, text_align=ft.TextAlign.JUSTIFY),
                ft.Text(value='Cientista de dados',theme_style=ft.TextThemeStyle.BODY_MEDIUM)
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )

class SidebarConteudo(ft.Container):
    """
    Conteúdo da barra lateral.
    Aceita quaisquer argumentos válidos para ft.Container.

    """ 
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.padding = ft.padding.all(20)
        self.bgcolor = ft.Colors.BLACK12

        local = ft.Container(
            ft.Column(
                controls=[
                    ft.Row( 
                        controls=[
                            ft.Text(value='Residência:', theme_style=ft.TextThemeStyle.BODY_LARGE),
                            ft.Text(value='Brasil', theme_style=ft.TextThemeStyle.BODY_MEDIUM)
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                    ),
                    ft.Row( 
                        controls=[
                            ft.Text(value='Cidade:', theme_style=ft.TextThemeStyle.BODY_LARGE),
                            ft.Text(value='Fortaleza', theme_style=ft.TextThemeStyle.BODY_MEDIUM)
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                    ),
                    ft.Row( 
                        controls=[
                            ft.Text(value='Idade:', theme_style=ft.TextThemeStyle.BODY_LARGE),
                            ft.Text(value='36', theme_style=ft.TextThemeStyle.BODY_MEDIUM)
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                    ),
                ]
            )
        )
        
        

        liguagens = ft.Row(
            controls=[
                
            ]
        )
        
        skills = ft.Container(content=ft.Text(value='comunicação'))
        
        tecnologias = ft.Container(content=ft.Text(value='SQL'))
        
        cv = ft.Container(content=ft.Text(value='currículo'))

        self.content = ft.Column(
            controls=[
                local,
                ft.Divider(height=30),
                liguagens,
                ft.Divider(height=30),
                skills,
                ft.Divider(height=30),
                tecnologias,
                ft.Divider(height=30),
                cv,
            ]
        )

class SidebarRodape(ft.Container):
    """
    Rodapé da barra lateral.
    Aceita quaisquer argumentos válidos para ft.Container.
    
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.padding = ft.padding.symmetric(vertical=10)
        self.content = ft.Row(
            controls=[
                ft.IconButton(
                    content=ft.Image(
                        src='icons/001-instagram.png', height=15, color=ft.Colors.WHITE,     
                    ),
                    url='https://www.instagram.com/pauloqneto/',
                ),
                ft.IconButton(
                    content=ft.Image(
                        src='icons/002-linkedin.png', height=15, color=ft.Colors.WHITE,   
                    ),
                    url='https://www.linkedin.com/feed/',
                ),
                ft.IconButton(
                    content=ft.Image(
                        src='icons/003-github.png', height=15, color=ft.Colors.WHITE,
                           
                    ),
                    url='https://github.com/PauloQuirinoMN',
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER
        )

class Sidebar(ft.Container):
    """
    Barra lateral.
    Aceita quaisquer argumentos válidos para ft.Container.
        
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.expand = True
        self.bgcolor = ft.Colors.BLACK
        self.content = ft.Column(
            controls=[
                SidebarCabecalho(),
                SidebarConteudo(),
                SidebarRodape(),
            ],
            expand=True
        )