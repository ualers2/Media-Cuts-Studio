// tailwind.config.js
module.exports = {
  darkMode: 'class', // <--- Garanta que esta linha esteja presente
  content: [
    './index.html',
    './src/**/*.{js,ts,jsx,tsx}',
  ],
  theme: {
    extend: {
      colors: {
        'primary-purple': '#6A4BFF',
        'primary-purple-dark': '#5A3FD9',
        'primary-purple-light': '#8B70FF',
        'deep-purple': '#100720',
        'accent-blue': '#7EABE6',
        'background-light': '#F2F2FF',
        'gray-text': '#969696',
        'gray-dark': '#343434',
        'white': '#FFFFFF',
        'black': '#000000',
        'border-light': '#EAEAEA',
        'border-dark': '#222222',
      },
      // Adicione os gradientes como background
      backgroundImage: {
        'gradient-hero': 'linear-gradient(180deg, #ebe6f1ff 0%, #ffffffff 50%, #cececeff 100%)',
        'gradient-card': 'linear-gradient(180deg, #362944ff 0%, #dcd9e0ff 100%)',
        'gradient-background': 'linear-gradient(180deg, #ffffffff 0%, #816aa3ff 34%, #ffffffff 100%)',
      },
    }
  },
  plugins: [],
};