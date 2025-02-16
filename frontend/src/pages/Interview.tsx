import { useState, useEffect } from 'react'
import useSpeechRecognition from '../hooks/useSpeechRecognitionHook'
import fish from '../assets/fish.png'
import styles from '../styles/Interview.module.css'

const Interview: React.FC = () => {
  const {
    text,
    startListening,
    stopListening,
    isListening,
    hasRecognitionSupport
  } = useSpeechRecognition()

  const [questions, setQuestions] = useState<Array<string> | null>(() => {
    const storedQuestions = localStorage.getItem("questions")
    return storedQuestions ? JSON.parse(storedQuestions) : null;
  })

  const [aiText, setAiText] = useState<string | null>(null)

  useEffect(() => {
    // You can update localStorage if needed
    if (questions !== null) {
      localStorage.setItem("questions", JSON.stringify(questions));
    }
  }, [questions]);

  // This method sends the users response to the prompt AND receives the AI's response
  const submitText = async () => {
    try {
      console.log("Text: ", text)
      const aiResponse = await fetch('http://127.0.0.1:5000/ai', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          "userResponse": text,
          "question": localStorage.getItem("questions") ?
            JSON.parse(localStorage.getItem("questions"))[0] :
            "Error retrieving question"
        }),

      })

      if (!aiResponse.ok) {
        throw new Error(`HTTP error! Status: ${aiResponse.status}`)
      }

      const data = await aiResponse.json()
      const ai = data.aiResponse
      console.log(data)
      setAiText(ai)

      // console.log("Response Data (userResponse): ", data.aiResponse.userResponse)
      // console.log("Response Data (category): ", data.aiResponse.category)
      // console.log("Response Data (userResponse): ", data.userResponse)
    } catch (err) {

    }


  }

  return (
    <div className={styles.interview_container}>
      <h1>Whenever you are ready click start!</h1>

      <img src={fish} className={styles.fish} />
      <h3>You question is: {questions != null ? questions[0] : "ERROR:QUESTION IS NULL"} </h3>

      {
        hasRecognitionSupport ? (
          <>
            <div>
              {isListening ?
                <button onClick={stopListening}>Stop</button> :
                <button onClick={startListening}>Start</button>
              }

            </div>

            {isListening ? (
              <div>!! Your browser is currently listening !!</div>
            ) : null}
            {text}
          </>

        ) : (
          <h1>Your browser has no support for speech recognition</h1>
        )
      }

      {text != "" ? (
        <button onClick={submitText}>Submit Response</button>
      ) : null}


      <h3>AI Response: {aiText}</h3>


    </div >
  )
}

export default Interview
