# =============================================================================
# utils/diagnostics.py — System diagnostics and driver checks
# =============================================================================

import bpy
import sys
import platform
import os
import subprocess
import re
from ..i18n import get_text as _

def get_system_info():
    """
    Get detailed system information
    
    Returns:
        Dictionary with system information
    """
    info = {
        "os": {
            "name": platform.system(),
            "version": platform.version(),
            "release": platform.release(),
            "platform": platform.platform()
        },
        "python": {
            "version": sys.version,
            "implementation": platform.python_implementation(),
            "compiler": platform.python_compiler()
        },
        "blender": {
            "version": bpy.app.version_string,
            "version_tuple": bpy.app.version,
            "build_date": bpy.app.build_date,
            "build_hash": bpy.app.build_hash,
            "binary_path": bpy.app.binary_path
        },
        "hardware": {
            "machine": platform.machine(),
            "processor": platform.processor()
        },
        "gpu": get_gpu_info()
    }
    
    # Add memory information
    try:
        import psutil
        mem = psutil.virtual_memory()
        info["memory"] = {
            "total": mem.total / (1024 * 1024),  # Total RAM in MB
            "available": mem.available / (1024 * 1024),  # Available RAM in MB
            "used": mem.used / (1024 * 1024),  # Used RAM in MB
            "percent": mem.percent  # Percentage used
        }
    except ImportError:
        info["memory"] = {
            "note": "psutil not available for detailed memory info"
        }
    
    return info

def get_gpu_info():
    """
    Get GPU information
    
    Returns:
        Dictionary with GPU information
    """
    gpu_info = {
        "device": bpy.context.preferences.system.compute_device_type,
        "vendor": "",
        "renderer": "",
        "version": "",
        "driver_version": ""
    }
    
    # Try to get OpenGL info from Blender
    try:
        import gpu
        vendor = gpu.platform.vendor_get()
        renderer = gpu.platform.renderer_get()
        version = gpu.platform.version_get()
        
        gpu_info["vendor"] = vendor
        gpu_info["renderer"] = renderer
        gpu_info["version"] = version
    except:
        pass
    
    # Try to get more detailed GPU info based on platform
    if platform.system() == "Windows":
        try:
            # Use Windows Management Instrumentation (WMI)
            import wmi
            computer = wmi.WMI()
            gpu_wmi = computer.Win32_VideoController()[0]
            
            gpu_info["name"] = gpu_wmi.Name
            gpu_info["driver_version"] = gpu_wmi.DriverVersion
            gpu_info["driver_date"] = gpu_wmi.DriverDate
            gpu_info["vram"] = int(gpu_wmi.AdapterRAM) / (1024 * 1024) if hasattr(gpu_wmi, "AdapterRAM") else 0
        except:
            # Fallback to dxdiag
            try:
                dxdiag_output = subprocess.check_output("dxdiag /t", shell=True).decode("utf-8", errors="ignore")
                
                # Extract GPU info from dxdiag output
                name_match = re.search(r"Card name: (.*)", dxdiag_output)
                if name_match:
                    gpu_info["name"] = name_match.group(1).strip()
                
                driver_match = re.search(r"Driver Version: (.*)", dxdiag_output)
                if driver_match:
                    gpu_info["driver_version"] = driver_match.group(1).strip()
            except:
                pass
    
    elif platform.system() == "Linux":
        try:
            # Try lspci for NVIDIA or AMD
            lspci_output = subprocess.check_output("lspci | grep -E 'VGA|3D'", shell=True).decode("utf-8", errors="ignore")
            
            # Extract GPU name
            if "NVIDIA" in lspci_output:
                gpu_info["vendor"] = "NVIDIA"
                name_match = re.search(r"NVIDIA Corporation (.*) \[", lspci_output)
                if name_match:
                    gpu_info["name"] = name_match.group(1).strip()
                
                # Try nvidia-smi for driver version
                try:
                    nvidia_smi = subprocess.check_output("nvidia-smi --query-gpu=driver_version --format=csv,noheader", shell=True).decode("utf-8", errors="ignore")
                    gpu_info["driver_version"] = nvidia_smi.strip()
                except:
                    pass
            
            elif "AMD" in lspci_output or "ATI" in lspci_output:
                gpu_info["vendor"] = "AMD"
                name_match = re.search(r"AMD/ATI\] (.*) \[", lspci_output)
                if name_match:
                    gpu_info["name"] = name_match.group(1).strip()
        except:
            pass
    
    elif platform.system() == "Darwin":  # macOS
        try:
            # Use system_profiler for Mac
            sp_output = subprocess.check_output("system_profiler SPDisplaysDataType", shell=True).decode("utf-8", errors="ignore")
            
            # Extract GPU info
            chipset_match = re.search(r"Chipset Model: (.*)", sp_output)
            if chipset_match:
                gpu_info["name"] = chipset_match.group(1).strip()
            
            vendor_match = re.search(r"Vendor: (.*)", sp_output)
            if vendor_match:
                gpu_info["vendor"] = vendor_match.group(1).strip()
            
            vram_match = re.search(r"VRAM \(.*\): (.*)", sp_output)
            if vram_match:
                gpu_info["vram"] = vram_match.group(1).strip()
        except:
            pass
    
    return gpu_info

