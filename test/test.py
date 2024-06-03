from typing import get_type_hints

from pydantic_settings import BaseSettings

class MySettings(BaseSettings):
    foo: str = "bar"

print(get_type_hints(MySettings))
print(get_type_hints(MySettings, include_extras=True))