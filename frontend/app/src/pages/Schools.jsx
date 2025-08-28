import { useEffect, useState } from "react"

export default function Schools() {
    const [schools, setSchools] = useState([])
    const [schools_invoices, setSchoolsInvoices] = useState({})
    const [schools_students, setSchoolsStudents] = useState({})
    const [total_debts, setTotalDebts] = useState({})

    useEffect(() => {
        fetch('/api/schools')
            .then(response => response.json())
            .then(data => setSchools(data))
            .catch(error => console.error('Error fetching schools:', error))
    }, [])

    useEffect(() => {
        schools.forEach(school => {
            fetch(`/api/schools/${school.id}/statement`)
                .then(response => response.json())
                .then(data => {
                    setSchoolsInvoices(prev => ({ ...prev, [school.id]: data }));
                    const totalDebt = Array.isArray(data)
                        ? data.reduce((sum, invoice) => sum + invoice.amount, 0)
                        : 0;
                    setTotalDebts(prev => ({ ...prev, [school.id]: totalDebt }));
                })
                .catch(error => console.error(`Error fetching statement for school ${school.id}:`, error));

            fetch(`/api/schools/${school.id}/students`)
                .then(response => response.json())
                .then(data => setSchoolsStudents(prev => ({ ...prev, [school.id]: data })))
                .catch(error => console.error(`Error fetching data for school ${school.id}:`, error));
        });
    }, [schools]);

    return (
        <div className="container py-4">
            <h1 className="mb-4">Escuelas</h1>
            <div className="row g-4">
                {schools.map(school => (
                    <div className="col-12 col-md-6 col-lg-4" key={school.id}>
                        <div className="card h-100 shadow-sm bg-dark text-white">
                            <div className="card-body d-flex flex-column justify-content-between">
                                <h2 className="card-title">{school.name}</h2>
                                <div className="my-3">
                                    <div className="d-flex justify-content-between">
                                        <span>
                                            <b>Estudiantes:</b> {schools_students[school.id]?.length ?? 0}
                                        </span>
                                        <span>
                                            <b>Deuda total:</b>{" "}
                                            <span className="badge bg-danger fs-6">
                                                ${total_debts[school.id] ?? 0}
                                            </span>
                                        </span>
                                    </div>
                                </div>
                                <div className="d-flex gap-2 mt-auto">
                                    <a className="btn btn-primary w-100" href={`/schools/${school.id}/students`}>
                                        Estudiantes
                                    </a>
                                    <a className="btn btn-danger w-100" href={`/schools/${school.id}/invoices`}>
                                        Facturas
                                    </a>
                                </div>
                            </div>
                        </div>
                    </div>
                ))}
            </div>
        </div>
    )
}