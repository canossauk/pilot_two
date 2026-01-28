#
#  Import LIBRARIES
import os

import flet as ft

#
#  Import FILES
#  __________________________________
#

# Constants
FACULTY_VIEW = "Faculty Management"
STUDENTS_VIEW = "Student Directory"
STAFF_VIEW = "Staff Administration"
FINANCE_VIEW = "Financial Overview"
CRM_VIEW = "Constituent Relationship Management"


def create_sidebar(page: ft.Page, content_area: ft.Container):
    """
    Creates the navigation rail and handles the logic for switching views.
    Accepts 'page' (for navigation) and 'content_area' (to update the UI).
    """

    # 1. Logic: callback logic - Handle Navigation Changes
    def on_nav_change(e) -> None:
        index = e.control.selected_index
        title = ""

        # Determine Title
        if index == 0:
            title = FACULTY_VIEW
        elif index == 1:
            title = STUDENTS_VIEW
        elif index == 2:
            title = STAFF_VIEW
        elif index == 3:
            title = FINANCE_VIEW
        elif index == 4:
            title = CRM_VIEW

        # Update the Content Area (passed from main.py)
        content_area.content = ft.Column(
            controls=[
                ft.Text(value=title, style=ft.TextThemeStyle.HEADLINE_MEDIUM, color=ft.Colors.PRIMARY),
                ft.Divider(),
                ft.Text(value=f"Content for {title} will appear here.", style=ft.TextThemeStyle.BODY_MEDIUM),
            ]
        )
        content_area.update()

    # 2. Asset: Resolve Logo Path
    # Note: os.getcwd() assumes you run main.py from the project root
    logo_path = os.path.abspath("support_files/ila.png")

    # 3. Component: The Navigation Rail
    # Define text styles for labels
    label_text_style = ft.TextStyle(size=16, weight=ft.FontWeight.W_500, color=ft.Colors.WHITE)

    # Helper to create styled destinations
    def create_dest(icon: str, selected_icon: str, label: str):
        return ft.NavigationRailDestination(
            icon=ft.Icon(icon, size=32, color=ft.Colors.WHITE70),
            selected_icon=ft.Icon(selected_icon, size=32, color=ft.Colors.WHITE),
            label=ft.Text(label, style=label_text_style),
        )

    rail = ft.NavigationRail(
        selected_index=None,
        label_type=ft.NavigationRailLabelType.ALL,
        min_width=100,
        min_extended_width=220,
        group_alignment=-0.9,
        destinations=[
            create_dest(ft.Icons.SCHOOL_OUTLINED, ft.Icons.SCHOOL, "Faculty"),
            create_dest(ft.Icons.PEOPLE_OUTLINE, ft.Icons.PEOPLE, "Students"),
            create_dest(ft.Icons.ADMIN_PANEL_SETTINGS_OUTLINED, ft.Icons.ADMIN_PANEL_SETTINGS, "Staff"),
            create_dest(ft.Icons.MONETIZATION_ON_OUTLINED, ft.Icons.MONETIZATION_ON, "Finance"),
            create_dest(ft.Icons.CONTACT_MAIL_OUTLINED, ft.Icons.CONTACT_MAIL, "CRM"),
        ],
        on_change=on_nav_change,
        leading=ft.Column(
            controls=[
                ft.IconButton(
                    icon=ft.Icons.MENU,
                    icon_size=30,
                    icon_color=ft.Colors.WHITE,
                    on_click=lambda e: setattr(rail, "extended", not rail.extended) or rail.update(),
                ),
                ft.Container(
                    content=ft.Image(src=logo_path, width=100, height=100),
                    padding=10,
                    on_click=lambda _: page.push_route(route="/dashboard"),
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        bgcolor="#071B63",
        extended=True,
    )

    return rail
