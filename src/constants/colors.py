# Default Color Palette (fallback values)
DEFAULTS = {
    "text": "000000",
    "button": "FFFFFF",
    "background": "82150D"
}

PALETTE = {
    """
    Instructions:
    - Index 0: Text color
    - Index 1: Button color
    - Index 2: Background color
    - Index 3: ? 
    - Index 4: ?
    - Index 5 (optional): ?
    """

    # The colors will still be rearranged to be more visually appealing

    # Abend Diabolos Pwuhn | The Unyielding Forge
    "abend": ("981D15",   # Dark red
              "10060C",   # Black
              "E64E17",   # Dark orange
              "331403",   # Chocolate brown
              "53DCEB"), # Bright blue
    
    # Bastest Chiusa | Keeper of Hearth and Throne
    "bastet": ("DFBE2A",  # Dark Yellow
               "B658E9", # Bright Purple
               "C3DEE4", # Light Blue
               "EED5D5", # Gray
               "FFFBG"),  # Grayish White (Note: Contains invalid hex character 'G')
    
    # Picking Thoth | Lord of Fire
    "thoth": ("FD922E",   # Dark Orange 
              "F0C537",   # Yellow
              "F8D471",   # Pale Yellow 
              "FAF6EC",   # Light Gray
              "FFFFFF"),  # White  

    # Nika Ra Dev | The Unbound Sun
    "nika": ("EE8637",    # Pale Orange
             "EE5634",    # Redish Orange
             "F8BF2E",    # Dark Yellow
             "ECCD2D",    # Yellow
             "FCE19E"),   # Pale Yellow
    
    # Eliaeb Esecuz | The faceless one
    "eliaeb": ("FFFFFF",), # White (comma makes it a tuple)
    # add more shades of white (gray) if needed
    # maybe black for the text?

    # Hathor Nuwa Sequel | The Radiant Muse
    "sequel": ("F77F9B",  # Light pink
               "EE3131", # Salmon red
               "9BF79E",  # Light-mint green
               "FCD968",  # Light-pale yellow
               "F8E9A1"), # Light gray
    
    # Sedah Ulink | The Judge of the Departed
    "ulink": ("1C1C1C",   # Dark gray
              "000B53",   # Dark blue
              "2B0745",   # Dark purple
              "B8860B"),  # Dark yellow
    
    # Abraxas Wa Attesa | The Twin-Edged Scale
    "abraxas": ("000000", # Black
                "808080", # Gray
                "FFFFFF"), # White
    
    # Rath Re Ply | The Keeper of Secrets
    "rath": ("9B8C06",   # Dark yellow-green
             "5D5D5D",   # Gray
             "11071D",   # Darker purple
             "210323"),  # Dark purple
}

def get_palette(god="abend"):
    """
    Returns a color dictionary for the specified god.
    
    Registered Gods:
    - abend
    - bastet
    - thoth
    - nika
    - eliaeb
    - sequel
    - ulink
    - abraxas
    - rath
    - ?

    Usage:
    p = get_palette("thoth") 
    self.screen.fill(f"#{p['background']}"
    text_surface = font.render("Hello", True, f"#{p['text']}")  
    pygame.draw.rect(self.screen, f"#{p['button']}", button_rect)
    """
    try:
        colors = PALETTE[god]
        return {
            "text": colors[0] if len(colors) > 0 else DEFAULTS["text"],
            "button": colors[1] if len(colors) > 1 else DEFAULTS["button"],
            "background": colors[2] if len(colors) > 2 else DEFAULTS["background"],
            # "?????": colors[3] if len(colors) > 3 else DEFAULTS["?????"]  - etc
        }
    except KeyError as e:
        print(f"\nKeyError: {e}.\n Palette for god '{god}' not found. Using default colors.")
        print(f"Check {__file__} for debugging.\n")
        return DEFAULTS.copy()

# Example usage:
# current_colors = get_palette("thoth")
# print(f"Text color: #{current_colors['text']}")
# print(f"Button color: #{current_colors['button']}")
# print(f"Background color: #{current_colors['background']}")