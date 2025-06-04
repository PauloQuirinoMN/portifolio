import flet as ft
from componentes.skills import SkillRing, SkillProgressbar

paleta = {
    "verdemuitoescuro": "#111b21",
    "azul claro": "#6994ae",
    "azul medio": "#274e61",
    "morronzinho": "#444e21",
    "gelo": "#99a67e",
}

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
                ft.Text(value='Paulo Quirino Maciel Neto', theme_style=ft.TextThemeStyle.BODY_LARGE, color=paleta['gelo'], text_align=ft.TextAlign.JUSTIFY, size=25),
                
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
        self.expand = True
        


        local = ft.Container(
            ft.Column(
                controls=[
                    ft.Row( 
                        controls=[
                            ft.Text(value='Formação:', theme_style=ft.TextThemeStyle.BODY_LARGE, color=paleta['gelo'],),
                            ft.Text(value='Big Data e Inteligência Analítica',theme_style=ft.TextThemeStyle.BODY_MEDIUM, color=paleta['gelo'], size=15)
                        ],
                        alignment=ft.MainAxisAlignment.START
                    ),
                    ft.Row( 
                        controls=[
                            ft.Text(value='Residência:', theme_style=ft.TextThemeStyle.BODY_LARGE, color=paleta['gelo']),
                            ft.Text(value='Fortaleza, CE', theme_style=ft.TextThemeStyle.BODY_MEDIUM, color=paleta['gelo'],)
                        ],
                        alignment=ft.MainAxisAlignment.START
                    ),
                    ft.Row( 
                        controls=[
                            ft.Text(value='Nascimento:', theme_style=ft.TextThemeStyle.BODY_LARGE, color=paleta['gelo'],),
                            ft.Text(value='27/07/1988', theme_style=ft.TextThemeStyle.BODY_MEDIUM, color=paleta['gelo'],)
                        ],
                        alignment=ft.MainAxisAlignment.START
                    ),
                    ft.Row(
                        controls=[
                            
                        ]
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=0,
            )
        )
        
        
        sql = SkillRing(titulo='SQL', valor=0.35)
        powerbi = SkillRing(titulo='Powerbi', valor=0.40)
        python = SkillRing('Python', 0.65)
        excel = SkillRing('Excel', 0.70)

        liguagens = ft.Row(
            controls=[
                sql,
                powerbi,
                python,
                excel,
            ]
        )
        

        python = SkillProgressbar('UX (Python - Flet)', 0.75)
        sql = SkillProgressbar('LGPD', 0.92)
        py = SkillProgressbar('Git e GitHub', 0.85)
        s = SkillProgressbar('Metodologias Ágeis', 0.75)

        skills = ft.Column(
            controls=[
                python,
                sql,
                py,
                s,
            ]
        )
        
        tecnologias = ft.Column(
            controls=[
                ft.ListTile(
                    leading=ft.Icon(name=ft.Icons.CHECK, color=paleta['azul claro']),
                    title=ft.Text(value='Pensamento Analítico e Crítico', theme_style=ft.TextThemeStyle.BODY_MEDIUM, color=paleta['gelo']),
                ),
                ft.ListTile(
                    leading=ft.Icon(name=ft.Icons.CHECK, color=paleta['azul claro']),
                    title=ft.Text(value='Curiosidade e Aprendizado Contínuo', theme_style=ft.TextThemeStyle.BODY_MEDIUM, color=paleta['gelo']),
                ),
                ft.ListTile(
                    leading=ft.Icon(name=ft.Icons.CHECK, color=paleta['azul claro']),
                    title=ft.Text(value='Trabalho em Equipe', theme_style=ft.TextThemeStyle.BODY_MEDIUM, color=paleta['gelo']),
                ),
                ft.ListTile(
                    leading=ft.Icon(name=ft.Icons.CHECK, color=paleta['azul claro']),
                    title=ft.Text(value='Resiliência e Adaptabilidade', theme_style=ft.TextThemeStyle.BODY_MEDIUM, color=paleta['gelo']),
                ),
                ft.ListTile(
                    leading=ft.Icon(name=ft.Icons.CHECK, color=paleta['azul claro']),
                    title=ft.Text(value='storytelling', theme_style=ft.TextThemeStyle.BODY_MEDIUM,color=paleta['gelo']),
                ), 
                ft.ListTile(
                    leading=ft.Icon(name=ft.Icons.CHECK, color=paleta['azul claro']),
                    title=ft.Text(value='Ética e Consciência de Viés', theme_style=ft.TextThemeStyle.BODY_MEDIUM,color=paleta['gelo']),
                ),
                ft.ListTile(
                    leading=ft.Icon(name=ft.Icons.CHECK, color=paleta['azul claro']),
                    title=ft.Text(value='Empatia', theme_style=ft.TextThemeStyle.BODY_MEDIUM,color=paleta['gelo']),
                ),               
            ],
            alignment=ft.MainAxisAlignment.START,
            spacing=0,
        )
        

        self.content = ft.Column(
            controls=[
                local,
                ft.Divider(height=30),
                ft.Text(value="SOBRE MIM ", size=20, color=paleta['azul medio']),
                sobre,
                ft.Divider(height=30),
                liguagens,
                ft.Divider(height=30),
                skills,
                ft.Divider(height=30),
                tecnologias,
                ft.Divider(height=30),
            ],
            scroll=ft.ScrollMode.AUTO,
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


sobre = ft.Text(
value="" \
"Em 2020, estava no 5º semestre da graduação em Engenharia de Energias na UNILAB, "
"a pandemia me levou a repensar minha carreira. "\
"Foi nesse período que descobri meu interesse pela Ciência de dados "\
"e decidi fazer a transição para a área. "\
"Em 2021, iniciei minha graduação em Big Data e Inteligência Analítica (UNIASSELVI), " \
"onde adquiri bases teóricas solidas em ciência e análise de dados e tecnologias emergentes. " \
"Paralelamente, dediquei-me ao estudo prático de ferramentas como "\
 "Python, SQL e Power BI para consolidar meu conhecimento técnico.", color=paleta['gelo'], text_align=ft.TextAlign.JUSTIFY)  

   
class Sidebar(ft.Container):
    """
    Barra lateral.
    Aceita quaisquer argumentos válidos para ft.Container. 
    """

    # https://sites.google.com/site/gdocs2direct/?pli=1j
    
    def __init__(self, **kwargs):   
        super().__init__(**kwargs)

        cabecalho = SidebarCabecalho()
        conteudo = SidebarConteudo()
        rodape = SidebarRodape()


        cv = ft.TextButton(
            text='DOWNLOAD CV',
            style=ft.ButtonStyle(color=ft.Colors.GREY),
            icon=ft.Icons.DOWNLOAD,
            icon_color=ft.Colors.GREY,
            url='https://drive.google.com/uc?export=download&id=14Sby_XwtfLnMh4paW1Ifn8mQMfSPU-hK',
        )

        self.content = ft.Column(
            controls=[
                cabecalho,
                conteudo,
                ft.Row(
                    controls=[
                        cv, 
                        rodape, 
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_EVENLY
                )                             
            ],
            spacing=0,
            expand=True
        )
        