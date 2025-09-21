import React, { useState, useEffect, useRef } from "react";
import { Send, Minimize2, MessageCircle } from "lucide-react";

// Função para converter markdown básico para JSX com classes CSS apropriadas
const parseMarkdown = (text: string, isBot: boolean = true) => {
    let parsed = text;
    
    // Escapa HTML existente para segurança
    parsed = parsed.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
    
    // Define classes baseadas no tipo de sender
    const strongClass = isBot ? 'font-semibold text-gray-900' : 'font-semibold text-white';
    const emClass = isBot ? 'italic text-gray-600' : 'italic text-purple-100';
    const codeClass = isBot 
        ? 'bg-gray-100 text-gray-800 px-2 py-1 rounded text-xs font-mono border border-gray-200' 
        : 'bg-purple-700 text-purple-100 px-2 py-1 rounded text-xs font-mono border border-purple-400';
    
    // Converte **texto** para <strong>texto</strong>
    parsed = parsed.replace(/\*\*(.*?)\*\*/g, `<strong class="${strongClass}">$1</strong>`);
    
    // Converte *texto* para <em>texto</em>
    parsed = parsed.replace(/(?<!\*)\*(?!\*)([^*\n]+?)\*(?!\*)/g, `<em class="${emClass}">$1</em>`);
    
    // Converte `texto` para <code>texto</code>
    parsed = parsed.replace(/`([^`\n]+?)`/g, `<code class="${codeClass}">$1</code>`);
    
    // Converte quebras de linha duplas para parágrafos
    parsed = parsed.replace(/\n\n/g, '</p><p class="mt-2">');
    
    // Converte quebras de linha simples para <br>
    parsed = parsed.replace(/\n/g, '<br>');
    
    // Adiciona wrapper de parágrafo se necessário
    if (parsed.includes('</p><p')) {
        parsed = '<p class="m-0">' + parsed + '</p>';
    }
    
    return parsed;
};

// Componente para renderizar mensagem com markdown
const MessageContent: React.FC<{ text: string; sender: string }> = ({ text, sender }) => {
    const isBot = sender === "bot";
    const parsedText = parseMarkdown(text, isBot);
    
    return (
        <div
            className={`p-3 rounded-lg max-w-[85%] text-sm leading-relaxed ${
                isBot
                    ? "bg-white text-gray-800 shadow-sm border border-gray-100"
                    : "bg-purple-500 text-white shadow-sm"
            }`}
            dangerouslySetInnerHTML={{ __html: parsedText }}
            style={{
                wordBreak: 'break-word'
            }}
        />
    );
};

const ChatWidget: React.FC = () => {
    const [isOpen, setIsOpen] = useState(true);
    const [messages, setMessages] = useState([
        { sender: "bot", text: "Olá, bem-vindo ao Assistente MediaCuts!" },
        { sender: "bot", text: "Em que posso ajudar hoje?" },
    ]);
    const [inputMessage, setInputMessage] = useState("");
    const [isLoading, setIsLoading] = useState(false);
    const messagesEndRef = useRef<HTMLDivElement>(null);
    const inputRef = useRef<HTMLInputElement>(null);
    
    const VITE_SUPPORT_URL = import.meta.env.VITE_SUPPORT_URL;

    // // Auto scroll para a última mensagem
    // const scrollToBottom = () => {
    //     messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
    // };

    // useEffect(() => {
    //     scrollToBottom();
    // }, [messages]);

    // Foca no input quando o chat abre
    useEffect(() => {
        if (isOpen && inputRef.current) {
            inputRef.current.focus();
        }
    }, [isOpen]);

    const sendMessage = async (text: string) => {
        if (!text.trim()) return;

        const userMsg = { sender: "user", text: text.trim() };
        setMessages((prev) => [...prev, userMsg]);
        setInputMessage("");
        setIsLoading(true);

        try {
            const res = await fetch(`${VITE_SUPPORT_URL}/api/chat-assistant`, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ message: text.trim() }),
            });
            
            if (!res.ok) {
                throw new Error('Erro na comunicação com o servidor');
            }
            
            const data = await res.json();
            setMessages((prev) => [...prev, { sender: "bot", text: data.reply }]);
        } catch (error) {
            console.error('Erro ao enviar mensagem:', error);
            setMessages((prev) => [...prev, { 
                sender: "bot", 
                text: "Desculpe, ocorreu um erro. Tente novamente em alguns instantes." 
            }]);
        } finally {
            setIsLoading(false);
        }
    };

    const handleSubmit = (e: React.FormEvent) => {
        e.preventDefault();
        sendMessage(inputMessage);
    };

    const handleKeyPress = (e: React.KeyboardEvent) => {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            sendMessage(inputMessage);
        }
    };

    const quickActions = [
        { text: "Suporte", message: "Preciso de ajuda com suporte técnico" },
        { text: "Pagamentos", message: "Tenho dúvidas sobre pagamentos e cobrança" },
        { text: "Planos", message: "Quero saber mais sobre os planos disponíveis" },
        { text: "Como usar", message: "Como posso usar o MediaCuts Studio?" },
    ];

    return (
        <div className="fixed bottom-6 right-6 w-80 z-50">
            {isOpen && (
                <div className="bg-white rounded-xl shadow-2xl overflow-hidden flex flex-col border border-gray-200">
                    {/* Header */}
                    <div className="bg-gradient-to-r from-purple-700 to-purple-600 text-white p-4 flex justify-between items-center">
                        <div className="flex items-center gap-2">
                            <MessageCircle className="w-5 h-5" />
                            <span className="font-semibold">Chat do Cliente</span>
                        </div>
                        <button 
                            onClick={() => setIsOpen(false)}
                            className="hover:bg-white/20 p-1 rounded transition-colors"
                            aria-label="Minimizar chat"
                        >
                            <Minimize2 className="w-4 h-4" />
                        </button>
                    </div>

                    {/* Messages Area */}
                    <div className="p-4 h-72 overflow-y-auto bg-gray-50">
                        <div className="space-y-3">
                            {messages.map((msg, i) => (
                                <div
                                    key={i}
                                    className={`flex ${msg.sender === "user" ? "justify-end" : "justify-start"}`}
                                >
                                    <MessageContent text={msg.text} sender={msg.sender} />
                                </div>
                            ))}
                            
                            {/* Loading indicator */}
                            {isLoading && (
                                <div className="flex justify-start">
                                    <div className="bg-white text-gray-800 p-3 rounded-lg shadow-sm border border-gray-100">
                                        <div className="flex space-x-1">
                                            <div className="w-2 h-2 bg-purple-400 rounded-full animate-bounce"></div>
                                            <div className="w-2 h-2 bg-purple-400 rounded-full animate-bounce" style={{animationDelay: '0.1s'}}></div>
                                            <div className="w-2 h-2 bg-purple-400 rounded-full animate-bounce" style={{animationDelay: '0.2s'}}></div>
                                        </div>
                                    </div>
                                </div>
                            )}
                        </div>
                        <div ref={messagesEndRef} />
                    </div>

                    {/* Quick Actions */}
                    <div className="px-4 py-2 bg-gray-50 border-t border-gray-200">
                        <div className="flex flex-wrap gap-1">
                            {quickActions.map((action, index) => (
                                <button
                                    key={index}
                                    onClick={() => sendMessage(action.message)}
                                    disabled={isLoading}
                                    className="px-2 py-1 bg-purple-100 hover:bg-purple-200 text-purple-700 rounded text-xs transition-colors disabled:opacity-50 disabled:cursor-not-allowed"
                                >
                                    {action.text}
                                </button>
                            ))}
                        </div>
                    </div>

                    {/* Input Area */}
                    <div className="p-4 bg-white border-t border-gray-200">
                        <form onSubmit={handleSubmit} className="flex gap-2">
                            <input
                                ref={inputRef}
                                type="text"
                                value={inputMessage}
                                onChange={(e) => setInputMessage(e.target.value)}
                                onKeyPress={handleKeyPress}
                                placeholder="Digite sua mensagem..."
                                disabled={isLoading}
                                className="flex-1 px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-purple-500 focus:border-transparent text-sm disabled:opacity-50"
                            />
                            <button
                                type="submit"
                                disabled={!inputMessage.trim() || isLoading}
                                className="px-3 py-2 bg-purple-600 hover:bg-purple-700 disabled:bg-gray-300 text-white rounded-lg transition-colors disabled:cursor-not-allowed"
                                aria-label="Enviar mensagem"
                            >
                                <Send className="w-4 h-4" />
                            </button>
                        </form>
                        <p className="text-xs text-gray-500 mt-2 text-center">
                            Pressione Enter para enviar • Shift + Enter para quebra de linha
                        </p>
                    </div>
                </div>
            )}

            {/* Minimized Button */}
            {!isOpen && (
                <button
                    onClick={() => setIsOpen(true)}
                    className="w-14 h-14 rounded-full bg-gradient-to-r from-purple-600 to-purple-700 hover:from-purple-700 hover:to-purple-800 text-white shadow-lg flex items-center justify-center transition-all duration-300 hover:scale-105"
                    aria-label="Abrir chat"
                >
                    <MessageCircle className="w-6 h-6" />
                </button>
            )}
        </div>
    );
};

export default ChatWidget;