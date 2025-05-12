from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from app.utility import token

class CombinedMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        origin = request.headers.get("origin")
        
        # Handle preflight CORS
        if request.method == "OPTIONS":
            return JSONResponse(
                status_code=200,
                content={},
                headers={
                    "Access-Control-Allow-Origin": origin or "*",
                    "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, OPTIONS",
                    "Access-Control-Allow-Headers": "Authorization, Content-Type",
                    "Access-Control-Allow-Credentials": "true",
                }
            )

        # Skip auth for login
        if request.url.path.startswith("/login") or request.url.path.startswith("/docs") or request.url.path.startswith(""):
            response = await call_next(request)
        else:
            tokefound = request.headers.get("Authorization")
            if tokefound and tokefound.startswith("Bearer "):
                payload = token.verify_token(token[7:])
                if payload:
                    request.state.user = payload
                    response = await call_next(request)
                    new_token = token.create_access_token(payload)
                    response.headers["X-New-Token"] = new_token
                else:
                    return JSONResponse(status_code=401, content={"detail": "Token invalidated"})
            else:
                return JSONResponse(status_code=401, content={"detail": "Missing or invalid token"})

        # Always add CORS headers to the response
        response.headers["Access-Control-Allow-Origin"] = origin or "*"
        response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
        response.headers["Access-Control-Allow-Headers"] = "Authorization, Content-Type"
        response.headers["Access-Control-Allow-Credentials"] = "true"
        return response