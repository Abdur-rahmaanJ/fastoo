from fastoo import render_template
from fastapi import APIRouter
from fastapi import Request

router = APIRouter(include_in_schema=False)


@router.get("/login/")
def login(request: Request):
    return render_template("themes/front/dingy/index.html", {}, request)
