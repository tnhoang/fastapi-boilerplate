from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps
from app.crud.base import CRUDBase
from app.db.base_class import Base

router = APIRouter()

current_schema: BaseModel = schemas.Item
current_model: Base = models.Item
current_crud: CRUDBase = crud.item


@router.get("/", response_model=List[current_schema])
def read_items(
    db: Session = Depends(deps.get_db), skip: int = 0, limit: int = 100
) -> Any:
    """
    Retrieve items.
    """
    # if crud.user.is_superuser(current_user):
    #     items = crud.item.get_multi(db, skip=skip, limit=limit)
    # else:
    #     items = current_crud.get_multi_by_owner(
    #         db=db, owner_id=current_user.id, skip=skip, limit=limit
    #     )
    items = current_crud.get_multi(db, skip=skip, limit=limit)
    return items


# @router.post("/", response_model=schemas.Item)
# def create_item(
#     *,
#     db: Session = Depends(deps.get_db),
#     item_in: schemas.ItemCreate,
# ) -> Any:
#     """
#     Create new item.
#     """
#     item = crud.item.create_with_owner(
#         db=db, obj_in=item_in, owner_id=current_user.id
#     )
#     return item


# @router.put("/{id}", response_model=current_schema)
# def update_item(
#     *,
#     db: Session = Depends(deps.get_db),
#     id: int,
#     item_in: schemas.ItemUpdate,
# ) -> Any:
#     """
#     Update an item.
#     """
#     item = current_crud.get(db=db, id=id)
#     if not item:
#         raise HTTPException(status_code=404, detail="Item not found")
#     if not crud.user.is_superuser(current_user) and (
#         item.owner_id != current_user.id
#     ):
#         raise HTTPException(status_code=400, detail="Not enough permissions")
#     item = current_crud.update(db=db, db_obj=item, obj_in=item_in)
#     return item


# @router.get("/{id}", response_model=current_schema)
# def read_item(
#     *,
#     db: Session = Depends(deps.get_db),
#     id: int,
# ) -> Any:
#     """
#     Get item by ID.
#     """
#     item = current_crud.get(db=db, id=id)
#     if not item:
#         raise HTTPException(status_code=404, detail="Item not found")
#     if not crud.user.is_superuser(current_user) and (
#         item.owner_id != current_user.id
#     ):
#         raise HTTPException(status_code=400, detail="Not enough permissions")
#     return item


# @router.delete("/{id}", response_model=current_schema)
# def delete_item(
#     *,
#     db: Session = Depends(deps.get_db),
#     id: int,
#     current_user: models.User = Depends(deps.get_current_active_user),
# ) -> Any:
#     """
#     Delete an item.
#     """
#     item = current_crud.get(db=db, id=id)
#     if not item:
#         raise HTTPException(status_code=404, detail="Item not found")
#     if not crud.user.is_superuser(current_user) and (
#         item.owner_id != current_user.id
#     ):
#         raise HTTPException(status_code=400, detail="Not enough permissions")
#     item = current_crud.remove(db=db, id=id)
#     return item
