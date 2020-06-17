extends Reference

class_name SharedLibrary

# TODO: Remove all this and use `GDNativeLibrary`'s method named
#       `get_current_dependencies()` which I only recently noticed? :)
#       (Particularly now that we are setting the libraries as dependencies.)

const testlib = {
    "_Base_": "addons/testlib/",
    "X11": "testlib.so",
    "Server": "testlib.so",
    "OSX": "testlib.dylib", # Note: Could be `.so` but clashes with X11 then.
    "Windows": "testlib.dll", # TODO: Handle/error 32 vs 64?
   }
