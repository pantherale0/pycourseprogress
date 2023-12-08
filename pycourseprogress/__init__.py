"""Course Progress entry point."""

from .api import CourseProgressSession

class CourseProgress:
    """The main Course Progress API."""

    def __init__(self, instance: str):
        """Super init, should only be used for advanced purposes.
        Use the class create method for standard usage."""
        self._api: CourseProgressSession = CourseProgressSession(instance)

    async def update(self):
        """Request update of cached data."""
        # TODO

    @classmethod
    async def create(cls, instance: str, username: str, password: str):
        """Creates an instance of Course Progress."""
        self = cls(instance)
        await self._api.login(username=username,
                              password=password)
        await self.update()
        return self
