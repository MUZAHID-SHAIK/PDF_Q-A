import React, { useState } from "react";
import { askQuestion } from "./api";

function QA({ documentId }) {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [loading, setLoading] = useState(false);

  const handleAsk = async () => {
    if (!question.trim()) return;
    setLoading(true);
    try {
      const res = await askQuestion(documentId, question);
      setAnswer(res.answer);
    } catch (e) {
      setAnswer("Error: " + e.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <textarea
        placeholder="Ask a question about the PDF..."
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
      />
      <button onClick={handleAsk} disabled={loading}>
        {loading ? "Asking..." : "Ask"}
      </button>
      {answer && <div className="answer">{answer}</div>}
    </div>
  );
}

export default QA;
