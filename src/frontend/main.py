#
#  Import LIBRARIES
import flet as ft
import httpx

#  Import FILES
from components.navigation_rail import create_sidebar
from utilities.styles import UniversityTheme

#

# --- Imports ---

# Import the function we created in Step 2


async def main(page: ft.Page) -> None:
    # 1. Page Configuration
    page.title = "School Management System"
    page.theme = UniversityTheme.theme
    page.padding = 0
    page.window.min_width = 800
    page.window.min_height = 600

    # 2. Backend Check
    async def check_backend_status() -> bool:
        try:
            async with httpx.AsyncClient() as client:
                response: httpx.Response = await client.get(url="http://localhost:8000/health", timeout=1.0)
                return response.status_code == 200
        except httpx.RequestError:
            return False

    if not await check_backend_status():
        print("Warning: Backend not reachable. Running in offline/UI-only mode.")

    # 3. Main Content Area
    # We define this first so we can pass it to the sidebar
    content_area = ft.Container(
        expand=True,
        padding=20,
        bgcolor=ft.Colors.BLUE_ACCENT_700,  # Using the constant directly for visibility
        content=ft.Column(
            controls=[
                ft.Text(value="Welcome to the Dashboard", theme_style=ft.TextThemeStyle.HEADLINE_MEDIUM),
                ft.Text(value="Select an option from the navigation menu.", theme_style=ft.TextThemeStyle.BODY_LARGE),
            ]
        ),
    )

    # 4. Create Sidebar (Navigation Rail)
    # We pass 'page' and 'content_area' so the sidebar knows what to update
    rail = create_sidebar(page=page, content_area=content_area)

    # 5. Layout
    page.add(
        ft.Row(
            controls=[
                rail,
                ft.VerticalDivider(width=1),
                content_area,
            ],
            expand=True,
        )
    )

    page.update()  # pyright: ignore[reportUnknownMemberType]


if __name__ == "__main__":
    ft.run(main=main)  # pyright: ignore[reportUnknownMemberType]

#
#  Import LIBRARIES
#  Import FILES

#  __________________________________
#
