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

 def unregister_all_keys(self):
  for key in self.active_keys:
   self.unregister_key(key, self.active_keys[key])

 def handle_key (self, key):
  try:
   function = self.active_keys[key]
  except KeyError:
   return
  return function()

 def register_keys(self, keys):
  #Given a dict with keys of keystrokes and values of functions, registers all keystrokes
  for k in keys:
   self.register_key(k, keys[k])

 def unregister_hotkeys(self):
  for key in self.active_keys:
   self.unregister_hotkey(k, self.active_keys[k])

