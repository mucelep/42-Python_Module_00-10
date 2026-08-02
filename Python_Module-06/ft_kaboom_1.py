def imp() -> None:
    from alchemy.grimoire.dark_spellbook import dark_spell_record
    dark_spell_record("Love", "Hair, Frogs and eyeball")


print("=== Kaboom 1 ===")
print("Access to alchemy/grimoire/dark_spellbook.py directly")
print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")
imp()
