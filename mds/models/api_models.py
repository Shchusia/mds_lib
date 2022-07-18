"""
Models returned from api
"""

from typing import Optional, TypeVar

from pydantic import BaseModel, Field

SubPydanticBaseModel = TypeVar("SubPydanticBaseModel", bound=BaseModel)


class ModelFile(BaseModel):
    file_name: str = Field(..., alias="fileName", description="Base name")
    version: str = Field(
        ..., description="Version of file with `fileName` in system MDS"
    )
    created: str = Field(..., description="DateTime uploaded current file to storage")
    file_type: Optional[str] = Field(
        None, alias="fileType", description="Optional attribute for grouped files"
    )


class ErrorModel(BaseModel):
    code: int = Field(default=400, description="http status code")
    title: str = Field(description="Error group")
    detail: str = Field(description="Details error")

    class Config:
        schema_extra = {
            "example": {
                "code": 400,
                "title": "IncorrectInputData",
                "detail": "Type of `sku_id` must be a integer and not a string",
            }
        }


class BadResponse(BaseModel):
    status: str = "error"
    error: ErrorModel


class RespModel(BaseModel):
    status: str
    data: SubPydanticBaseModel  # type: ignore
