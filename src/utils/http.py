from __future__ import annotations

import json
from typing import Dict
from aiohttp import ClientSession, TCPConnector


class HttpClient:
    session: ClientSession = None
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

    @staticmethod
    async def start(
        *args,
        headers=None,
        json_serialize=lambda obj, **kwargs: json.dumps(obj, default=str, **kwargs),
        raise_for_status=True,
        connector_parameters: Dict = None,
        **kwargs
    ):
        if headers is None:
            headers = HttpClient.headers

        if connector_parameters is None:
            connector_parameters = {}

        connector = TCPConnector(**connector_parameters)
        HttpClient.session = ClientSession(headers=headers,
                                           json_serialize=json_serialize,
                                           raise_for_status=raise_for_status,
                                           connector=connector,
                                           **kwargs)

    @staticmethod
    async def stop():
        await HttpClient.session.close()
        HttpClient.session = None

    @staticmethod
    async def restart(*args, **kwargs):
        await HttpClient.stop()
        await HttpClient.start(*args, **kwargs)

    def __call__(self) -> ClientSession:
        assert HttpClient.session is not None, "Session not found. Please start or restart session."
        return HttpClient.session


http_client = HttpClient()
