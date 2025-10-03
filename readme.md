# Keyboard Handler

Cross-platform global hotkey handler for Python with human-readable key parsing.

## Platform Support

- **Windows**: WX-based via `wx.RegisterHotKey()` or direct via pywin32
- **Linux**: AT-SPI via pyatspi
- **macOS**: Carbon/AppKit (partial support)

## Installation

```bash
pip install keyboard_handler
# Windows only:
pip install keyboard_handler[':sys_platform == "win32"']
```

## Usage

### WXKeyboardHandler

```python
from keyboard_handler.wx_handler import WXKeyboardHandler

handler = WXKeyboardHandler(parent)

# Register a hotkey
handler.register_key("control+t", self.display_time)
handler.register_key("control+win+w", self.do_something_else)

# Register multiple hotkeys
mapping = {
    "control+w": self.close_window,
    "alt+f4": self.close_all
}
handler.register_keys(mapping)

# Unregister
handler.unregister_key("control+t", self.display_time)
handler.unregister_keys(mapping)
handler.unregister_all_keys()
```

### Error Handling

```python
from keyboard_handler import KeyboardHandlerError

try:
    handler.register_key("control+t", callback)
except KeyboardHandlerError:
    # Key already registered or parse error
    pass
```

### Key Format

Keys use `+` to separate modifiers from the main key:

- Modifiers: `control`, `shift`, `alt`, `win` (or `windows`)
- Examples: `"control+t"`, `"shift+alt+f1"`, `"control+win+delete"`

