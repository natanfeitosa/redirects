import typing as t

from lespy.core.router import Route


class WildcardRoute(Route):
    def match(self, path: str) -> t.Optional[t.Dict[str, t.Any]]:
        return {}
