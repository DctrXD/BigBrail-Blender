# =============================================================================
# version.py — Version information and update checking
# =============================================================================

import bpy
import requests
import threading
from datetime import datetime

# Current version information
VERSION = (2, 0, 0)
VERSION_STRING = ".".join(map(str, VERSION))
RELEASE_DATE = "2023-11-15"  # Data atualizada
GITHUB_REPO = "DctrXD/BigBrain"
GITHUB_API_URL = f"https://api.github.com/repos/{GITHUB_REPO}/releases/latest"

# For storing update check results
update_available = False
latest_version = None
latest_url = None
last_check_time = None

def get_version_tuple():
    """Returns the current version as a tuple"""
    return VERSION

def get_version_string():
    """Returns the current version as a string"""
    return VERSION_STRING

def version_to_string(version_tuple):
    """Converts a version tuple to string"""
    return ".".join(map(str, version_tuple))

def string_to_version(version_string):
    """Converts a version string to tuple"""
    try:
        return tuple(map(int, version_string.split('.')))
    except:
        return (0, 0, 0)

def is_newer_version(version_a, version_b):
    """Checks if version_a is newer than version_b"""
    return version_a > version_b

def check_for_updates(callback=None):
    """
    Checks GitHub for newer versions of the addon
    If callback is provided, it will be called with (has_update, version, url)
    """
    global update_available, latest_version, latest_url, last_check_time
    
    def _check_thread():
        global update_available, latest_version, latest_url, last_check_time
        try:
            response = requests.get(GITHUB_API_URL, timeout=5)
            if response.status_code == 200:
                data = response.json()
                latest_tag = data.get('tag_name', '').lstrip('v')
                latest_version_tuple = string_to_version(latest_tag)
                
                update_available = is_newer_version(latest_version_tuple, VERSION)
                latest_version = latest_tag
                latest_url = data.get('html_url')
                last_check_time = datetime.now()
                
                if callback:
                    # Execute callback on the main thread
                    bpy.app.timers.register(
                        lambda: callback(update_available, latest_version, latest_url),
                        first_interval=0.1
                    )
            
        except Exception as e:
            print(f"[BigBrain] Update check failed: {e}")
            if callback:
                # Execute callback on the main thread with failure
                bpy.app.timers.register(
                    lambda: callback(False, None, None),
                    first_interval=0.1
                )
    
    # Run the check in a background thread to avoid blocking Blender
    thread = threading.Thread(target=_check_thread)
    thread.daemon = True
    thread.start()
    
    return thread

def get_update_status():
    """Returns current update status information"""
    return {
        'update_available': update_available,
        'current_version': VERSION_STRING,
        'latest_version': latest_version,
        'latest_url': latest_url,
        'last_check': last_check_time,
        'blender_version': bpy.app.version_string,
        'is_blender4_plus': bpy.app.version >= (4, 0, 0)
    }

class BIGBRAIN_OT_CheckForUpdates(bpy.types.Operator):
    bl_idname = "bigbrain.check_for_updates"
    bl_label = "Check for Updates"
    bl_description = "Check if a newer version of BigBrain is available"
    
    def execute(self, context):
        def update_callback(has_update, version, url):
            if has_update:
                self.report({'INFO'}, f"BigBrain update available: v{version}")
            else:
                if version is None:
                    self.report({'ERROR'}, "Update check failed. Check your internet connection.")
                else:
                    self.report({'INFO'}, f"BigBrain is up to date (v{VERSION_STRING})")
        
        check_for_updates(update_callback)
        return {'FINISHED'}

class BIGBRAIN_OT_OpenUpdatePage(bpy.types.Operator):
    bl_idname = "bigbrain.open_update_page"
    bl_label = "Get Update"
    bl_description = "Open the download page for the latest version"
    
    def execute(self, context):
        if latest_url:
            bpy.ops.wm.url_open(url=latest_url)
        else:
            self.report({'ERROR'}, "Update URL not available. Check for updates first.")
        return {'FINISHED'}

def register():
    bpy.utils.register_class(BIGBRAIN_OT_CheckForUpdates)
    bpy.utils.register_class(BIGBRAIN_OT_OpenUpdatePage)
    
    # Check for updates when addon is loaded
    check_for_updates()

def unregister():
    bpy.utils.unregister_class(BIGBRAIN_OT_OpenUpdatePage)
    bpy.utils.unregister_class(BIGBRAIN_OT_CheckForUpdates)