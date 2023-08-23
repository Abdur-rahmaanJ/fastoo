from fastoo import render_template
from fastapi import APIRouter
from fastapi import Request
from fastapi import Depends

from typing import Annotated

from pydantic_settings import BaseSettings

from init import get_settings

router = APIRouter(include_in_schema=False)


@router.get("/login/")
def login(request: Request):
    return render_template("themes/front/dingy/index.html", {}, request)


@router.get("/info")
async def info(settings: Annotated[BaseSettings, Depends(get_settings)]):
    return {
        "app_name": settings.app_name,
        "admin_email": settings.admin_email,
        "items_per_user": settings.items_per_user,
    }
