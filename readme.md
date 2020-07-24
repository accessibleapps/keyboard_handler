## Introduction

Keyboard Handler allows you to register global hotkeys on multiple platforms, in addition to implementing a flexible parsing system.

## WXKeyboardHandler

This can be used in an WX application:

### Initializing the handler

```python
from keyboard_handler.wx_handler import WXKeyboardHandler
handler = WXKeyboardHandler(parent)
```

### Registering a global hotkey

```python
try:
	key = handler.register_key(key, function)
except keyboard_handler.KeyboardHandlerError:
	handle parse error
```

Keys can be parsed in a human-readable format, perfect for config files.

```python
handler.register_key("control+t", self.display_time)
handler.register_key("control+windows+w", self.do_something_else)
```

You can register keys in bulk given a mapping.

```python
mapping = {"control+w": self.close_window, "alt+f4": self.close_all}
handler.register_keys(mapping)
```

### Unregistering a global hotkey

```python
handler.unregister_key("control+t", self.display_time)
handler.unregister_key("control+windows+w", self.do_something_else)
```

or to unregister a mapping:

```python
mapping = {"control+w": self.close_window, "alt+f4": self.close_all}
handler.unregister_keys(mapping)
```

or to unregister everything:

```python
handler.unregister_all_keys()
```