def check_gpu_driver():
    """
    Check if GPU driver is up to date
    
    Returns:
        Dictionary with driver status information
    """
    gpu_info = get_gpu_info()
    result = {
        "is_outdated": False,
        "current_version": gpu_info.get("driver_version", "Unknown"),
        "recommended_version": "Unknown",
        "vendor": gpu_info.get("vendor", "Unknown"),
        "message": ""
    }
    
    # NVIDIA driver check
    if "NVIDIA" in gpu_info.get("vendor", "") or "NVIDIA" in gpu_info.get("name", ""):
        result["vendor"] = "NVIDIA"
        
        # Minimum recommended versions for Blender
        if bpy.app.version >= (3, 0, 0):
            result["recommended_version"] = "460.xx or newer"
            
            # Check if driver is older than 460
            current = gpu_info.get("driver_version", "")
            if current and re.match(r"^\d+", current):
                major_version = int(re.match(r"^\d+", current).group(0))
                if major_version < 460:
                    result["is_outdated"] = True
                    result["message"] = f"Your NVIDIA driver ({current}) is outdated for Blender {bpy.app.version_string}. Please update to 460.xx or newer."
        
        elif bpy.app.version >= (2, 90, 0):
            result["recommended_version"] = "450.xx or newer"
            
            # Check if driver is older than 450
            current = gpu_info.get("driver_version", "")
            if current and re.match(r"^\d+", current):
                major_version = int(re.match(r"^\d+", current).group(0))
                if major_version < 450:
                    result["is_outdated"] = True
                    result["message"] = f"Your NVIDIA driver ({current}) is outdated for Blender {bpy.app.version_string}. Please update to 450.xx or newer."
    
    # AMD driver check
    elif "AMD" in gpu_info.get("vendor", "") or "AMD" in gpu_info.get("name", ""):
        result["vendor"] = "AMD"
        
        # Minimum recommended versions for Blender
        if bpy.app.version >= (3, 0, 0):
            result["recommended_version"] = "21.Q4 or newer"
            # AMD driver version check is more complex and varies by OS
            # This is a simplified check
        
        elif bpy.app.version >= (2, 90, 0):
            result["recommended_version"] = "20.Q3 or newer"
    
    # Intel driver check
    elif "Intel" in gpu_info.get("vendor", "") or "Intel" in gpu_info.get("name", ""):
        result["vendor"] = "Intel"
        
        # Minimum recommended versions for Blender
        if bpy.app.version >= (3, 0, 0):
            result["recommended_version"] = "27.20.100.xxxx or newer"
        
        elif bpy.app.version >= (2, 90, 0):
            result["recommended_version"] = "26.20.100.xxxx or newer"
    
    return result

def run_diagnostics():
    """
    Run comprehensive system diagnostics
    
    Returns:
        Dictionary with diagnostic results
    """
    from .. import utils
    
    utils.log("Starting system diagnostics...", 'INFO')
    
    # Get system info
    system_info = get_system_info()
    
    # Check GPU driver
    driver_status = check_gpu_driver()
    
    # Check Blender version compatibility
    blender_version = bpy.app.version
    blender_compat = {
        "is_compatible": True,
        "message": f"Blender {bpy.app.version_string} is fully compatible with BigBrain"
    }
    
    if blender_version < (2, 93, 0):
        blender_compat["is_compatible"] = False
        blender_compat["message"] = f"Blender {bpy.app.version_string} may not be fully compatible with BigBrain. Version 2.93 or newer is recommended."
    
    # Check for conflicting addons
    from .. import utils
    conflicts = utils.detect_conflicts()
    
    # Check memory status
    memory_status = {
        "total": system_info.get("memory", {}).get("total", 0),
        "available": system_info.get("memory", {}).get("available", 0),
        "used": system_info.get("memory", {}).get("used", 0),
        "percent": system_info.get("memory", {}).get("percent", 0),
        "is_low": False,
        "message": ""
    }
    
    # Check if memory is low (less than 2GB available)
    if memory_status["available"] < 2048:
        memory_status["is_low"] = True
        memory_status["message"] = f"Low memory detected: {memory_status['available']:.0f}MB available. Performance may be affected."
    
    # Compile diagnostic results
    results = {
        "timestamp": bpy.utils.time_from_start(),
        "system_info": system_info,
        "driver_status": driver_status,
        "blender_compatibility": blender_compat,
        "conflicts": conflicts,
        "memory_status": memory_status,
        "warnings": []
    }
    
    # Add warnings
    if not blender_compat["is_compatible"]:
        results["warnings"].append(blender_compat["message"])
    
    if driver_status["is_outdated"]:
        results["warnings"].append(driver_status["message"])
    
    if memory_status["is_low"]:
        results["warnings"].append(memory_status["message"])
    
    if conflicts:
        results["warnings"].append(f"Found {len(conflicts)} conflicting addon(s): {', '.join(conflicts)}")
    
    # Log results
    utils.log(f"Diagnostics complete. Found {len(results['warnings'])} warning(s)", 'INFO')
    for warning in results["warnings"]:
        utils.log(f"Warning: {warning}", 'WARNING')
    
    return results

