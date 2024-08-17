import typing
from urllib.parse import quote

from lespy import Response


class RedirectResponse(Response):
    def __init__(self, redirect_to: str, status_code: typing.Union[int, str] = None):
        if status_code is None:
            status_code = 301
        super().__init__(
            '',
            status_code=int(status_code),
            headers={'Location': quote(redirect_to, safe="/#%[]=:;$&()+,!?*@'~")}
        )
