// src/services/userConfigService.ts
export async function fetchUserConfig(email: string) {

  const response = await fetch(`${import.meta.env.VITE_LANDING_API}/api/user-config/${email}`);
  if (!response.ok) throw new Error('Erro ao buscar configurações do usuário');
  return response.json();
}
