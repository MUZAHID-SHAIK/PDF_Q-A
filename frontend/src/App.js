import React, { useState } from "react";
import Upload from "./Upload";
import QA from "./QA";
import "./styles.css";

function App() {
  const [docId, setDocId] = useState(null);

  return (
    <div className="App">
      <h1>PDF Q&A App</h1>
      <Upload onUpload={setDocId} />
      {docId && <QA documentId={docId} />}
    </div>
  );
}

export default App;
