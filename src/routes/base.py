from fastapi import FastAPI , APIRouter, Depends
from helpers.config import get_settings, Settings

Base_router =APIRouter(
    prefix="/api/v1", 
    tags=["api_v1"],
)

@Base_router.get("/")
async def welcome(app_settings:Settings= Depends(get_settings)):
    #app_setings = get_settings()
    #in routes we can use Depends to get the settings more efficiently and avoid creating a new instance of settings every time we need to access it
    app_name = app_settings.APP_NAME
    app_version = app_settings.APP_VERSION
    return {
        "app_name": app_name,
        "app_version": app_version
    }

