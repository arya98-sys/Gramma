/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
      "./src/**/*.{js,jsx,ts,tsx}",
      "./public/index.html"
    ],
    theme: {
      extend: {
        colors: {
          // AI-themed blue palette
          primary: "#2563eb", 
          secondary: "#1d4ed8",
        },
      },
    },
    plugins: [],
  }