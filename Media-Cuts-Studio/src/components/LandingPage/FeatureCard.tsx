// src/components/LandingPage/FeatureCard.tsx
import React from "react";

interface FeatureCardProps {
  icon: React.ReactNode; // Ou string para caminho de imagem/SVG
  title: string;
  description: string;
  learnMoreLink: string;
}

export const FeatureCard: React.FC<FeatureCardProps> = ({ icon, title, description, learnMoreLink }) => (
  <div className="bg-[rgba(255,255,255,0.05)] border border-[rgba(255,255,255,0.15)] rounded-lg p-6 flex flex-col items-center text-center">
    <div className="mb-4 text-purple-500 text-4xl">
      {icon}
    </div>
    <h3 className="text-xl font-bold mb-2">{title}</h3>
    <p className="text-gray-300 mb-4">{description}</p>
    <a href={learnMoreLink} className="text-purple-400 hover:text-purple-300 text-sm">
      Learn more
    </a>
  </div>
);