import platform
if platform.system() == 'Windows':
 from wx_handler import WXKeyboardHandler as GlobalKeyboardHandler
elif platform.system() == 'Linux':
 from linux import LinuxKeyboardHandler as GlobalKeyboardHandler
