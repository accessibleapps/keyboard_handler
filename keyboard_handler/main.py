import platform

class KeyboardHandlerError (Exception): pass

class KeyboardHandler(object):

 def __init__(self):
  super(KeyboardHandler, self).__init__()
  self.active_keys = {}
  if not hasattr(self, 'replacement_mods'):
   self.replacement_mods = {}
  if not hasattr(self, 'replacement_keys'):
   self.replacement_keys = {}

 def register_key (self, key, function):
  if key in self.active_keys:
   raise KeyboardHandlerError, "Key %s is already registered to a function" % key
  if not callable(function):
   raise TypeError, "Must provide a callable to be invoked upon keypress"
  self.active_keys[key] = function

 def unregister_key (self, key, function):
  try:
   if self.active_keys[key] != function:
    raise KeyboardHandlerError, "key %s is not registered to that function" % key
  except KeyError:
   raise KeyboardHandlerError, "Key %s not currently registered"

 def handle_key (self, key):
  try:
   function = self.active_keys[key]
  except KeyError:
   return
  return function()


class WindowsKeyboardHandler(KeyboardHandler):

 def __init__ (self):
  if platform.system() == 'Windows':
   self.win32api = __import__('win32api')
   self.win32con = __import__('win32con')
  super(WindowsKeyboardHandler, self).__init__()
  self.replacement_keys = dict(pageup=self.win32con.VK_PRIOR, pagedown=self.win32con.VK_NEXT)

