# Module `api_models.py`
```text
Models returned from api
```

> Path: `mds_lib\models\api_models.py`
`SubPydanticBaseModel` = TypeVar('SubPydanticBaseModel', bound=BaseModel)
## Class `ModelFile`
### Basses(s)
+ BaseModel
### SubElement(s)
 > `file_name`: str = Field(..., alias='fileName', description='Base name')
 > `version`: str = Field(..., description='Version of file with `fileName` in system MDS')
 > `created`: str = Field(..., description='DateTime uploaded current file to storage')
 > `file_type`: Optional[str] = Field(None, alias='fileType', description='Optional attribute for grouped files')
## Class `ErrorModel`
### Basses(s)
+ BaseModel
### SubElement(s)
 > `code`: int = Field(default=400, description='http status code')
 > `title`: str = Field(description='Error group')
 > `detail`: str = Field(description='Details error')
 > ## Class `Config`
 > ### SubElement(s)
 > > `schema_extra` = {
 > > "example": {
 > > "code": 400,
 > > "title": "IncorrectInputData",
 > > "detail": "Type of `sku_id` must be a integer and not a string"
 > > }
 > > }
## Class `BadResponse`
### Basses(s)
+ BaseModel
### SubElement(s)
 > `status`: str = "error"
 > `error`: ErrorModel = None
## Class `RespModel`
### Basses(s)
+ BaseModel
### SubElement(s)
 > `status`: str = None
 > `data`: SubPydanticBaseModel = None