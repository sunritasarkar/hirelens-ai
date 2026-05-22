"use client";

import { useState } from "react";

export default function Home() {
  const [file, setFile] = useState<File | null>(null);
  const [response, setResponse] = useState("");
  const [loading, setLoading] = useState(false);

  const handleUpload = async () => {
    if (!file) return;

    setLoading(true);

    const formData = new FormData();
    formData.append("file", file);

    try {
      const res = await fetch("http://127.0.0.1:8000/upload-resume", {
        method: "POST",
        body: formData,
      });

      const data = await res.json();

      setResponse(data.extracted_text);
    } catch (error) {
      console.error(error);
      setResponse("Upload failed");
    }

    setLoading(false);
  };

  return (
    <main className="min-h-screen bg-black text-white flex flex-col items-center justify-center p-10">
      <h1 className="text-5xl font-bold mb-8">HireLens AI</h1>

      <input
        type="file"
        accept=".pdf"
        onChange={(e) => {
          if (e.target.files) {
            setFile(e.target.files[0]);
          }
        }}
        className="mb-4"
      />

      <button
        onClick={handleUpload}
        className="bg-white text-black px-6 py-3 rounded-lg font-semibold hover:bg-gray-300"
      >
        {loading ? "Uploading..." : "Upload Resume"}
      </button>

      {response && (
        <div className="mt-10 max-w-4xl bg-gray-900 p-6 rounded-lg overflow-auto max-h-[400px]">
          <h2 className="text-2xl font-bold mb-4">Extracted Resume Text</h2>
          <pre className="whitespace-pre-wrap text-sm">
            {response}
          </pre>
        </div>
      )}
    </main>
  );
}