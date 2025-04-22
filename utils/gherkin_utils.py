from typing import Dict, List, Any
import re

def parse_table(table: List[Dict[str, str]]) -> Dict[str, str]:
    """
    Parse a Gherkin table into a dictionary.
    
    Args:
        table: List of dictionaries representing table rows
        
    Returns:
        Dictionary with keys and values from the table
    """
    return {row['key']: row['value'] for row in table}

def parse_data_table(table: List[Dict[str, str]]) -> List[Dict[str, str]]:
    """
    Parse a Gherkin data table into a list of dictionaries.
    
    Args:
        table: List of dictionaries representing table rows
        
    Returns:
        List of dictionaries with data from the table
    """
    return table

def format_step_text(text: str) -> str:
    """
    Format step text to be more readable in logs and reports.
    
    Args:
        text: Original step text
        
    Returns:
        Formatted step text
    """
    # Remove quotes around parameters
    text = re.sub(r'"([^"]*)"', r'\1', text)
    # Capitalize first letter
    text = text[0].upper() + text[1:]
    return text

def extract_parameters(text: str) -> List[str]:
    """
    Extract parameters from a step text.
    
    Args:
        text: Step text with parameters
        
    Returns:
        List of extracted parameters
    """
    return re.findall(r'"([^"]*)"', text)

def format_table_for_logging(table: List[Dict[str, str]]) -> str:
    """
    Format a table for logging purposes.
    
    Args:
        table: List of dictionaries representing table rows
        
    Returns:
        Formatted string representation of the table
    """
    if not table:
        return ""
    
    headers = list(table[0].keys())
    max_lengths = {header: len(header) for header in headers}
    
    # Calculate maximum lengths
    for row in table:
        for header in headers:
            max_lengths[header] = max(max_lengths[header], len(str(row[header])))
    
    # Create format string
    format_str = " | ".join(f"{{:<{max_lengths[header]}}}" for header in headers)
    
    # Create header separator
    separator = "-+-".join("-" * max_lengths[header] for header in headers)
    
    # Build table string
    table_str = [format_str.format(*headers), separator]
    for row in table:
        table_str.append(format_str.format(*[row[header] for header in headers]))
    
    return "\n".join(table_str) 