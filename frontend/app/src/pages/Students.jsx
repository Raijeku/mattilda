import { useEffect, useState } from "react"
import { useParams } from 'react-router-dom'
import React from "react"

export default function Students() {
    const [students, setStudents] = useState([])
    const [students_invoices, setStudentsInvoices] = useState({})
    const [total_debts, setTotalDebts] = useState({})
    const { school_id } = useParams()
    const [showForm, setShowForm] = useState({})
    const [formData, setFormData] = useState({})

    useEffect(() => {
        fetch('/api/students')
            .then(response => response.json())
            .then(data => setStudents(data))
            .catch(error => console.error('Error fetching students:', error))
    }, [])

    useEffect(() => {
        students.forEach(student => {
            fetch(`/api/students/${student.id}/statement`)
                .then(response => response.json())
                .then(data => {
                    setStudentsInvoices(prev => ({ ...prev, [student.id]: data }));
                    const totalDebt = Array.isArray(data)
                        ? data.reduce((sum, invoice) => sum + invoice.amount, 0)
                        : 0;
                    setTotalDebts(prev => ({ ...prev, [student.id]: totalDebt }));
                })
                .catch(error => console.error(`Error fetching statement for school ${student.school_id}:`, error));
        })
    }, [students]);

    const handleInputChange = (studentId, field, value) => {
        setFormData(prev => ({
            ...prev,
            [studentId]: {
                ...prev[studentId],
                [field]: value
            }
        }))
    }

    const handleSubmit = (studentId, schoolId) => {
        const { amount, description } = formData[studentId] || {}
        fetch('/api/invoices', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                amount: Number(amount),
                description,
                student_id: studentId,
                school_id: schoolId
            })
        })
        .then(response => response.json())
        .then(data => {
            alert('Factura creada correctamente')
            setShowForm(prev => ({ ...prev, [studentId]: false }))
            setFormData(prev => ({ ...prev, [studentId]: {} }))
        })
        .catch(error => alert('Error al crear la factura'))
    }

    return (
        <div className="container py-4">
            <div className="d-flex justify-content-between align-items-center mb-4">
                <h1 className="mb-0">Estudiantes</h1>
                <a href={`/schools`} className="btn btn-outline-secondary">Volver a escuelas</a>
            </div>
            <div className="card shadow-sm">
                <div className="card-body">
                    <div className="table-responsive">
                        <table className="table table-hover align-middle">
                            <thead className="table-dark">
                                <tr>
                                    <th>ID</th>
                                    <th>Nombre</th>
                                    <th>Deuda total</th>
                                    <th>ID Escuela</th>
                                    <th>Acciones</th>
                                </tr>
                            </thead>
                            <tbody>
                                {students.filter(student => student.school_id == school_id).map(student => (
                                    <React.Fragment key={student.id}>
                                        <tr>
                                            <td>{student.id}</td>
                                            <td>{student.name}</td>
                                            <td>
                                                <span className="badge bg-danger fs-6">
                                                    ${total_debts[student.id] ?? 0}
                                                </span>
                                            </td>
                                            <td>{student.school_id}</td>
                                            <td>
                                                <button
                                                    className="btn btn-success btn-sm"
                                                    onClick={() => setShowForm(prev => ({ ...prev, [student.id]: !prev[student.id] }))}
                                                >
                                                    Nueva factura
                                                </button>
                                            </td>
                                        </tr>
                                        {showForm[student.id] && (
                                            <tr>
                                                <td colSpan={5}>
                                                    <div className="d-flex flex-wrap gap-2 justify-content-center align-items-center py-2 bg-light rounded">
                                                        <input
                                                            type="number"
                                                            className="form-control form-control-sm"
                                                            placeholder="Monto"
                                                            value={formData[student.id]?.amount || ''}
                                                            onChange={e => handleInputChange(student.id, 'amount', e.target.value)}
                                                            style={{ maxWidth: 120 }}
                                                        />
                                                        <input
                                                            type="text"
                                                            className="form-control form-control-sm"
                                                            placeholder="Descripción"
                                                            value={formData[student.id]?.description || ''}
                                                            onChange={e => handleInputChange(student.id, 'description', e.target.value)}
                                                            style={{ maxWidth: 200 }}
                                                        />
                                                        <button
                                                            className="btn btn-primary btn-sm"
                                                            onClick={() => handleSubmit(student.id, student.school_id)}
                                                        >
                                                            Guardar
                                                        </button>
                                                        <button
                                                            className="btn btn-outline-secondary btn-sm"
                                                            onClick={() => setShowForm(prev => ({ ...prev, [student.id]: false }))}
                                                        >
                                                            Cancelar
                                                        </button>
                                                    </div>
                                                </td>
                                            </tr>
                                        )}
                                    </React.Fragment>
                                ))}
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>
    )
}