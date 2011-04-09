import pkgutil

__all__ = []
__modules__ = []
for loader, module_name, is_pkg in  pkgutil.walk_packages(__path__):
    __all__.append(module_name)
    module = loader.find_module(module_name).load_module(module_name)
    __modules__.append(module)
    exec('%s = module' % module_name)