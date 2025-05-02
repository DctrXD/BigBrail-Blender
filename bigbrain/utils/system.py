# =============================================================================
# utils/system.py — System operations (restart Blender, check drivers)
# =============================================================================

import bpy
import os
import sys
import subprocess
import platform
import webbrowser
from ..i18n import get_text as _

def restart_blender():
    """
    Restart Blender with the same file
    
    Returns:
        True if restart initiated, False otherwise
    """
    from .. import utils
    
    # Get current file path
    current_file = bpy.data.filepath
    
    # Get Blender executable path
    blender_exe = bpy.app.binary_path
    
    # Check if paths exist
    if not os.path.exists(blender_exe):
        utils.log(f"Cannot restart: Blender executable not found at {blender_exe}", 'ERROR')
        return False
    
    # Build command
    cmd = [blender_exe]
    
    # Add file if one is open
    if current_file and os.path.exists(current_file):
        cmd.append(current_file)
    
    try:
        # Start new Blender process
        if platform.system() == "Windows":
            subprocess.Popen(cmd, shell=True)
        else:
            subprocess.Popen(cmd)
        
        # Quit current Blender
        utils.log("Restarting Blender...", 'INFO')
        bpy.ops.wm.quit_blender()
        
        return True
    except Exception as e:
        utils.log(f"Error restarting Blender: {e}", 'ERROR')
        return False

def open_driver_download_page():
    """
    Open the appropriate driver download page based on GPU vendor
    
    Returns:
        True if page opened, False otherwise
    """
    from . import diagnostics
    from .. import utils
    
    # Get GPU info
    gpu_info = diagnostics.get_gpu_info()
    vendor = gpu_info.get("vendor", "").lower()
    
    # Determine URL based on vendor
    url = None
    
    if "nvidia" in vendor:
        url = "https://www.nvidia.com/Download/index.aspx"
    elif "amd" in vendor or "ati" in vendor:
        url = "https://www.amd.com/en/support"
    elif "intel" in vendor:
        url = "https://www.intel.com/content/www/us/en/download-center/home.html"
    else:
        utils.log(f"Unknown GPU vendor: {vendor}", 'ERROR')
        return False
    
    # Open URL in browser
    try:
        webbrowser.open(url)
        utils.log(f"Opened driver download page: {url}", 'INFO')
        return True
    except Exception as e:
        utils.log(f"Error opening driver download page: {e}", 'ERROR')
        return False

def check_for_updates():
    """
    Check for BigBrain updates
    
    Returns:
        Dictionary with update information
    """
    from .. import utils
    
    # Get current version
    try:
        from .. import bl_info
        current_version = bl_info.get("version", (0, 0, 0))
    except:
        current_version = (0, 0, 0)
    
    current_version_str = ".".join(str(v) for v in current_version)
    
    # Placeholder for actual update check
    # In a real implementation, this would connect to a server or GitHub API
    # to check for the latest version
    
    # Simulate update check
    result = {
        "current_version": current_version_str,
        "latest_version": current_version_str,
        "update_available": False,
        "download_url": "",
        "release_notes": "",
        "error": None
    }
    
    utils.log(f"Update check complete. Current version: {current_version_str}", 'INFO')
    
    return result

def open_addon_directory():
    """
    Open the BigBrain addon directory in file explorer
    
    Returns:
        True if directory opened, False otherwise
    """
    from .. import utils
    
    # Get addon directory
    addon_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    
    if not os.path.exists(addon_dir):
        utils.log(f"Addon directory not found: {addon_dir}", 'ERROR')
        return False
    
    # Open directory
    try:
        if platform.system() == "Windows":
            os.startfile(addon_dir)
        elif platform.system() == "Darwin":  # macOS
            subprocess.Popen(["open", addon_dir])
        else:  # Linux
            subprocess.Popen(["xdg-open", addon_dir])
        
        utils.log(f"Opened addon directory: {addon_dir}", 'INFO')
        return True
    except Exception as e:
        utils.log(f"Error opening addon directory: {e}", 'ERROR')
        return False

def register():
    """Register system functionality"""
    from .. import utils
    utils.log("System utilities initialized", 'INFO')

def unregister():
    """Unregister system functionality"""
    pass