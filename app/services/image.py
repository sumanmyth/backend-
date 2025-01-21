from app.schemas.image import ImageResponse
from app.core.db import get_db
from sqlalchemy.orm import Session
from fastapi import FastAPI, File, UploadFile, HTTPException, Depends
import os
import shutil
from fastapi.responses import JSONResponse
from app.models.image import Image

# Synchronous function to save the image info into the DB
def upload_image_to_db(db: Session, filename: str):
    image = Image(name=filename)
    db.add(image)
    db.commit()
    db.refresh(image)
    return image

# FastAPI endpoint to upload image
async def upload_image(file: UploadFile = File(...), db: Session = Depends(get_db)):
    try:
        upload_dir = "uploads"
        if not os.path.exists(upload_dir):
            os.makedirs(upload_dir)

        file_path = os.path.join(upload_dir, file.filename)
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)  # Save file to disk

        # Save image record to the DB
        uploaded_image = upload_image_to_db(db, file.filename)  # This is a blocking operation, hence no 'await'

        return ImageResponse.from_orm(uploaded_image)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

