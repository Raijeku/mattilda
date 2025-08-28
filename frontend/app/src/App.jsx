import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import Schools from './pages/Schools'
import Students from './pages/Students'
import Invoices from './pages/Invoices'
import { Route, Routes } from 'react-router-dom'

function App() {

  return (
    <>
      <Routes>
        <Route path="/" element={<Schools />} />
        <Route path="/schools/:school_id/students" element={<Students />} />
        <Route path="/schools/:school_id/invoices" element={<Invoices />} />
        <Route path="*" element={<Schools />} />
      </Routes>
    </>
  )
}

export default App
