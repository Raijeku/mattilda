from fastapi import FastAPI
from db import create_db_and_tables
from routes import student, school, invoice

app = FastAPI(
    title='School Invoice API',
    description='Maneja facturas generadas a estudiantes en escuelas',
    version='1.0.0'
)
create_db_and_tables()

@app.get('/')
async def root():
    return {'message': 'Bienvenidos al School Invoice API!'}

app.include_router(student.router)
app.include_router(school.router)
app.include_router(invoice.router)