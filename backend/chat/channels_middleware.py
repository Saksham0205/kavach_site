from channels.middleware import BaseMiddleware
from rest_framework.exceptions import AuthenticationFailed
from django.db import close_old_connections
from accounts.tokenauthentication import JWTAuthentication

class JWTWebsocketMiddleware(BaseMiddleware):
    async def __call__(self, scope, receive, send):
        close_old_connections()
        quary_string = scope.get("quary_String", b" ").decode("utf-8")
        quary_parameters =  dict(qp.split("=") for qp in quary_string.split("&"))
        token = quary_parameters.get('token', None)
        if token is None:

            await send({
                "type": "websocket.close",
                "code": 4000
            })
        authentication= JWTAuthentication()
        try:
            user = await authentication.authenticate_websocket(scope, token)
            if user is not None:
                scope ['user']  = user
            else:
                await send
                (
                    {"type": "websocket.close",
                "code": 4000
            }) 
            return await super().__call__(scope, receive, send) 
        except AuthenticationFailed:    
            await send({
                "type": "websocket.close",
                "code": 4002
            })