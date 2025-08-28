import { use, useEffect, useState } from "react"

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

            fetch(`/api/schools/${school.id}`)
                .then(response => response.json())
                .then(data => setSchoolsStudents(prev => ({ ...prev, [school.id]: data })))
                .catch(error => console.error(`Error fetching data for school ${school.id}:`, error));
        });
        console.log(schools_students);
        console.log(total_debts);
    }, [schools]);

    return (
        <div className="container-fluid">
            <h1>Schools</h1>
            <ul>
                {schools.map(school => (
                    <div className="card" key={school.id}>
                        <div className="card-body">
                            <div className="row">    
                                <div className="col-5">
                                    <h2 className="card-title">{school.name}</h2>
                                    <div className="row">
                                        <div className="col-6">
                                            <p className="card-text">Num. de estudiantes: {schools_students[school.id]?.students?.length ?? 0}</p>
                                        </div>
                                        <div className="col-6">
                                            <p className="card-text">Deuda total: {total_debts[school.id] ?? 0}</p>
                                        </div>
                                    </div>
                                </div>
                                <div className="col-2">
                                </div>
                                <div className="col-5">
                                    <a className="btn btn-primary" href={`/schools/${school.id}`}>View Details</a>
                                </div>
                            </div>
                        </div>
                    </div>
                ))}
            </ul>
        </div>
    )
}