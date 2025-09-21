// src/services/accountService.ts
export async function fetchAccountData(email: string) {
  const response = await fetch(`${import.meta.env.VITE_LANDING_API}/api/account/${email}`);
  if (!response.ok) throw new Error('Erro ao buscar dados da conta');
  return response.json();
}
