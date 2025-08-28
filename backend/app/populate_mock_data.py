from app.db import get_session, create_db_and_tables
from app.models.school import School
from app.models.student import Student
from app.models.invoice import Invoice

def populate():
    create_db_and_tables()
    session = next(get_session())

    # Escuelas
    escuelas = [
        School(name="Escuela Primaria Benito Juárez"),
        School(name="Colegio Nacional de Ciencias"),
        School(name="Instituto Tecnológico Moderno"),
        School(name="Escuela Secundaria Sor Juana"),
        School(name="Instituto Bilingüe Siglo XXI")
    ]
    session.add_all(escuelas)
    session.commit()

    # Estudiantes
    estudiantes = [
        Student(name="Juan Pérez", school_id=escuelas[0].id),
        Student(name="María López", school_id=escuelas[0].id),
        Student(name="Carlos Sánchez", school_id=escuelas[1].id),
        Student(name="Ana Torres", school_id=escuelas[1].id),
        Student(name="Luis Ramírez", school_id=escuelas[2].id),
        Student(name="Sofía Martínez", school_id=escuelas[2].id),
        Student(name="Pedro Gómez", school_id=escuelas[3].id),
        Student(name="Lucía Fernández", school_id=escuelas[3].id),
        Student(name="Miguel Herrera", school_id=escuelas[4].id),
        Student(name="Valentina Cruz", school_id=escuelas[4].id)
    ]
    session.add_all(estudiantes)
    session.commit()

    # Facturas
    facturas = [
        Invoice(amount=1500.0, description="Pago de inscripción", student_id=estudiantes[0].id),
        Invoice(amount=1200.0, description="Pago de libros", student_id=estudiantes[0].id),
        Invoice(amount=1300.0, description="Pago de inscripción", student_id=estudiantes[1].id),
        Invoice(amount=1100.0, description="Pago de laboratorio", student_id=estudiantes[2].id),
        Invoice(amount=1400.0, description="Pago de inscripción", student_id=estudiantes[3].id),
        Invoice(amount=1250.0, description="Pago de materiales", student_id=estudiantes[4].id),
        Invoice(amount=1350.0, description="Pago de excursión", student_id=estudiantes[5].id),
        Invoice(amount=1450.0, description="Pago de uniforme", student_id=estudiantes[6].id),
        Invoice(amount=1550.0, description="Pago de inscripción", student_id=estudiantes[7].id),
        Invoice(amount=1600.0, description="Pago de libros", student_id=estudiantes[8].id),
        Invoice(amount=1700.0, description="Pago de laboratorio", student_id=estudiantes[9].id),
        Invoice(amount=1800.0, description="Pago de excursión", student_id=estudiantes[9].id)
    ]
    session.add_all(facturas)
    session.commit()
    session.close()
    print("¡Datos de ejemplo insertados correctamente!")

if __name__ == "__main__":
    populate()