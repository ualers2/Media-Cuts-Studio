import type { Config } from "tailwindcss";

export default {
  darkMode: ["class"],
  content: [
    "./pages/**/*.{ts,tsx}",
    "./components/**/*.{ts,tsx}",
    "./app/**/*.{ts,tsx}",
    "./src/**/*.{ts,tsx}",
  ],
  theme: {
    container: {
      center: true,
      padding: "2rem",
      screens: {
        "2xl": "1400px",
      },
    },
    extend: {
      colors: {
        border: "hsl(var(--border))",
        input: "hsl(var(--input))",
        ring: "hsl(var(--ring))",
        background: "hsl(var(--background))",
        foreground: "hsl(var(--foreground))",
        primary: {
          DEFAULT: "#090014", // roxo
          foreground: "#ffffff",
        },
        secondary: {
          DEFAULT: "#64748b", // Azul acinzentado
          foreground: "#ffffff",
        },
        accent: {
          DEFAULT: "#090014", // Roxo
          foreground: "#ffffff",
        },
        muted: {
          DEFAULT: "#f1f5f9", // Cinza claro
          foreground: "#334155",
        },
        destructive: {
          DEFAULT: "#ef4444", // Vermelho
          foreground: "#ffffff",
        },
        card: {
          DEFAULT: "#ffffff",
          foreground: "#0f172a",
        },
        popover: {
          DEFAULT: "#f8fafc",
          foreground: "#0f172a",
        },
        sidebar: {
          DEFAULT: "#ffffff",
          foreground: "#00030a",
          primary: "#0f172a",
          "primary-foreground": "#f1f5f9",
          accent: "#090014",
          "accent-foreground": "#ffffff",
          border: "#334155",
          ring: "#1e40af",
        },
      },
      borderRadius: {
        lg: "1rem",
        md: "0.75rem",
        sm: "0.5rem",
      },
      fontFamily: {
        sans: ["Inter", "ui-sans-serif", "system-ui"],
      },
      keyframes: {
        "accordion-down": {
          from: { height: "0" },
          to: { height: "var(--radix-accordion-content-height)" },
        },
        "accordion-up": {
          from: { height: "var(--radix-accordion-content-height)" },
          to: { height: "0" },
        },
        "fade-in": {
          "0%": { opacity: "0", transform: "translateY(7px)" },
          "100%": { opacity: "1", transform: "translateY(0)" },
        },
      },
      animation: {
        "accordion-down": "accordion-down 0.2s ease-out",
        "accordion-up": "accordion-up 0.2s ease-out",
        "fade-in": "fade-in 0.3s ease-out",
      },
      boxShadow: {
        card: "0 4px 14px 0 rgba(0, 0, 0, 0.05)",
        input: "0 1px 2px 0 rgba(0, 0, 0, 0.05)",
      },
    },
  },
  plugins: [require("tailwindcss-animate")],
} satisfies Config;
