from .dark_spellbook import dark_spell_allowed_ingredients


def dark_validate_ingredients(ingredients: str) -> str:
    allowed = dark_spell_allowed_ingredients()
    ingredients_lower = ingredients.lower()
    for item in allowed:
        if item.lower() in ingredients_lower:
            return "VALID"
    return "INVALID"
