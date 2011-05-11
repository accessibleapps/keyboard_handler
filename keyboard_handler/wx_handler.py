import wx

from main import KeyboardHandler

__all__ = ['WXKeyboardHandler', 'WXControlKeyboardHandler']

class BaseWXKeyboardHandler(KeyboardHandler):

 def __init__(self, *args, **kwargs):
  super(BaseWXKeyboardHandler, self).__init__(*args, **kwargs)
  #Setup the replacement dictionaries.

  for i in dir(wx):
   if i.startswith('WXK_'):
    key = i[4:].lower()
    self.replacement_keys[key] = getattr(wx, i)
   elif i.startswith('MOD_'):
    key = i[4:].lower()
    self.replacement_mods[key] = getattr(wx, i)

 def parse_key (self, keystroke, separator="+"):
  keystroke = [self.keycode_from_key(i) for i in keystroke.split(separator)]
  mods = 0
  for i in keystroke[:-1]:
   mods = mods | i #or everything together
  return (mods, keystroke[-1])

 def keycode_from_key(self, key):
  if key in self.replacement_mods:
   return self.replacement_mods[key]
  if key in self.replacement_keys:
   return self.replacement_keys[key]
  if len(key) == 1:
   return ord(key.upper())



class WXKeyboardHandler(BaseWXKeyboardHandler):

 def __init__ (self, parent, *args, **kwargs):
  super(WXKeyboardHandler, self).__init__(*args, **kwargs)
  self.parent = parent
  self.key_ids = {}

 def register_key(self, key, function):
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
  for i in self.key_ids:
   if self.key_ids[i] == id:
    self.handle_key(i)

class WXControlKeyboardHandler(wx.StaticText, BaseWXKeyboardHandler):

 def __init__(self, parent=None, *a, **k):
  wx.StaticText.__init__(self, parent=parent)
  KeyboardHandler.__init__(self, *a, **k)
  self.wx_replacements = {}
  for i in [d for d in dir(wx) if d.startswith('WXK_')]:
   self.wx_replacements[getattr(wx, i)] = i[4:].lower()
  self.Bind(wx.EVT_KEY_DOWN, self.process_key, self)
  self.SetFocus()

 def process_key(self, evt):
  keycode = evt.GetKeyCode()
  keyname = self.wx_replacements.get(keycode, None)
  modifiers = ""
  replacements = (   (evt.ControlDown(), 'control+'),
   (evt.AltDown(),     'alt+'),
   (evt.ShiftDown(),   'shift+'),
   (evt.MetaDown(),    'win+')
  )
  for mod, ch in (replacements):
   if mod:
    modifiers += ch
  if keyname is None:
   if 27 < keycode < 256:
    keyname = chr(keycode).lower()
   else:
    keyname = "(%s)unknown" % keycode
  key = modifiers + keyname
  self.handle_key(key)

