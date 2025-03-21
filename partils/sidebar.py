import flet as ft
from componentes.skills import SkillRing, SkillProgressbar

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
                    src='images/img3.jpeg',
                    border_radius=ft.border_radius.all(100),
                    width=100,
                    badge=ft.Badge(small_size=10)
                ),
                ft.Text(value='Paulo Quirino Maciel Neto', theme_style=ft.TextThemeStyle.BODY_LARGE, color=ft.Colors.WHITE, text_align=ft.TextAlign.JUSTIFY),
                ft.Text(value='Cientista de dados',theme_style=ft.TextThemeStyle.BODY_MEDIUM, color=ft.Colors.WHITE)
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
        self.height = 500


        local = ft.Container(
            ft.Column(
                controls=[
                    ft.Row( 
                        controls=[
                            ft.Text(value='Residência:', theme_style=ft.TextThemeStyle.BODY_LARGE, color=ft.Colors.WHITE),
                            ft.Text(value='Brasil', theme_style=ft.TextThemeStyle.BODY_MEDIUM, color=ft.Colors.WHITE)
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                    ),
                    ft.Row( 
                        controls=[
                            ft.Text(value='Cidade:', theme_style=ft.TextThemeStyle.BODY_LARGE, color=ft.Colors.WHITE),
                            ft.Text(value='Fortaleza', theme_style=ft.TextThemeStyle.BODY_MEDIUM, color=ft.Colors.WHITE)
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                    ),
                    ft.Row( 
                        controls=[
                            ft.Text(value='Nascimento:', theme_style=ft.TextThemeStyle.BODY_LARGE, color=ft.Colors.WHITE),
                            ft.Text(value='1988', theme_style=ft.TextThemeStyle.BODY_MEDIUM, color=ft.Colors.WHITE)
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                    ),
                ]
            )
        )
        
        
        sql = SkillRing(titulo='SQL', valor=0.65)
        powerbi = SkillRing(titulo='Powerbi', valor=0.4)
        python = SkillRing('Python', 0.75)

        liguagens = ft.Row(
            controls=[
                sql,
                powerbi,
                python,
            ],
            expand=True
        )
        

        python = SkillProgressbar('Python', 1.0)
        sql = SkillProgressbar('SQL', 0.75)
        py = SkillProgressbar('Python', 0.85)
        s = SkillProgressbar('SQL', 0.75)
        pyt = SkillProgressbar('Python', 0.69)
        sq = SkillProgressbar('SQL', 0.75)

        skills = ft.Column(
            controls=[
                python,
                sql,
                py,
                s,
                pyt,
                sq
            ]
        )
        
        tecnologias = ft.Column(
            controls=[
                ft.ListTile(
                    leading=ft.Icon(name=ft.Icons.CHECK, color=ft.Colors.WHITE),
                    title=ft.Text(value='Flet', theme_style=ft.TextThemeStyle.BODY_MEDIUM, color=ft.Colors.WHITE),
                ),
                ft.ListTile(
                    leading=ft.Icon(name=ft.Icons.CHECK, color=ft.Colors.WHITE),
                    title=ft.Text(value='excel', theme_style=ft.TextThemeStyle.BODY_MEDIUM, color=ft.Colors.WHITE),
                ),
                ft.ListTile(
                    leading=ft.Icon(name=ft.Icons.CHECK, color=ft.Colors.WHITE),
                    title=ft.Text(value='LGPD', theme_style=ft.TextThemeStyle.BODY_MEDIUM, color=ft.Colors.WHITE),
                ),
                ft.ListTile(
                    leading=ft.Icon(name=ft.Icons.CHECK, color=ft.Colors.WHITE),
                    title=ft.Text(value='pandas', theme_style=ft.TextThemeStyle.BODY_MEDIUM, color=ft.Colors.WHITE),
                ),
                ft.ListTile(
                    leading=ft.Icon(name=ft.Icons.CHECK, color=ft.Colors.WHITE),
                    title=ft.Text(value='storytelling', theme_style=ft.TextThemeStyle.BODY_MEDIUM,color=ft.Colors.WHITE),
                ),                
            ],
            alignment=ft.MainAxisAlignment.START,
            spacing=0,
        )
        

        # https://sites.google.com/site/gdocs2direct/?pli=1j
        cv = ft.TextButton(
            text='DOWNLOAD CV',
            style=ft.ButtonStyle(color=ft.Colors.GREY),
            icon=ft.Icons.DOWNLOAD,
            icon_color=ft.Colors.GREY,
            url='https://drive.google.com/uc?export=download&id=14Sby_XwtfLnMh4paW1Ifn8mQMfSPU-hK',
        )

        self.content = ft.Column(
            scroll=ft.ScrollMode.AUTO,
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
            ],
            expand=True
        )

class SidebarRodape(ft.Container):
    """
    Rodapé da barra lateral.
    Aceita quaisquer argumentos válidos para ft.Container.
    
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.expand=True,
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
        self.bgcolor = ft.Colors.BLACK
        self.expand = True
        self.content = ft.Column(
            controls=[
                SidebarCabecalho(), # Fixo
                SidebarConteudo(),
                SidebarRodape(), # Fixo
            ],
            expand=True,
            
        )