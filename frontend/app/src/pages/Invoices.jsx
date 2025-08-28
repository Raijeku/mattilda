import { useEffect, useState } from "react"
import { useParams } from 'react-router-dom'

export default function Invoices() {
    const [invoices, setInvoices] = useState([])
    const [students, setStudents] = useState({})
    const { school_id } = useParams()

    useEffect(() => {
        fetch('/api/invoices')
            .then(response => response.json())
            .then(data => setInvoices(data))
            .catch(error => console.error('Error fetching invoices:', error))
    }, [])

    useEffect(() => {
        invoices.forEach(invoice => {
            fetch(`/api/students/${invoice.student_id}`)
                .then(response => response.json())
                .then(data => {
                    setStudents(prev => ({ ...prev, [invoice.student_id]: data }));
                })
                .catch(error => console.error(`Error fetching student for invoice ${invoice.id}:`, error));
        })
    }, [invoices]);

    return (
        <div className="container py-4">
            <div className="d-flex justify-content-between align-items-center mb-4">
                <h1 className="mb-0">Facturas</h1>
                <a href={`/schools/${school_id}/students`} className="btn btn-outline-secondary">Ver estudiantes</a>
            </div>
            <div className="card shadow-sm">
                <div className="card-body">
                    <div className="table-responsive">
                        <table className="table table-hover align-middle">
                            <thead className="table-dark">
                                <tr>
                                    <th>ID</th>
                                    <th>Nombre estudiante</th>
                                    <th>Descripción</th>
                                    <th>Deuda</th>
                                    <th>ID Escuela</th>
                                </tr>
                            </thead>
                            <tbody>
                                {invoices.filter(invoice => students[invoice.student_id]?.school_id == school_id).map(invoice => (
                                    <tr key={invoice.id}>
                                        <td>{invoice.id}</td>
                                        <td>{students[invoice.student_id]?.name}</td>
                                        <td>{invoice.description}</td>
                                        <td>
                                            <span className="badge bg-danger fs-6">
                                                ${invoice.amount}
                                            </span>
                                        </td>
                                        <td>{students[invoice.student_id]?.school_id}</td>
                                    </tr>
                                ))}
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>
    )
}