from pydantic_settings import BaseSettings
from injector import Injector, Module, SingletonScope, Binder


class MySettings(BaseSettings):
    foo: str = "bar"


class Configuration(Module):

    def configure(self, binder: Binder):
        binder.bind(MySettings, scope=SingletonScope, to=lambda: MySettings())

def test_works_with_lambda_factory():
    print("Everything is sad with Injector")
    injector = Injector([Configuration])

    config = injector.get(MySettings)
    print(config)
    assert(True)

assert(True)