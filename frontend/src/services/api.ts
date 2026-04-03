/// <reference types="vite/client" />

const API_URL = import.meta.env.VITE_API_URL;

export const downloadVideo = async (formData: FormData) => {
  const response = await fetch(`${API_URL}/download`, {
    method: "POST",
    body: formData,
  });

  if (!response.ok) {
    throw new Error("Download failed");
  }

  return response.json();
};