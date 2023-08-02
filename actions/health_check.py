from typing import List

from pydantic import BaseModel

from . import action_store as s


class HealthRequest(BaseModel):
    pass


class HealthResponse(BaseModel):
    params: bool
    errors: List[str]


@s.kubiya_action()
def health_check(_: HealthRequest) -> HealthResponse:
    errors = List[str]
    params = _validate_params(errors)
    return HealthResponse(params=params, errors=errors)


def _validate_params(e: List[str]) -> bool:
    valid = True
    if s.secrets.get("JENKINS_URL") == "":
        valid = False
        e.append("JENKINS_URL is not set")

    if s.secrets.get("JENKINS_USER") == "":
        valid = False
        e.append("JENKINS_USER is not set")

    if s.secrets.get("JENKINS_PASSWORD") == "":
        valid = False
        e.append("JENKINS_PASSWORD is not set")

    return valid
