# =============================================================================
# i18n/__init__.py — Internationalization support
# =============================================================================

import bpy
import os
from . import languages

# Current active language
current_language = 'EN'

def get_system_language():
    """
    Attempts to detect the system language and map it to a supported language code
    Returns a supported language code (defaults to 'EN' if not found)
    """
    import locale
    
    try:
        # Get system locale
        system_locale = locale.getdefaultlocale()[0]
        if system_locale:
            # Extract language code (first 2 characters)
            lang_code = system_locale[:2].upper()
            
            # Map to supported languages
            lang_map = {
                'EN': 'EN',  # English
                'PT': 'PT',  # Portuguese
                'ES': 'ES',  # Spanish
                'FR': 'FR',  # French
                'DE': 'DE',  # German
                'IT': 'IT',  # Italian
                'JA': 'JP',  # Japanese
            }
            
            return lang_map.get(lang_code, 'EN')
    except:
        pass
    
    # Default to English if detection fails
    return 'EN'

def set_language(lang_code):
    """Sets the current language"""
    global current_language
    if lang_code in languages.TEXTS:
        current_language = lang_code
        return True
    return False

def get_language():
    """Returns the current language code"""
    return current_language

def get_text(key, lang=None):
    """
    Gets translated text for a key in the specified language
    If lang is None, uses the current language
    Falls back to English if the key is not found
    """
    if lang is None:
        lang = current_language
    
    # Try to get text in requested language
    lang_dict = languages.TEXTS.get(lang, {})
    text = lang_dict.get(key)
    
    # Fall back to English if not found
    if text is None and lang != 'EN':
        text = languages.TEXTS.get('EN', {}).get(key)
    
    # Return key as fallback if still not found
    return text if text is not None else key

def register():
    # Auto-detect system language on first load
    prefs = bpy.context.preferences.addons.get("bigbrain")
    if prefs:
        # If user has already set a language preference, use that
        set_language(prefs.preferences.language)
    else:
        # Otherwise try to detect system language
        set_language(get_system_language())

def unregister():
    pass