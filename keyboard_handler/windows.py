import win32api
import win32con

from main import KeyboardHandler

class WindowsKeyboardHandler(KeyboardHandler):

 def __init__ (self):
  super(WindowsKeyboardHandler, self).__init__()
  #Setup the replacement dictionaries.
  for i in dir(win32con):
   if i.startswith("VK_"):
    key=i[3:].lower()
    self.replacement_keys[key] = getattr(win32con, i)
   elif i.startswith("MOD_"):
    key=i[4:].lower()
    self.replacement_mods[key] = getattr(win32con, i)
  self.replacement_keys .update(dict(pageup=win32con.VK_PRIOR, pagedown=win32con.VK_NEXT))


