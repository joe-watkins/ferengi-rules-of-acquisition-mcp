"""
Ferengi Rules of Acquisition MCP Server

An MCP server that provides access to the Ferengi Rules of Acquisition
from Star Trek. Query rules by number, search by keyword, or get random rules.
"""

import json
from pathlib import Path
from typing import Optional
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("Ferengi Rules of Acquisition")

# Load the rules data
DATA_PATH = Path(__file__).parent / "data" / "ferengi-rules-of-acquisition.json"

def load_rules():
    """Load the Ferengi Rules of Acquisition from JSON file."""
    with open(DATA_PATH, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data['ferengi_rules_of_acquisition']

# Load rules at startup
RULES = load_rules()


@mcp.tool()
def get_rule(rule_number: int) -> str:
    """
    Get a specific Ferengi Rule of Acquisition by its number.
    
    Args:
        rule_number: The rule number (1-286)
    
    Returns:
        The rule text with its number
    """
    for rule in RULES:
        if rule['id'] == rule_number:
            return f"Rule #{rule['id']}: {rule['rule']}"
    
    return f"Rule #{rule_number} not found. Valid rules are 1-286."


@mcp.tool()
def search_rules(keyword: str) -> str:
    """
    Search for Ferengi Rules containing a specific keyword.
    
    Args:
        keyword: The word or phrase to search for in the rules
    
    Returns:
        A list of matching rules
    """
    keyword_lower = keyword.lower()
    matches = [
        rule for rule in RULES 
        if keyword_lower in rule['rule'].lower()
    ]
    
    if not matches:
        return f"No rules found containing '{keyword}'"
    
    result = f"Found {len(matches)} rule(s) containing '{keyword}':\n\n"
    for rule in matches:
        result += f"Rule #{rule['id']}: {rule['rule']}\n\n"
    
    return result.strip()


@mcp.tool()
def get_random_rule() -> str:
    """
    Get a random Ferengi Rule of Acquisition.
    
    Returns:
        A randomly selected rule
    """
    import random
    rule = random.choice(RULES)
    return f"Rule #{rule['id']}: {rule['rule']}"


@mcp.tool()
def list_all_rules() -> str:
    """
    Get all Ferengi Rules of Acquisition.
    
    Returns:
        A complete list of all 286 rules
    """
    result = "Complete Ferengi Rules of Acquisition:\n\n"
    for rule in RULES:
        result += f"Rule #{rule['id']}: {rule['rule']}\n\n"
    
    return result.strip()


@mcp.tool()
def get_rules_count() -> str:
    """
    Get the total number of Ferengi Rules of Acquisition.
    
    Returns:
        The count of rules
    """
    return f"There are {len(RULES)} Ferengi Rules of Acquisition."


@mcp.tool()
def get_rules_by_range(start: int, end: int) -> str:
    """
    Get Ferengi Rules within a specific range.
    
    Args:
        start: Starting rule number
        end: Ending rule number
    
    Returns:
        Rules within the specified range
    """
    if start < 1 or end > 286 or start > end:
        return "Invalid range. Please use numbers between 1 and 286, with start <= end."
    
    matches = [rule for rule in RULES if start <= rule['id'] <= end]
    
    result = f"Rules #{start} to #{end}:\n\n"
    for rule in matches:
        result += f"Rule #{rule['id']}: {rule['rule']}\n\n"
    
    return result.strip()


# Run the server
if __name__ == "__main__":
    mcp.run()
