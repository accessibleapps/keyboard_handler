import wx

from windows import WindowsKeyboardHandler

__all__ = ['WXKeyboardHandler', 'WXPanelKeyboardHandler']

class WXKeyboardHandler(WindowsKeyboardHandler):

 def __init__ (self, frame, *args, **kwargs):
  super(WXKeyboardHandler, self).__init__(*args, **kwargs)
  self.frame = frame
  self.key_ids = {}

 def register_key (self, key, function):
  super(WXKeyboardHandler, self).register_key(key, function)
  key_id = wx.NewId()
  parsed = self.parse_key(key)
  self.frame.RegisterHotKey(key_id, *parsed)
  self.frame.Bind(wx.EVT_HOTKEY, lambda evt: self.process_key(evt, key_id), id=key_id)
  self.key_ids[key] = key_id

 def unregister_key (self, key, function):
  super(WXKeyboardHandler, self).unregister_key(key, function)
  key_id = self.key_ids[key]
  answer = self.frame.UnregisterHotKey(key_id)
  self.frame.Unbind(wx.EVT_HOTKEY, id=key_id)
  del(self.key_ids[key])

 def process_key (self, evt, id):
  evt.Skip()
  key = None
  for i in self.key_ids:
   if self.key_ids[i] == id:
    self.handle_key(i)

 def parse_key (self, key):
  key=key.split("+")
 #replacements
 #Modifier keys:
  for index, item in enumerate(key[0:-1]):
   if self.replacement_mods.has_key(item):
    key[index] = self.replacement_mods[item]
  if self.replacement_keys.has_key(key[-1]):
   key[-1] = self.replacement_keys[key[-1]]
  elif len(key[-1])==1:
   key[-1] = win32api.VkKeyScan(str(key[-1]))
  mods = 0
  for i in key[:-1]:
   mods = mods|i
  print [mods, key[-1]]
  return [mods, key[-1]]


class WXPanelKeyboardHandler(WindowsKeyboardHandler):

 def create_capturer (self, target):
  #Creates a keyboard capturer control on the given target and binds this handler to it.
  self.capturer = self.wx.StaticText(parent=target, style=self.wx.WANTS_CHARS)
  self.capturer.Bind(self.wx.EVT_CHAR, self.handle_key_evt)
  self.capturer.SetFocus()

 def handle_key_evt (self, evt):
  key = evt.GetUnicodeKey()
  modifiers = evt.GetModifiers()
  replacements = {37:'left', 38:'up', 39:'right', 40:'down'}
  if key in replacements:
   key = replacements[key]
  else:
   key = chr(key)
  self.handle_key(key)

