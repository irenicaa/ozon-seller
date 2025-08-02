from __future__ import annotations
from typing import Optional, cast
from http.server import ThreadingHTTPServer
import types
import threading
import socket

from .test_server_endpoint import TestServerEndpoint
from .test_server_handler import TestServerHandler


class TestServer:
    def __init__(self, endpoints: list[TestServerEndpoint]) -> None:
        self._endpoints = endpoints

    def __enter__(self) -> TestServer:
        self.start()
        return self

    def __exit__(
        self,
        exc_type: Optional[type[BaseException]],
        exc_value: Optional[BaseException],
        traceback: Optional[types.TracebackType],
    ) -> None:
        self.stop()

    @property
    def address(self) -> str:
        return f"http://{self._server.server_name}:{self._server.server_port}"

    def start(self) -> None:
        self._server = ThreadingHTTPServer(
            server_address=("localhost", _find_available_port()),
            RequestHandlerClass=TestServerHandler.create(self._endpoints),
        )

        self._thread = threading.Thread(target=self._server.serve_forever, daemon=True)
        self._thread.start()

    def stop(self) -> None:
        self._server.shutdown()
        self._server.server_close()

        self._thread.join()


def _find_available_port() -> int:
    with socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM) as temp_socket:
        temp_socket.bind(("localhost", 0))
        return cast(int, temp_socket.getsockname()[1])
