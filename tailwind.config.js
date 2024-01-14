/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
      './templates/**/*.html',
      './node_modules/flowbite/**/*.js',
      './core/templatetags/**/*.py'
  ],
  theme: {
    colors: {
      primary : {
        DEFAULT: 'var(--primary)',
        soft: 'var(--soft-primary)',
        hard: 'var(--hard-primary)',
      },
      gray: {
        DEFAULT: 'var(--gray)',
        100: 'var(--gray-100)',
        200: 'var(--gray-200)',
        300: 'var(--gray-300)',
        400: 'var(--gray-400)',
        500: 'var(--gray-500)',
        600: 'var(--gray-600)',
        700: 'var(--gray-700)',
        800: 'var(--gray-800)',
        900: 'var(--gray-900)'
      },
      green_gray: {
        DEFAULT: 'var(--green-gray)',
        100: 'var(--green-gray-100)',
        200: 'var(--green-gray-200)',
        300: 'var(--green-gray-300)',
        400: 'var(--green-gray-400)',
        500: 'var(--green-gray-500)',
        600: 'var(--green-gray-600)',
        700: 'var(--green-gray-700)',
        800: 'var(--green-gray-800)',
        900: 'var(--green-gray-900)'
      },
      red: 'var(--danger)'
    },
    extend: {
      borderRadius: {
        '4xl': '48px'
      }
    },
  },
  plugins: [
    require('flowbite/plugin')
]

}