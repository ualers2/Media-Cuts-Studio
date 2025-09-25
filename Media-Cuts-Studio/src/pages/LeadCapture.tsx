// src/pages/LeadCapture.tsx
import React, { useState } from "react";
import { motion } from "framer-motion";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Card, CardHeader, CardTitle, CardContent } from "@/components/ui/card";
import { User, Mail, Phone } from "lucide-react";

export default function LeadCapture() {
    const [form, setForm] = useState({ name: "", email: "", whatsapp: "" });

    const API_BASE_URL = import.meta.env.VITE_LANDING_API || 'http://localhost:5000';

    const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        setForm({ ...form, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        try {
            const res = await fetch(`${API_BASE_URL}/api/leads`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(form),
            });

            if (!res.ok) throw new Error("Erro ao salvar lead");

            const data = await res.json();
            console.log("Lead salvo:", data);

            alert("✅ Inscrição realizada com sucesso!");
            setForm({ name: "", email: "", whatsapp: "" });
        } catch (error) {
            console.error(error);
            alert("❌ Erro ao enviar inscrição, tente novamente.");
        }
    };

    return (
        <div className="min-h-screen bg-gray-50 flex items-center justify-center px-4">
        <motion.div
            initial={{ opacity: 0, y: 30 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.6 }}
            className="w-full max-w-md"
        >
            <Card className="shadow-xl rounded-2xl border border-gray-200 bg-white">
            <CardHeader className="text-center">
                <img
                src="/logo-branco-removebg-preview (2).png"
                alt="Media Cuts Studio"
                className="mx-auto mb-10 w-10"
                />
                <CardTitle className="text-2xl font-bold text-blue-900 font-poppins">
                Poste Todo Dia Sem Editar Nada!. 🚀
                </CardTitle>
                <p className="mt-2 text-gray-600 font-inter">
                Inscreva-se para receber acesso gratuito e começar sua jornada.
                </p>
            </CardHeader>
            <CardContent>
                <form onSubmit={handleSubmit} className="space-y-4">
                <div className="relative">
                    <User className="absolute left-3 top-3 h-5 w-5 text-gray-400" />
                    <Input
                    name="name"
                    placeholder="Seu nome"
                    value={form.name}
                    onChange={handleChange}
                    required
                    className="pl-10"
                    />
                </div>
                <div className="relative">
                    <Mail className="absolute left-3 top-3 h-5 w-5 text-gray-400" />
                    <Input
                    type="email"
                    name="email"
                    placeholder="Seu e-mail"
                    value={form.email}
                    onChange={handleChange}
                    required
                    className="pl-10"
                    />
                </div>
                <div className="relative">
                    <Phone className="absolute left-3 top-3 h-5 w-5 text-gray-400" />
                    <Input
                    type="tel"
                    name="whatsapp"
                    placeholder="WhatsApp (opcional)"
                    value={form.whatsapp}
                    onChange={handleChange}
                    className="pl-10"
                    />
                </div>
                <Button
                    type="submit"
                    className="w-full bg-blue-600 hover:bg-blue-700 text-white font-inter font-medium rounded-xl py-3"
                >
                    Quero me inscrever
                </Button>
                <p className="text-xs text-center text-gray-400 font-inter">
                    Ao enviar, você concorda com nossa{" "}
                    <a href="/privacy-policy" className="underline">
                    política de privacidade
                    </a>.
                </p>
                </form>
            </CardContent>
            </Card>
        </motion.div>
        </div>
    );
}
