from .sessions import Session

from typing import Any, Optional, Union
from inspect import signature

def request(
    method: str,
    url: str,
    **kwargs
):
    """Send a request"""
    session = Session(**{key: kwargs[key] for key in kwargs.keys() if (key in signature(Session).parameters.keys())})
    return session.request(method=method, url=url, **{key: kwargs[key] for key in kwargs.keys() if (key in signature(session.request).parameters.keys())})

def get(
    url: str,
    **kwargs: Any
):
    """Sends a GET request"""
    return request(method="GET", url=url, **kwargs)

def options(
    url: str,
    **kwargs: Any
):
    """Sends a OPTIONS request"""
    return request(method="OPTIONS", url=url, **kwargs)

def head(
    url: str,
    **kwargs: Any
):
    """Sends a HEAD request"""
    return request(method="HEAD", url=url, **kwargs)

def post(
    url: str,
    data: Optional[Union[str, dict]] = None,
    json: Optional[dict] = None,
    **kwargs: Any
):
    """Sends a POST request"""
    return request(method="POST", url=url, data=data, json=json, **kwargs)

def put(
    url: str,
    data: Optional[Union[str, dict]] = None,
    json: Optional[dict] = None,
    **kwargs: Any
):
    """Sends a PUT request"""
    return request(method="PUT", url=url, data=data, json=json, **kwargs)

def patch(
    url: str,
    data: Optional[Union[str, dict]] = None,
    json: Optional[dict] = None,
    **kwargs: Any
):
    """Sends a PATCH request"""
    return request(method="PATCH", url=url, data=data, json=json, **kwargs)

def delete(
    url: str,
    **kwargs: Any
):
    """Sends a DELETE request"""
    return request(method="DELETE", url=url, **kwargs)