def format_diagnostics_report(results):
    """
    Format diagnostic results as a human-readable report
    
    Args:
        results: Dictionary with diagnostic results from run_diagnostics()
    
    Returns:
        String with formatted report
    """
    report = []
    
    # Header
    report.append("=" * 80)
    report.append(f"BigBrain Diagnostics Report")
    report.append(f"Generated: {bpy.utils.time_from_start():.2f} seconds after Blender startup")
    report.append("=" * 80)
    report.append("")
    
    # System information
    report.append("SYSTEM INFORMATION")
    report.append("-" * 80)
    system_info = results["system_info"]
    
    report.append(f"OS: {system_info['os']['name']} {system_info['os']['version']} {system_info['os']['release']}")
    report.append(f"Python: {system_info['python']['version'].split()[0]}")
    report.append(f"Blender: {system_info['blender']['version']}")
    report.append(f"CPU: {system_info['hardware']['processor']}")
    
    # GPU information
    gpu_info = system_info["gpu"]
    report.append(f"GPU: {gpu_info.get('name', gpu_info.get('renderer', 'Unknown'))}")
    report.append(f"GPU Vendor: {gpu_info.get('vendor', 'Unknown')}")
    report.append(f"GPU Driver: {gpu_info.get('driver_version', 'Unknown')}")
    
    # Memory information
    memory = system_info.get("memory", {})
    if "total" in memory:
        report.append(f"RAM: {memory['total']:.0f}MB total, {memory['available']:.0f}MB available ({memory['percent']}% used)")
    else:
        report.append(f"RAM: Information not available")
    
    report.append("")
    
    # Warnings
    if results["warnings"]:
        report.append("WARNINGS")
        report.append("-" * 80)
        for warning in results["warnings"]:
            report.append(f"• {warning}")
        report.append("")
    
    # Driver status
    driver = results["driver_status"]
    report.append("GPU DRIVER STATUS")
    report.append("-" * 80)
    report.append(f"Vendor: {driver['vendor']}")
    report.append(f"Current Version: {driver['current_version']}")
    report.append(f"Recommended Version: {driver['recommended_version']}")
    if driver["is_outdated"]:
        report.append(f"Status: OUTDATED - {driver['message']}")
    else:
        report.append(f"Status: UP TO DATE")
    
    report.append("")
    
    # Blender compatibility
    compat = results["blender_compatibility"]
    report.append("BLENDER COMPATIBILITY")
    report.append("-" * 80)
    report.append(f"Blender Version: {system_info['blender']['version']}")
    if compat["is_compatible"]:
        report.append(f"Status: COMPATIBLE")
    else:
        report.append(f"Status: LIMITED COMPATIBILITY - {compat['message']}")
    
    report.append("")
    
    # Conflicting addons
    if results["conflicts"]:
        report.append("CONFLICTING ADDONS")
        report.append("-" * 80)
        for addon in results["conflicts"]:
            report.append(f"• {addon}")
        report.append("")
    
    # Footer
    report.append("=" * 80)
    report.append("End of Diagnostics Report")
    report.append("=" * 80)
    
    return "\n".join(report)

def export_diagnostics_report(filepath=None):
    """
    Run diagnostics and export report to file
    
    Args:
        filepath: Path to save the report (None for default location)
    
    Returns:
        Path to the saved report
    """
    from .. import utils
    
    # Run diagnostics
    results = run_diagnostics()
    
    # Format report
    report = format_diagnostics_report(results)
    
    # Determine filepath
    if not filepath:
        # Use default location in addon directory
        addon_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        reports_dir = os.path.join(addon_dir, "reports")
        os.makedirs(reports_dir, exist_ok=True)
        
        # Create filename with timestamp
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filepath = os.path.join(reports_dir, f"bigbrain_diagnostics_{timestamp}.txt")
    
    # Write report to file
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(report)
        
        utils.log(f"Diagnostics report exported to {filepath}", 'INFO')
        return filepath
    except Exception as e:
        utils.log(f"Error exporting diagnostics report: {e}", 'ERROR')
        return None

def register():
    """Register diagnostics functionality"""
    from .. import utils
    utils.log("Diagnostics system initialized", 'INFO')

def unregister():
    """Unregister diagnostics functionality"""
    pass