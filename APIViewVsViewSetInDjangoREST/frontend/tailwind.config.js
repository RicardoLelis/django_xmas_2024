/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    '../templates/**/*.html', // Include global templates
    '../**/templates/**/*.html', // Include app-specific templates
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}

