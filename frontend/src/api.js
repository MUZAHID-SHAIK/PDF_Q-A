// api.js
const BASE_URL = "http://127.0.0.1:8000";

export const uploadPDF = async (file) => {
  const formData = new FormData();
  formData.append("file", file);
  const response = await fetch(`${BASE_URL}/upload`, {
    method: "POST",
    body: formData,
  });
  return response.json();
};

export const askQuestion = async (documentId, question) => {
  const response = await fetch(`${BASE_URL}/ask`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ document_id: documentId, question }),
  });
  return response.json();
};
