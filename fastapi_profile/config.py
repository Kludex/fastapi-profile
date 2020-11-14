from typing import Optional

from pydantic import BaseModel
from sqlalchemy.engine import Engine


class ProfileConfig(BaseModel):
    debug: bool = False
    engine: Engine

    class Config:
        arbitrary_types_allowed = True


profile_config: Optional[ProfileConfig] = None
print(profile_config)
