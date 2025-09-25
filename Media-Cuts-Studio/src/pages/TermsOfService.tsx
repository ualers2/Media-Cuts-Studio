import { Link } from "react-router-dom";
import { ArrowLeft, FileText, Mail, Calendar, AlertCircle } from "lucide-react";
import { Button } from "@/components/ui/button";
import { Card } from "@/components/ui/card";
import { Alert, AlertDescription } from "@/components/ui/alert";
import "../styles/legal-theme.css";

const TermsOfService = () => {
  return (
    <div className="legal-theme min-h-screen bg-gradient-to-br from-background to-legal-section">
      {/* Header */}
      <header className="border-b bg-background/95 backdrop-blur supports-[backdrop-filter]:bg-background/60 sticky top-0 z-50">
        <div className="container max-w-6xl mx-auto px-4 py-4">
          <div className="flex items-center justify-between">
            <div className="flex items-center gap-4">
              <Link to="/shortify">
                <Button variant="ghost" size="sm" className="gap-2">
                  <ArrowLeft className="h-4 w-4" />
                  Voltar
                </Button>
              </Link>
              <div className="flex items-center gap-2">
                <FileText className="h-6 w-6 text-primary" />
                <h1 className="text-xl font-semibold">Media Cuts Studio</h1>
              </div>
            </div>
            <Link to="/privacy-policy">
              <Button variant="outline" size="sm">
                Política de Privacidade
              </Button>
            </Link>
          </div>
        </div>
      </header>


      {/* Content */}
      <main className="container max-w-4xl mx-auto px-4 py-8">
        <Card className="p-8 shadow-lg">
          {/* Title Section */}
          <div className="text-center mb-8">
            <h1 className="text-3xl font-bold text-legal-heading mb-4">
              Termos de Uso
            </h1>
            <div className="flex items-center justify-center gap-2 text-muted-foreground">
              <Calendar className="h-4 w-4" />
              <span>Data de Vigência: 01 de agosto de 2025</span>
            </div>
          </div>

          {/* Beta Warning */}
          <Alert className="mb-6 border-primary/20 bg-primary/5">
            <AlertCircle className="h-4 w-4" />
            <AlertDescription className="text-legal-text">
              <strong>IMPORTANTE:</strong> O Media Cuts Studio está em fase de testes (beta). Isso significa que ele pode conter bugs, erros, funcionalidades incompletas e não operacionais, e pode sofrer alterações significativas a qualquer momento. O uso do Software Beta é por sua conta e risco.
            </AlertDescription>
          </Alert>

          <div className="prose prose-lg max-w-none space-y-6">
            <p className="text-legal-text leading-relaxed">
              Bem-vindo ao Media Cuts Studio ("o Software Beta" ou "o Serviço"). Estes Termos de Uso ("Termos") regem o seu acesso e uso do software Media Cuts Studio em sua fase beta, desenvolvido por Ualerson Rodrigues de Freitas e Media Cuts Studio ("nós", "nosso", ou "o Desenvolvedor").
            </p>

            <section className="bg-legal-section p-6 rounded-lg">
              <h2 className="text-xl font-semibold text-legal-heading mb-4">
                1. Aceitação dos Termos
              </h2>
              <p className="text-legal-text mb-4">
                Ao utilizar o Media Cuts Studio, você declara que:
              </p>
              <ul className="space-y-2 text-legal-text">
                <li>• Leu, compreendeu e concordou com estes Termos de Uso e com nossa Política de Privacidade.</li>
                <li>• Tem idade legal para celebrar contratos vinculativos em sua jurisdição (geralmente 18 anos ou mais).</li>
                <li>• Não está proibido de receber serviços sob as leis do Brasil ou outras jurisdições aplicáveis.</li>
              </ul>
            </section>

            <section>
              <h2 className="text-xl font-semibold text-legal-heading mb-4">
                2. Natureza Beta do Software e Isenção de Garantias
              </h2>
              
              <div className="space-y-4">
                <div className="bg-legal-section p-4 rounded">
                  <h3 className="font-semibold text-legal-heading mb-2">2.1. Software Beta:</h3>
                  <p className="text-legal-text">Você reconhece que o Media Cuts Studio é uma versão de pré-lançamento e não uma versão final. Ele pode conter bugs, erros, falhas de funcionamento, interrupções, e pode não operar como pretendido ou de forma ininterrupta.</p>
                </div>

                <div className="bg-legal-section p-4 rounded">
                  <h3 className="font-semibold text-legal-heading mb-2">2.2. Sem Garantias:</h3>
                  <p className="text-legal-text">O Software Beta é fornecido "no estado em que se encontra" e "conforme disponível", sem garantias de qualquer tipo, expressas ou implícitas.</p>
                </div>

                <div className="bg-legal-section p-4 rounded">
                  <h3 className="font-semibond text-legal-heading mb-2">2.3. Exclusão de Responsabilidade:</h3>
                  <p className="text-legal-text">O Desenvolvedor não será responsável por quaisquer danos diretos, indiretos, incidentais, especiais, consequenciais ou exemplares decorrentes do uso do Software Beta.</p>
                </div>

                <div className="bg-destructive/10 p-4 rounded border border-destructive/20">
                  <h3 className="font-semibold text-destructive mb-2">2.4. Perda de Dados:</h3>
                  <p className="text-legal-text">Existe o risco de perda de dados e/ou informações criadas, editadas ou armazenadas através do Software Beta. Você concorda em fazer backup de seus dados e não confiar no Software Beta para o armazenamento exclusivo de suas informações.</p>
                </div>
              </div>
            </section>

            <section>
              <h2 className="text-xl font-semibold text-legal-heading mb-4">
                3. Registro de Conta e Segurança
              </h2>
              <ul className="space-y-2 text-legal-text">
                <li><strong>Criação de Conta:</strong> Para acessar certas funcionalidades do Media Cuts Studio, você pode precisar criar uma conta, fornecendo um endereço de e-mail e outras informações.</li>
                <li><strong>Informações Precisas:</strong> Você concorda em fornecer informações de registro precisas, completas e atualizadas.</li>
                <li><strong>Responsabilidade pela Conta:</strong> Você é responsável por manter a confidencialidade de sua senha e por todas as atividades que ocorrem em sua conta.</li>
              </ul>
            </section>

            <section>
              <h2 className="text-xl font-semibold text-legal-heading mb-4">
                4. Licença de Uso do Software Beta
              </h2>
              
              <div className="bg-primary/5 p-4 rounded mb-4">
                <h3 className="font-semibold text-legal-heading mb-2">4.1. Concessão de Licença:</h3>
                <p className="text-legal-text">Sujeito à sua conformidade com estes Termos, o Desenvolvedor concede a você uma licença limitada, não exclusiva, não transferível, revogável e não sublicenciável para usar o Software Beta para fins de testes e feedback.</p>
              </div>

              <div className="bg-legal-section p-4 rounded">
                <h3 className="font-semibold text-legal-heading mb-2">4.2. Restrições de Uso:</h3>
                <p className="text-legal-text mb-2">Você não pode:</p>
                <ul className="space-y-1 text-legal-text text-sm">
                  <li>• Modificar, adaptar, traduzir, fazer engenharia reversa, descompilar, desmontar ou tentar extrair o código-fonte do Software Beta.</li>
                  <li>• Vender, alugar, arrendar, distribuir, transferir, licenciar ou sublicenciar o Software Beta.</li>
                  <li>• Usar o Software Beta para fins comerciais que não estejam explicitamente autorizados.</li>
                  <li>• Usar o Software Beta para qualquer finalidade ilegal ou não autorizada.</li>
                  <li>• Usar o Software Beta para criar, armazenar ou transmitir materiais ilegais, difamatórios, abusivos ou obscenos.</li>
                </ul>
              </div>
            </section>

            <section>
              <h2 className="text-xl font-semibold text-legal-heading mb-4">
                5. Conteúdo do Usuário e Direitos de Propriedade
              </h2>
              
              <div className="space-y-4">
                <div className="bg-legal-section p-4 rounded">
                  <h3 className="font-semibold text-legal-heading mb-2">5.1. Responsabilidade pelo Conteúdo:</h3>
                  <p className="text-legal-text">Você é o único responsável pelo conteúdo que você cria, envia, edita ou compartilha usando o Media Cuts Studio. Você declara e garante que possui todos os direitos necessários para o conteúdo que você submete.</p>
                </div>

                <div className="bg-legal-section p-4 rounded">
                  <h3 className="font-semibold text-legal-heading mb-2">5.2. Concessão de Licença ao Desenvolvedor:</h3>
                  <p className="text-legal-text">Ao usar o Media Cuts Studio para criar ou editar conteúdo, você concede ao Desenvolvedor uma licença limitada, não exclusiva, global e isenta de royalties para hospedar, armazenar, transmitir e exibir seu conteúdo, conforme necessário para operar o Serviço.</p>
                </div>

                <div className="bg-legal-section p-4 rounded">
                  <h3 className="font-semibold text-legal-heading mb-2">5.3. Propriedade Intelectual:</h3>
                  <p className="text-legal-text">Todo o conteúdo gerado pelo Media Cuts Studio (excluindo seu vídeo base original, mas incluindo os cortes, legendas e outros elementos gerados pelo software), bem como o próprio software, são de propriedade exclusiva do Desenvolvedor.</p>
                </div>
              </div>
            </section>

            <section>
              <h2 className="text-xl font-semibold text-legal-heading mb-4">
                6. Feedback e Sugestões
              </h2>
              <p className="text-legal-text mb-4">
                O Desenvolvedor valoriza seu feedback, sugestões, relatórios de bugs, ideias de aprimoramento e qualquer outra informação ("Feedback") que você possa fornecer relacionada ao Software Beta.
              </p>
              <div className="bg-primary/5 p-4 rounded">
                <p className="text-legal-text">
                  <strong>Concessão de Direitos ao Feedback:</strong> Ao enviar Feedback, você concede ao Desenvolvedor uma licença irrevogável, perpétua, mundial, não exclusiva, livre de royalties e totalmente sublicenciável para usar, reproduzir, distribuir e explorar o Feedback para qualquer finalidade.
                </p>
              </div>
            </section>

            <section>
              <h2 className="text-xl font-semibold text-legal-heading mb-4">
                7. Limitações de Uso e Conteúdo (Planos Beta)
              </h2>
              <p className="text-legal-text mb-4">
                As seguintes limitações serão aplicadas à sua conta de usuário, conforme detalhado nos planos de assinatura aplicáveis à fase beta:
              </p>
              <ul className="grid grid-cols-1 md:grid-cols-2 gap-2 text-legal-text">
                <li>• Limitações do Algoritmo AI Curation</li>
                <li>• Contas TikTok Conectadas limitadas</li>
                <li>• Agendamento de Criação de Cortes limitado</li>
                <li>• Controle de Tema limitado</li>
                <li>• Limitações de Requisições diárias</li>
              </ul>
            </section>

            <section>
              <h2 className="text-xl font-semibold text-legal-heading mb-4">
                8. Encerramento da Conta e Suspensão
              </h2>
              <div className="space-y-4">
                <div className="bg-legal-section p-4 rounded">
                  <h3 className="font-semibold text-legal-heading mb-2">Por Você:</h3>
                  <p className="text-legal-text">Você pode encerrar sua conta a qualquer momento, entrando em contato conosco através do e-mail mediacutsstudio@gmail.com.</p>
                </div>
                <div className="bg-legal-section p-4 rounded">
                  <h3 className="font-semibold text-legal-heading mb-2">Por Nós:</h3>
                  <p className="text-legal-text">O Desenvolvedor pode suspender ou encerrar sua conta e seu acesso ao Software Beta a qualquer momento, com ou sem aviso prévio, por qualquer motivo, incluindo violação destes Termos.</p>
                </div>
                <div className="bg-legal-section p-4 rounded">
                  <h3 className="font-semibold text-legal-heading mb-2">Fim do Programa Beta:</h3>
                  <p className="text-legal-text">O Desenvolvedor reserva-se o direito de encerrar o programa beta a qualquer momento, sem aviso prévio.</p>
                </div>
              </div>
            </section>

            <section>
              <h2 className="text-xl font-semibold text-legal-heading mb-4">
                9. Links para Sites de Terceiros
              </h2>
              <p className="text-legal-text">
                O Media Cuts Studio pode conter links para sites ou serviços de terceiros que não são de propriedade ou controlados pelo Desenvolvedor. Não temos controle sobre, e não assumimos responsabilidade pelo conteúdo, políticas de privacidade ou práticas de quaisquer sites ou serviços de terceiros.
              </p>
            </section>

            <section>
              <h2 className="text-xl font-semibold text-legal-heading mb-4">
                10. Alterações nos Termos de Uso
              </h2>
              <p className="text-legal-text">
                Reservamos o direito de modificar ou substituir estes Termos a qualquer momento. Se uma revisão for material, faremos esforços razoáveis para fornecer um aviso com pelo menos 30 (trinta) dias de antecedência antes que quaisquer novos termos entrem em vigor.
              </p>
            </section>

            <section className="bg-legal-section p-6 rounded-lg">
              <h2 className="text-xl font-semibold text-legal-heading mb-4">
                11. Lei Aplicável e Foro
              </h2>
              <p className="text-legal-text">
                Estes Termos serão regidos e interpretados de acordo com as leis da República Federativa do Brasil, em particular a Lei Geral de Proteção de Dados (Lei nº 13.709/2018) e o Código de Defesa do Consumidor (Lei nº 8.078/1990). Qualquer disputa ou controvérsia será submetida ao foro da comarca de Belo Horizonte, Estado de Minas Gerais, Brasil.
              </p>
            </section>

            <section>
              <h2 className="text-xl font-semibold text-legal-heading mb-4">
                12. Disposições Gerais
              </h2>
              <ul className="space-y-2 text-legal-text">
                <li><strong>Independência das Cláusulas:</strong> Se qualquer disposição destes Termos for considerada inválida ou inexequível, as demais disposições permanecerão em pleno vigor e efeito.</li>
                <li><strong>Renúncia:</strong> Nenhuma renúncia de qualquer termo ou condição estabelecida nestes Termos será considerada uma renúncia adicional ou contínua.</li>
              </ul>
            </section>
          </div>

          {/* Contact Footer */}
          <div className="mt-8 pt-6 border-t">
            <div className="flex items-center justify-center gap-2 text-muted-foreground">
              <Mail className="h-4 w-4" />
              <span>Dúvidas sobre os termos? Entre em contato:</span>
              <a 
                href="mailto:mediacutsstudio@gmail.com" 
                className="text-primary hover:underline font-medium"
              >
                mediacutsstudio@gmail.com
              </a>
            </div>
          </div>
        </Card>
      </main>
    </div>
  );
};

export default TermsOfService;