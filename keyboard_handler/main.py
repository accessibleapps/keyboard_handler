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

 @staticmethod
 def standardize_key(key):
  """Takes a keystroke and places it in a standard case and order in a list."""
  working = key.split('+')
  working = [i.lower() for i in working]
  answer = []
  if "control" in working:
   answer.append("control")
  if "win" in working:
   answer.append("win")
  if "alt" in working:
   answer.append("alt")
  if "shift" in working:
   answer.append("shift")
  if working[-1] not in answer:
   answer.append(working[-1])
  return answer

