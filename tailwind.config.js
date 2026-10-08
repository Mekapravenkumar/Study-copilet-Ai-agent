/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        navy: {
          950: '#060913',
          900: '#0B0F19',
          800: '#111827',
          700: '#1F2937'
        },
        brand: {
          purple: '#8B5CF6',
          cyan: '#06B6D4',
          blue: '#3B82F6'
        }
      }
    },
  },
  plugins: [],
}
