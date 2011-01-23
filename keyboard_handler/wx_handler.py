import wx

from windows import WindowsKeyboardHandler

__all__ = ['WXKeyboardHandler']

class WXKeyboardHandler(WindowsKeyboardHandler):

 def __init__ (self, parent, is_global=False):
  super(WXKeyboardHandler, self).__init__()
  self.parent = parent
  self.is_global = is_global
  self.key_ids = {}

 def register_key (self, key, function):
  super(WXKeyboardHandler, self).register_key(key, function)
  key_id = wx.NewId()
  parsed = self.parse_key(key)
  self.parent.RegisterHotKey(key_id, *parsed)
  self.parent.Bind(wx.EVT_HOTKEY, lambda evt: self.process_key(evt, key_id), id=key_id)
  self.key_ids[key] = key_id

 def unregister_key (self, key, function):
  super(WXKeyboardHandler, self).unregister_key(key, function)
  key_id = self.key_ids[key]
  answer = self.parent.UnregisterHotKey(key_id)
  self.parent.Unbind(wx.EVT_HOTKEY, id=key_id)
  del(self.key_ids[key])

 def process_key (self, evt, id):
  evt.Skip()
  if not self.is_global and not self.parent.HasFocus():
   return
  key = None
  for i in self.key_ids:
   if self.key_ids[i] == id:
    self.handle_key(i)

