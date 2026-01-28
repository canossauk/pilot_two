import flet as ft

class UniversityTheme:
    # Color Palette based on "University" Professional look
    # Deep Navy Blue for primary, White/Grey for background, Gold/Amber for accents if needed
    primary = "#1565C0" # Blue 800
    primary_container = "#0D47A1" # Blue 900
    secondary = "#FFC107" # Amber 500
    background = "#F5F5F7" # Light greyish white
    surface = "#FFFFFF"
    error = "#B00020"
    on_primary = "#FFFFFF"
    on_secondary = "#000000"
    
    theme = ft.Theme(
        color_scheme=ft.ColorScheme(
            primary=primary,
            primary_container=primary_container,
            secondary=secondary,
            # background=background, # Removed as it caused TypeError
            surface=surface,
            error=error,
            on_primary=on_primary,
            on_secondary=on_secondary,
        ),
        visual_density=ft.VisualDensity.ADAPTIVE_PLATFORM_DENSITY,
        use_material3=True,
    )
