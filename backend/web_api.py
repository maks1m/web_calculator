from typing import Any

from fastapi import FastAPI
from pydantic import BaseModel
from starlette.responses import FileResponse
from starlette.staticfiles import StaticFiles

from services.calculation_service import CalculationService, CalculationError

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

calc_service = CalculationService()


# or inject desired calculator while creating the service
# calc_service = CalculationService(CalculatorExtended())


class ResponseItem(BaseModel):
    response: Any | None = None
    error: dict | None = None


@app.get("/math-operations",
         response_description="Get list of supported math operations",
         response_model_exclude_none=True
         )
def get_supported_math_operations() -> ResponseItem:
    return {
        "response": calc_service.supported_operations()
    }


class CalculateRequest(BaseModel):
    args: list[int]
    operations: list[str]


@app.post("/calculate",
          response_description="Calculate provided mathematical expression",
          response_model_exclude_none=True)
def calculate(req: CalculateRequest) -> ResponseItem:
    result = error = None
    try:
        result = calc_service.calculate(req.args, req.operations)
    except CalculationError as e:
        error = str(e)
    except Exception:
        error = "Unexpected error found"

    return {
        "response": result,
        "error": error
    }


@app.exception_handler(404)
def custom_404_handler(_, __):
    return FileResponse('./static/404.html')
