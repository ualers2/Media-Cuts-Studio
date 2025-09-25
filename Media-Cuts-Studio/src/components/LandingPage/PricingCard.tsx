// src/components/LandingPage/PricingCard.tsx
import React from "react";

interface PricingCardProps {
  planName: string;
  price: string;
  features: string[];
  buttonText: string;
  buttonVariant: "dark" | "purple"; // Para diferentes estilos de botão
  onClick?: () => void;   // 🔥 adiciona suporte a onClick
}

export const PricingCard: React.FC<PricingCardProps> = ({
  planName,
  price,
  features,
  buttonText,
  buttonVariant,
  onClick
}) => {
  const buttonClasses =
    buttonVariant === "purple"
      ? "bg-purple-600 hover:bg-purple-700 text-white"
      : "bg-gray-800 hover:bg-gray-700 text-white border border-gray-700";

  return (
    <div className="bg-[rgba(255,255,255,0.05)] border border-[rgba(255,255,255,0.15)] rounded-lg p-6 flex flex-col items-center text-center w-full max-w-sm">
      <h3 className="text-2xl font-bold mb-2">{planName}</h3>
      <p className="text-4xl font-bold text-purple-400 mb-6">{price}</p>
      <ul className="text-left text-gray-300 mb-8 w-full">
        {features.map((feature, index) => (
          <li key={index} className="flex items-center mb-2">
            <svg
              className="w-5 h-5 text-green-500 mr-2"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth="2"
                d="M5 13l4 4L19 7"
              ></path>
            </svg>
            {feature}
          </li>
        ))}
      </ul>
      <button 
        className={`w-full py-3 rounded-lg font-semibold ${buttonClasses}`}
        onClick={onClick}   // 🔥 agora funciona
        >
        {buttonText}
        
      </button>
    </div>
  );
};