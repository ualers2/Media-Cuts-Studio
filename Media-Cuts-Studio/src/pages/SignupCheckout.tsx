// src/components/SignupCheckout.tsx
import React, { useMemo, useState } from "react";
import { loadStripe } from "@stripe/stripe-js";

const STRIPE_KEY = (import.meta.env.VITE_STRIPE_PUBLISHABLE_KEY as string) || "";
const stripePromise = STRIPE_KEY ? loadStripe(STRIPE_KEY) : Promise.resolve(null);

export default function SignupCheckout(): JSX.Element {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  // sempre content creator (apenas esse plano)
  const plan = "content creator";
  const [billingCycle, setBillingCycle] = useState<"monthly" | "annual">("monthly");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const VITE_API_URL = (import.meta.env.VITE_API_URL as string) || "";

  // preços fixos (pode extrair para env se quiser)
  const PRICES = {
    monthly: { amount: 8, label: "$8 / mês (Dolares)" },
    annual: { amount: 88, label: "$88 / ano (1 mês grátis) (Dolares)" },
  };

  const priceLabel = useMemo(() => PRICES[billingCycle].label, [billingCycle]);
  const priceAmount = useMemo(() => PRICES[billingCycle].amount, [billingCycle]);

  function validateEmail(e: string) {
    // validação simples (suficiente para UX)
    return /\S+@\S+\.\S+/.test(e);
  }

  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault();
    setError(null);

    if (!validateEmail(email)) {
      setError("Informe um email válido.");
      return;
    }
    if (password.length < 4) {
      setError("Senha precisa ter 4 caracteres ou mais.");
      return;
    }
    if (!VITE_API_URL) {
      setError("Configuração de API ausente. Contate o time.");
      return;
    }

    setLoading(true);
    try {
      const resp = await fetch(`${VITE_API_URL}/proxy-checkout`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          email,
          password,
          plano: plan,
          billingCycle, // informa ciclo ao backend
        }),
      });

      const body = await resp.json().catch(() => ({}));
      if (!resp.ok) {
        throw new Error(body?.error || `Erro do servidor (${resp.status})`);
      }

      if (body.sessionId) {
        const stripe = await stripePromise;
        if (stripe) {
          // redireciona para o checkout do Stripe
          const result = await stripe.redirectToCheckout({ sessionId: body.sessionId });
          if ((result as any).error) {
            setError((result as any).error.message || "Erro ao redirecionar para o Stripe.");
          }
        } else {
          setError("Stripe não configurado no frontend.");
        }
      } else {
        setError("Resposta inesperada do servidor.");
      }
    } catch (err: any) {
      setError(err?.message || "Erro ao criar sessão.");
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="max-w-md mx-auto bg-white rounded-2xl shadow-md p-6">
      {/* Header */}
      <div className="flex items-start justify-between">
        <div>
          <h2 className="text-2xl font-semibold mb-1">Estamos quase Completando sua assinatura</h2>
          <p className="text-sm text-gray-600">Escolha o plano Content Creator abaixo e preencha as informacoes.</p>
        </div>
        
      </div>

      {/* Plano Card */}
      <div className="mt-5 border rounded-lg p-4 bg-gradient-to-b from-white to-gray-50">
        <div className="flex items-center justify-between">
          <div>
            <div className="text-sm font-medium">Plano</div>
            <div className="text-lg font-bold">Content Creator</div>
            <div className="text-xs text-gray-500">Ideal para criadores de conteúdo — tudo que precisa para começar.</div>
          </div>
          <div className="text-right">
            <div className="text-sm text-gray-600">Preço</div>
            <div className="text-xl font-extrabold">{priceLabel}</div>
            {billingCycle === "annual" && (
              <div className="mt-1 text-xs text-green-700 font-medium">Você ganha 1 mês grátis!</div>
            )}
          </div>
        </div>

        {/* Billing toggle */}
        <div className="mt-4">
          <div className="flex items-center gap-2 text-sm">
            <button
              type="button"
              onClick={() => setBillingCycle("monthly")}
              className={`px-3 py-1 rounded-full font-medium border ${
                billingCycle === "monthly" ? "bg-white shadow-sm" : "bg-transparent"
              }`}
              aria-pressed={billingCycle === "monthly"}
            >
              Mensal
            </button>
            {/* <button
              type="button"
              onClick={() => setBillingCycle("annual")}
              className={`px-3 py-1 rounded-full font-medium border ${
                billingCycle === "annual" ? "bg-white shadow-sm" : "bg-transparent"
              }`}
              aria-pressed={billingCycle === "annual"}
            >
              Anual
            </button> */}
            {/* <span className="ml-2 text-xs text-gray-500">Troque a cobrança quando quiser</span> */}
          </div>
        </div>

        {/* Features */}
        <ul className="mt-4 text-sm space-y-1">
          <li>• Cortes em 2K (Quad HD)</li>
          <li>• Remoção de marca d´agua nos cortes</li>
          <li>• 2 projetos em simultaneo</li>
          <li>• 90 vídeos base por mes</li>
          <li>• Acesso Instantaneo (1 a 10 minutos)</li>
          
        </ul>
      </div>

      {/* Form */}
      <form onSubmit={handleSubmit} className="mt-6 space-y-4" aria-live="polite">
        <label className="block">
          <span className="text-sm font-medium">Email</span>
          <input
            type="email"
            className="mt-1 block w-full rounded-md border px-3 py-2"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
            placeholder="seu@exemplo.com"
            aria-label="Email"
          />
        </label>

        <label className="block">
          <span className="text-sm font-medium">Senha</span>
          <input
            type="password"
            className="mt-1 block w-full rounded-md border px-3 py-2"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
            minLength={4}
            placeholder="Mínimo 4 caracteres"
            aria-label="Senha"
          />
          <p className="text-xs mt-1 text-gray-500">Mínimo 4 caracteres.</p>
        </label>

        {/* resumo do preço / CTA */}
        <div className="pt-2">
          <button
            type="submit"
            className="w-full py-3 rounded-xl bg-gradient-to-r from-blue-700 to-blue-500 text-white font-semibold flex items-center justify-center gap-3 disabled:opacity-60"
            disabled={loading}
            aria-disabled={loading}
          >
            {loading ? (
              <>
                <svg className="animate-spin h-5 w-5" viewBox="0 0 24 24">
                  <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4" fill="none" />
                  <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8v8z" />
                </svg>
                Processando...
              </>
            ) : (
              <>
                Prosseguir — {billingCycle === "monthly" ? `$${priceAmount}/mês` : `$${priceAmount}/ano`}
              </>
            )}
          </button>
          <p className="text-xs text-gray-500 mt-2">
            Você será redirecionado para o checkout seguro do Stripe.
          </p>
        </div>

        {error && (
          <div className="text-sm text-red-600 mt-1" role="alert">
            {error}
          </div>
        )}
      </form>
    </div>
  );
}
