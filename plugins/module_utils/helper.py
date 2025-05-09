from __future__ import annotations

__metaclass__ = type


def create_greeting(greeting, cat) -> str:
    """
    Create a greeting for a special kitty.

    Args:
        greeting (str): The greeting to use
        cat (str): Name of the cat

    Returns:
        str: Formatted greeting message
    """
    return f"{greeting}, {cat}!"
