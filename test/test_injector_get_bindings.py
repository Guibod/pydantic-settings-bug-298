from pydantic_settings import BaseSettings
from injector import Injector, Module, SingletonScope, Binder, get_bindings


class Configuration(Module):

    def configure(self, binder: Binder):
        binder.bind(BaseSettings)

def test_get_bindings_works():
    print("Everything is sad with Injector")

    print(get_bindings(BaseSettings))

    assert(True)
def test_get_bindings_works():
    print("Everything is sad with Injector")

    print(get_bindings(BaseSettings))

    assert(True)

assert(True)