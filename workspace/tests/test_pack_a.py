from pack_a import __version__

from types import ModuleType, FunctionType


def test_version():
    assert __version__ == '0.1.0'


class TestImport:
    def test_import1(self):
        from pack_a import sub_1
        isinstance(sub_1, ModuleType)
        # sub_1 は <module 'pack_a.sub_1' from  ~~中略~~ /pack_a/sub_1/__init__.py'>

    def test_import2(self):
        from pack_a.sub_1 import module_one
        isinstance(module_one, ModuleType)

    def test_importe3(self):
        from pack_a.sub_1.module_one import say_name
        isinstance(say_name, FunctionType)

    def test_import4(self):
        """package sub_1 に module1 の中身をおいておいた """
        from pack_b import sub_1
        isinstance(sub_1.say_name, FunctionType)
