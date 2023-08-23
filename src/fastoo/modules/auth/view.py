from fastoo import render_template
from fastoo.api.module import Module

from fastapi import APIRouter
from fastapi import Request
from fastapi import Depends

from typing import Annotated

from pydantic_settings import BaseSettings

from init import get_settings

router = APIRouter(include_in_schema=False)
module = Module(__file__)

@router.get("/login/")
def login(request: Request):
    with module.set(request) as m:
        return module.render_template("themes/front/dingy/index.html", {})


@router.get("/info")
async def info(settings: Annotated[BaseSettings, Depends(get_settings)]):
    return {
        "app_name": settings.app_name,
        "admin_email": settings.admin_email,
        "items_per_user": settings.items_per_user,
    }
