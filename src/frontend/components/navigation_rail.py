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
    rail = ft.NavigationRail(
        selected_index=None,
        label_type=ft.NavigationRailLabelType.ALL,
        min_width=100,
        min_extended_width=200,  # Increased slightly for better visibility
        group_alignment=-0.9,
        destinations=[
            ft.NavigationRailDestination(icon=ft.Icons.SCHOOL_OUTLINED, selected_icon=ft.Icons.SCHOOL, label="Faculty"),
            ft.NavigationRailDestination(icon=ft.Icons.PEOPLE_OUTLINE, selected_icon=ft.Icons.PEOPLE, label="Students"),
            ft.NavigationRailDestination(
                icon=ft.Icons.ADMIN_PANEL_SETTINGS_OUTLINED, selected_icon=ft.Icons.ADMIN_PANEL_SETTINGS, label="Staff"
            ),
            ft.NavigationRailDestination(
                icon=ft.Icons.MONETIZATION_ON_OUTLINED, selected_icon=ft.Icons.MONETIZATION_ON, label="Finance"
            ),
            ft.NavigationRailDestination(
                icon=ft.Icons.CONTACT_MAIL_OUTLINED, selected_icon=ft.Icons.CONTACT_MAIL, label="CRM"
            ),
        ],
        on_change=on_nav_change,
        leading=ft.Container(
            content=ft.Image(src=logo_path, width=80, height=80),
            padding=10,
            on_click=lambda _: page.push_route(route="/dashboard"),
            # on_click=lambda _: page.go("/dashboard"),
        ),
        bgcolor=ft.Colors.SURFACE,
    )

    return rail
