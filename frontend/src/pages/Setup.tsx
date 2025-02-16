import styles from '../styles/setup.module.css'
import React, { useState, ChangeEvent } from 'react'
import { useNavigate } from "react-router-dom";

const Setup: React.FC = () => {
  const navigate = useNavigate()
  interface FormData {
    experience: string
    question_amt: string
    complexity: string
    profession: string
  }

  const [formData, setFormData] = useState<FormData>({
    experience: '',
    question_amt: '',
    complexity: '',
    profession: '',
  })

  const handleChange = (e: ChangeEvent<HTMLSelectElement>) => {
    const { name, value } = e.target
    setFormData(prevData => ({
      ...prevData,
      [name]: value,
    }))
  }

  const handleSubmit = async () => {
    localStorage.setItem("experience", formData.experience)
    localStorage.setItem("question_amt", formData.question_amt)
    localStorage.setItem("complexity", formData.complexity)
    localStorage.setItem("profession", formData.profession)

    try {
      const response = await fetch('http://127.0.0.1:5000/metadata', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData),
      })

      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`)
      }

      const data = await response.json()  // Properly parse the JSON response
      console.log("Response Data: ", data.questions)
      localStorage.setItem("questions", JSON.stringify(data.questions))
      navigate("/interview")
    } catch (error) {

      console.error("Fetch Error: ", error)
    }
  }

  return (
    <div className={styles.setup_container}>
      <h1 className={styles.metadata}>Interview Options</h1>
      <div className={styles.forms}>
        <br />

        <div className={styles.combo}>
          <h1>Experience:</h1>
          <select name="experience" value={formData.experience} onChange={handleChange}>
            <option value="">Select</option>
            <option value="Entry-level">Entry-level</option>
            <option value="Mid-level">Mid-level</option>
            <option value="Senior">Senior</option>
          </select>
        </div>
        <br />
        <div className={styles.combo}>
          <h1># of Questions:</h1>
          <select name="question_amt" value={formData.question_amt} onChange={handleChange}>
            <option value="">Select</option>
            <option value="1">1</option>
            <option value="2">2</option>
            <option value="3">3</option>
            <option value="4">4</option>
            <option value="5">5</option>
          </select>
        </div>
        <br />
        <div className={styles.combo}>
          <h1>Complexity:</h1>
          <select name="complexity" value={formData.complexity} onChange={handleChange}>
            <option value="">Select</option>
            <option value="random">Random</option>
            <option value="Easy">Easy</option>
            <option value="Medium">Medium</option>
            <option value="Hard">Hard</option>
          </select>
        </div>
        <br />
        <div className={styles.combo}>
          <h1>Profession:</h1>
          <select name="profession" value={formData.profession} onChange={handleChange}>
            <option value="">Select</option>
            <option value="General">General</option>
            <option value="Healthcare">Healthcare</option>
            <option value="Computer Science">Computer Science</option>
            <option value="Finance">Finance & Accounting</option>
            <option value="Marketing">Marketing & Sales</option>
          </select>
        </div>
      </div>

      <button className={styles.submit_meta} onClick={handleSubmit}>Submit</button>
    </div>
  )
}

export default Setup

