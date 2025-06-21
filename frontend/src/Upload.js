
import React, { useState } from "react";
import { uploadPDF } from "./api";

function Upload({ onUpload }) {
  const [file, setFile] = useState();
  const [loading, setLoading] = useState(false);
  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!file) return;
    setLoading(true);
    try {
      const res = await uploadPDF(file);
      onUpload(res.id);
    } catch (e) {
      alert(e.message);
    } finally {
      setLoading(false);
    }
  };
  return (
    <form onSubmit={handleSubmit}>
      <input type="file" accept=".pdf" onChange={e => setFile(e.target.files[0])} />
      <button type="submit" disabled={loading}>{loading ? "Uploading..." : "Upload"}</button>
    </form>
  );
}
export default Upload;
