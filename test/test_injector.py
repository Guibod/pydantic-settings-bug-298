from pydantic_settings import BaseSettings
from injector import Injector, Module, SingletonScope, Binder


class MySettings(BaseSettings):
    foo: str = "bar"


class Configuration(Module):

    def configure(self, binder: Binder):
        binder.bind(MySettings, scope=SingletonScope)

def test_wont_work_through_injector():
    print("Everything is sad with Injector")
    injector = Injector([Configuration])

    config = injector.get(MySettings)

    assert(True)

assert(True)