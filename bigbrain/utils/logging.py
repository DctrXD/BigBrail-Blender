# =============================================================================
# utils/logging.py — Logging system for BigBrain
# =============================================================================

import bpy
import os
import datetime
import time
from ..i18n import get_text as _

# Log storage
log_entries = []
log_timestamps = []
log_levels = []

# Log level constants
DEBUG = 0
INFO = 1
WARNING = 2
ERROR = 3

# Log level names
LEVEL_NAMES = {
    DEBUG: "DEBUG",
    INFO: "INFO",
    WARNING: "WARNING",
    ERROR: "ERROR"
}

def log(message, level='INFO'):
    """
    Add a message to the log
    
    Args:
        message: The message to log
        level: Log level ('DEBUG', 'INFO', 'WARNING', 'ERROR') or integer
    """
    # Convert string level to integer
    if isinstance(level, str):
        level = level.upper()
        level_int = {
            'DEBUG': DEBUG,
            'INFO': INFO,
            'WARNING': WARNING,
            'ERROR': ERROR
        }.get(level, INFO)
    else:
        level_int = level
    
    # Get current timestamp
    timestamp = time.time()
    formatted_time = datetime.datetime.fromtimestamp(timestamp).strftime('%H:%M:%S')
    
    # Format the log entry
    level_name = LEVEL_NAMES.get(level_int, "INFO")
    formatted_message = f"[{formatted_time}] [{level_name}] {message}"
    
    # Store the log entry
    log_entries.append(formatted_message)
    log_timestamps.append(timestamp)
    log_levels.append(level_int)
    
    # Limit log size
    max_logs = 1000
    if len(log_entries) > max_logs:
        log_entries.pop(0)
        log_timestamps.pop(0)
        log_levels.pop(0)
    
    # Write to file if enabled
    if hasattr(bpy.context, "preferences"):
        prefs = bpy.context.preferences.addons.get("bigbrain")
        if prefs and hasattr(prefs.preferences, "log_to_file") and prefs.preferences.log_to_file:
            write_to_log_file(formatted_message)
    
    return formatted_message

def get_logs(level=None, count=None):
    """
    Get log entries filtered by level
    
    Args:
        level: Minimum log level to include (None for all)
        count: Maximum number of entries to return (None for all)
    
    Returns:
        List of log entries
    """
    if level is None:
        filtered_logs = log_entries
    else:
        # Convert string level to integer
        if isinstance(level, str):
            level = level.upper()
            level_int = {
                'DEBUG': DEBUG,
                'INFO': INFO,
                'WARNING': WARNING,
                'ERROR': ERROR,
                'ALL': None
            }.get(level, None)
        else:
            level_int = level
        
        if level_int is None:
            filtered_logs = log_entries
        else:
            # Filter by level
            filtered_logs = [
                entry for i, entry in enumerate(log_entries)
                if log_levels[i] >= level_int
            ]
    
    # Limit count
    if count is not None:
        filtered_logs = filtered_logs[-count:]
    
    return filtered_logs

def clear_logs():
    """Clear all log entries"""
    log_entries.clear()
    log_timestamps.clear()
    log_levels.clear()
    log("Logs cleared", 'INFO')

def write_to_log_file(message):
    """Write a message to the log file"""
    try:
        prefs = bpy.context.preferences.addons["bigbrain"].preferences
        log_location = getattr(prefs, "log_location", "")
        
        # Use default location if not specified
        if not log_location:
            log_location = os.path.join(bpy.utils.user_resource('SCRIPTS'), "addons", "bigbrain", "logs")
        
        # Create directory if it doesn't exist
        os.makedirs(log_location, exist_ok=True)
        
        # Create log filename with date
        date_str = datetime.datetime.now().strftime('%Y%m%d')
        log_file = os.path.join(log_location, f"bigbrain_{date_str}.log")
        
        # Append to log file
        with open(log_file, 'a', encoding='utf-8') as f:
            f.write(message + "\n")
    except Exception as e:
        # Don't use log() here to avoid recursion
        print(f"Error writing to log file: {e}")

def export_logs(filepath):
    """
    Export logs to a file
    
    Args:
        filepath: Path to save the log file
    
    Returns:
        True if successful, False otherwise
    """
    try:
        # Create directory if it doesn't exist
        directory = os.path.dirname(filepath)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)
        
        # Write logs to file
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(f"BigBrain Logs - {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("=" * 60 + "\n\n")
            
            for entry in log_entries:
                f.write(f"{entry}\n")
        
        log(f"Logs exported to {filepath}", 'INFO')
        return True
    except Exception as e:
        log(f"Error exporting logs: {e}", 'ERROR')
        return False

def register():
    """Register logging functionality"""
    log("Logging system initialized", 'INFO')

def unregister():
    """Unregister logging functionality"""
    pass