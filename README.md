# fastapi-primer
A learning project to get FastAPI + SQLAlchemy to work for me

## Stages 1-7
### FastAPI is like Flask
```python
from fastapi import FastAPI, APIRouter
...

app = FastAPI(title="Recipe API", openapi_url="/openapi.json")
api_router = APIRouter()

...

@api_router.get("/recipe/{recipe_id}", status_code=200, response_model=Recipe)
def fetch_recipe(*, recipe_id: int, db: Session = Depends(deps.get_db)) -> Any:
    "Fetch a single recipe by ID"
    result = crud.recipe.get(db, recipe_id)
    if not result:
        raise HTTPException(
            status_code=404,
            detail=f"Recipe with ID {recipe_id} is not found"
        )
    
    return result

...

app.include_router(api_router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")
```

### Working with data: pydantic (schema) + SQLAlchemy (model)
![CRUD diagram](diagrams/crud.gif)
