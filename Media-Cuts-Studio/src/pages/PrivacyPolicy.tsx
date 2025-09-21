import { Link } from "react-router-dom";
import { ArrowLeft, Shield, Mail, Calendar } from "lucide-react";
import { Button } from "@/components/ui/button";
import { Card } from "@/components/ui/card";

const PrivacyPolicy = () => {
  return (
    <div className="min-h-screen bg-gradient-to-br from-background to-legal-section">
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
                <Shield className="h-6 w-6 text-primary" />
                <h1 className="text-xl font-semibold">Media Cuts Studio</h1>
              </div>
            </div>
            <Link to="/terms-of-use">
              <Button variant="outline" size="sm">
                Termos de Serviço
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
              Política de Privacidade
            </h1>
            <div className="flex items-center justify-center gap-2 text-muted-foreground">
              <Calendar className="h-4 w-4" />
              <span>Data de Vigência: 01 de agosto de 2025</span>
            </div>
          </div>

          <div className="prose prose-lg max-w-none space-y-6">
            <p className="text-legal-text leading-relaxed">
              Bem-vindo ao Media Cuts Studio. Esta Política de Privacidade descreve como o Media Cuts Studio ("nós", "nosso", ou "o Desenvolvedor") coleta, usa, compartilha e protege as informações pessoais dos usuários ("você" ou "Usuário") que participam do nosso programa de software em fase beta. Ao acessar, baixar, instalar ou utilizar o software beta do Media Cuts Studio, você concorda com os termos desta Política de Privacidade.
            </p>

            <section className="bg-legal-section p-6 rounded-lg">
              <h2 className="text-xl font-semibold text-legal-heading mb-4">
                1. Identificação do Controlador de Dados
              </h2>
              <p className="text-legal-text mb-4">
                O controlador de dados responsável pelo tratamento dos seus dados pessoais é:
              </p>
              <div className="bg-background p-4 rounded border">
                <p className="font-medium">Ualerson Rodrigues de Freitas e Media Cuts Studio</p>
                <p>CNPJ: Ainda Não temos</p>
                <p>Endereço Completo: Ainda Não temos</p>
                <div className="flex items-center gap-2 mt-2">
                  <Mail className="h-4 w-4 text-primary" />
                  <p>E-mail para contato com o Encarregado de Dados (DPO): <a href="mailto:mediacutsstudio@gmail.com" className="text-primary hover:underline">mediacutsstudio@gmail.com</a></p>
                </div>
              </div>
            </section>

            <section>
              <h2 className="text-xl font-semibold text-legal-heading mb-4">
                2. Dados Pessoais Coletados e Finalidades do Tratamento
              </h2>
              <p className="text-legal-text mb-4">
                Coletamos os seguintes tipos de dados pessoais para as finalidades descritas abaixo:
              </p>
              
              <div className="space-y-4">
                <div className="bg-legal-section p-4 rounded">
                  <h3 className="font-semibold text-legal-heading">Dados de Registro:</h3>
                  <p className="text-legal-text">Informações fornecidas diretamente por você durante o cadastro, como nome, endereço de e-mail e informações de contato.</p>
                  <p className="text-sm text-primary font-medium mt-2">Finalidade: Gerenciamento da sua conta, comunicação sobre o programa beta e atualizações.</p>
                </div>

                <div className="bg-legal-section p-4 rounded">
                  <h3 className="font-semibold text-legal-heading">Dados de Uso e Navegação:</h3>
                  <p className="text-legal-text">Endereço IP, localização geográfica (país), tempo de navegação e acesso, recursos utilizados e interações com o software.</p>
                  <p className="text-sm text-primary font-medium mt-2">Finalidade: Análise de desempenho, identificação de padrões de uso e aprimoramento da experiência do usuário.</p>
                </div>

                <div className="bg-legal-section p-4 rounded">
                  <h3 className="font-semibold text-legal-heading">Dados Técnicos e de Desempenho (Específicos da Versão Beta):</h3>
                  <p className="text-legal-text">Logs de falha (crash logs), dados de desempenho do aplicativo, informações sobre o dispositivo (identificadores únicos, especificações de hardware/SO), estatísticas de uso e informações de rede.</p>
                  <p className="text-sm text-primary font-medium mt-2">Finalidade: Identificação e correção de bugs e falhas, análise de desempenho, aprimoramento e desenvolvimento contínuo do software beta. Para os fins do programa beta, a coleta desses dados é essencial e, geralmente, não pode ser desativada, pois é crucial para o nosso objetivo de identificar e resolver problemas.</p>
                </div>

                <div className="bg-legal-section p-4 rounded">
                  <h3 className="font-semibold text-legal-heading">Dados de Feedback:</h3>
                  <p className="text-legal-text">Comentários, sugestões, relatórios de bugs, capturas de tela e outras informações que você nos fornece para ajudar a aprimorar o software.</p>
                  <p className="text-sm text-primary font-medium mt-2">Finalidade: Aprimoramento do software e desenvolvimento de novas funcionalidades.</p>
                </div>

                <div className="bg-legal-section p-4 rounded">
                  <h3 className="font-semibold text-legal-heading">Cookies e Tecnologias de Rastreamento:</h3>
                  <p className="text-legal-text">Utilizamos cookies e tecnologias de rastreamento para coletar informações sobre o uso do nosso site e aplicativo.</p>
                  <p className="text-sm text-primary font-medium mt-2">Finalidade: Personalização da sua experiência, análise de tendências e administração do software.</p>
                </div>
              </div>
            </section>

            <section>
              <h2 className="text-xl font-semibold text-legal-heading mb-4">
                3. Base Legal para o Tratamento de Dados (LGPD)
              </h2>
              <p className="text-legal-text mb-4">
                O tratamento dos seus dados pessoais é realizado com base nas seguintes justificativas legais, conforme a LGPD:
              </p>
              <ul className="space-y-2 text-legal-text">
                <li><strong>Consentimento do Titular:</strong> Para finalidades que não são estritamente essenciais para a sua participação no programa beta, como o envio de comunicações de marketing (que exigirão seu consentimento explícito e separado).</li>
                <li><strong>Execução de Contrato ou Procedimentos Preliminares:</strong> Para a coleta de dados indispensáveis ao acesso e utilização das funcionalidades do software beta, considerando que sua participação no programa beta é um contrato de serviço implícito.</li>
                <li><strong>Legítimo Interesse do Controlador:</strong> Para o tratamento de dados necessários ao aprimoramento, segurança e operação do software beta, como a coleta de logs de falha e dados de uso (anonimizados quando possível) para análises de desempenho e identificação de bugs.</li>
                <li><strong>Cumprimento de Obrigação Legal ou Regulatória:</strong> Se houver qualquer exigência legal específica para o tratamento de determinados dados.</li>
              </ul>
            </section>

            <section>
              <h2 className="text-xl font-semibold text-legal-heading mb-4">
                4. Compartilhamento de Dados com Terceiros e Transferências Internacionais
              </h2>
              <p className="text-legal-text mb-4">
                Podemos compartilhar seus dados pessoais com terceiros apenas quando estritamente necessário para as finalidades descritas nesta política. Isso pode incluir:
              </p>
              <ul className="space-y-2 text-legal-text mb-4">
                <li><strong>Provedores de Serviços:</strong> Empresas que nos auxiliam na operação do software, como plataformas de hospedagem em nuvem, ferramentas de análise de dados (ex: para processamento de vídeos no "Modo Curadoria Pro (IA)") e serviços de comunicação.</li>
                <li><strong>Parceiros de Teste:</strong> Em alguns casos, dados podem ser compartilhados com parceiros envolvidos no programa beta para fins de teste e aprimoramento.</li>
              </ul>
              <p className="text-legal-text">
                Exigimos que todos os terceiros com os quais compartilhamos dados pessoais garantam a proteção e o tratamento adequado dessas informações, em conformidade com a LGPD.
              </p>
            </section>

            <section className="bg-primary/5 p-6 rounded-lg">
              <h2 className="text-xl font-semibold text-legal-heading mb-4">
                5. Direitos dos Titulares de Dados
              </h2>
              <p className="text-legal-text mb-4">
                De acordo com a LGPD, você possui os seguintes direitos em relação aos seus dados pessoais:
              </p>
              <ul className="grid grid-cols-1 md:grid-cols-2 gap-2 text-sm text-legal-text">
                <li>• Confirmação da Existência de Tratamento</li>
                <li>• Acesso aos Dados</li>
                <li>• Correção de Dados Incompletos</li>
                <li>• Anonimização, Bloqueio ou Eliminação</li>
                <li>• Portabilidade dos Dados</li>
                <li>• Eliminação dos Dados Pessoais</li>
                <li>• Informação sobre Compartilhamento</li>
                <li>• Revogação do Consentimento</li>
              </ul>
              <div className="mt-4 p-4 bg-background rounded border">
                <p className="text-legal-text">
                  Para exercer qualquer um desses direitos, entre em contato conosco através do e-mail{" "}
                  <a href="mailto:mediacutsstudio@gmail.com" className="text-primary hover:underline font-medium">
                    mediacutsstudio@gmail.com
                  </a>{" "}
                  com assunto "Privacidade".
                </p>
              </div>
            </section>

            <section>
              <h2 className="text-xl font-semibold text-legal-heading mb-4">
                6. Medidas de Segurança e Proteção de Dados
              </h2>
              <p className="text-legal-text">
                Implementamos medidas técnicas e organizacionais adequadas para proteger seus dados pessoais contra acesso não autorizado, destruição acidental ou ilícita, perda, alteração, comunicação ou qualquer forma de tratamento inadequado ou ilícito. Nossas medidas incluem, mas não se limitam a: criptografia de dados, controles de acesso rigorosos, uso de firewalls e políticas internas para o manuseio de dados.
              </p>
            </section>

            <section>
              <h2 className="text-xl font-semibold text-legal-heading mb-4">
                7. Coleta de Feedback e Dados de Uso do Beta
              </h2>
              <p className="text-legal-text">
                Para os propósitos do programa beta, o Media Cuts Studio coleta automaticamente logs de falha, estatísticas de uso, dados de desempenho e feedback direto do software. É fundamental que você compreenda que, para a sua participação no programa beta, geralmente não é possível optar por não participar dessa coleta de dados, uma vez que ela é essencial para o propósito de teste, identificação de bugs e aprimoramento do software.
              </p>
            </section>

            <section>
              <h2 className="text-xl font-semibold text-legal-heading mb-4">
                8. Alterações na Política de Privacidade e Notificação aos Usuários
              </h2>
              <p className="text-legal-text">
                Reservamos o direito de modificar esta Política de Privacidade a qualquer momento, especialmente para adaptá-la a novas funcionalidades, requisitos legais ou mudanças em nossas práticas de gerenciamento de dados. Quando fizermos alterações significativas, você será notificado por meio de e-mail, notificação dentro do aplicativo ou aviso proeminente em nosso site.
              </p>
            </section>
          </div>

          {/* Contact Footer */}
          <div className="mt-8 pt-6 border-t">
            <div className="flex items-center justify-center gap-2 text-muted-foreground">
              <Mail className="h-4 w-4" />
              <span>Dúvidas? Entre em contato:</span>
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

export default PrivacyPolicy;