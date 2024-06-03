from typing import get_type_hints

from pydantic_settings import BaseSettings


class MySettings(BaseSettings):
    foo: str = "bar"

def test_everything_is_smooth_without_injector():
    print("Everything is smooth without Injector")
    print(get_type_hints(MySettings))
    print(get_type_hints(MySettings, include_extras=True))

    assert(True)