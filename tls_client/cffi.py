from sys import platform
from platform import machine, version
import ctypes
import os

if platform == 'darwin':
    file_ext = '-darwin-arm64.dylib' if machine() == 'arm64' else '-darwin-amd64.dylib'
elif platform in ('win32', 'cygwin'):
    file_ext = '-windows-64.dll' if 8 == ctypes.sizeof(ctypes.c_voidp) else '-windows-32.dll'
else:
    if machine() == 'aarch64':
        file_ext = '-linux-arm64.so'
    elif machine() == 'armv7l':
        file_ext = '-linux-armv7.so'
    elif 'ubuntu' in version().lower():
        file_ext = '-linux-ubuntu-amd64.so'
    else:
        file_ext = '-linux-alpine-amd64.so'

root_dir = os.path.abspath(os.path.dirname(__file__))
library = ctypes.cdll.LoadLibrary(f'{root_dir}/dependencies/tls-client{file_ext}')

# extract the exposed request function from the shared package
request = library.request
request.argtypes = [ctypes.c_char_p]
request.restype = ctypes.c_char_p

freeMemory = library.freeMemory
freeMemory.argtypes = [ctypes.c_char_p]
freeMemory.restype = ctypes.c_char_p