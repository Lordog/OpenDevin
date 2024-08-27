from dataclasses import dataclass


@dataclass
class Event:
    @property
    def message(self) -> str | None:
        if hasattr(self, '_message'):
            return self._message  # type: ignore [attr-defined]
        return ''

    @property
    def id(self) -> int | None:
        if hasattr(self, '_id'):
            return self._id  # type: ignore [attr-defined]
        return -1

    @property
    def timestamp(self) -> str | None:
        if hasattr(self, '_timestamp'):
            return self._timestamp  # type: ignore [attr-defined]
        return None

    @property
    def source(self) -> str | None:
        if hasattr(self, '_source'):
            return self._source  # type: ignore [attr-defined]
        return None

    @property
    def cause(self) -> int | None:
        if hasattr(self, '_cause'):
            return self._cause  # type: ignore [attr-defined]
        return None


@dataclass
class Observation(Event):
    content: str


@dataclass
class AgentStateChangedObservation(Observation):
    """
    This data class represents the result from delegating to another agent
    """

    agent_state: str
    observation: str = ''

    @property
    def message(self) -> str:
        return ''


E = Event()
print(E.message)
