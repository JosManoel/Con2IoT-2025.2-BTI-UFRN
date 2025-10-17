<h1 align = "center">
    Atividade Avaliativa II - Tecnologias de Comunicação para IoT
</h1>

**Aluno:** José Manoel Freitas da Silva

<p align ="center">
<a href= "#sobre-este-projeto">🕹️ Sobre este projeto</a> &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
<a href="#licenca">📝 Licença</a>
</p>

<hr>

<h2 id = "sobre-este-projeto">🕹️ Sobre este projeto</h2>

Esse projeto consiste na implementação do bot de mensagens [Eliza](https://pt.wikipedia.org/wiki/ELIZA), considerado o primeiro software de simulação de conversa, para o uso em mensagens via [XMPP](https://pt.wikipedia.org/wiki/Extensible_Messaging_and_Presence_Protocol). Para essa implementação, utilizamos uma versão reduzida do bot escrita em python e disponibilizada como uma lib pelo usuário [Jez Higgins](https://github.com/jezhiggins), acessível no seu [repositório](https://github.com/jezhiggins/eliza.py) do GitHub.

### Utilização

#### Instalando as dependencias

Para a utilização desse projeto, certifique-se de antes instalar o servidor Eajabberd, que será responsável por gerenciar as mensagens enviadas pelo usuário.

Infelizmente, existem alguns problemas com a instalação do Eajabberd com alguns gerenciadores de pacotes, como o dnf do Fedora, sendo recomendado o uso dos packages disponíveis no repositório oficial do [projeto](https://github.com/processone/ejabberd/releases).

Exemplo:

```bash
sudo dnf install ejabberd-25.08-1.x86_64.rpm
```

Além disso, também será necessário instalar o [Pidgin](https://pidgin.im/install/) ou outro cliente de mensagens XMPP a sua escolha.

#### Configurando o servidor Ejabberd

Após a instalação do Ejabberd, edite o arquivo **_.yml_** de configuração para apontar o servidor para localhost, se estiver executando os testes em sua própria máquina. O arquivo de configuração pode ser encontrado em:

* /etc/ejabberd/ejabberd.yml
* /opt/ejabberd/conf/ejabberd.yml

Em **_hosts:_** verifique se o servidor está configurado para localhost.

Em seguida, inicie o servidor:

```bash
sudo systemctl start ejabberd
sudo systemctl enable ejabberd
```

O status pod ser visualizado comm:
```bash
sudo systemctl status ejabberd
```

#### Registrando um usuário

Para utilizar o bot, registre o usuário que o bot irá utilizar com o seguinte comando:

```bash
sudo ejabberdctl register android18 localhost 123456
```

Registre também o seu usuário que irá se comunicar com o bot. Por padrão, o bot envia as mensagens para **_kuririn@localhost_**.

```bash
sudo ejabberdctl register kuririn localhost 123456
```

#### Executando o bot

Feito todo o processo, execute o script em python **_eliza_bot.py** e inicie o seu cliente de mensagens XMPP para conversar!

```bash
python3 eliza_bot.py
```

<hr>

<h2 id="licenca">📝 Licença</h2>

- Este projeto está sob a licença [MIT](https://github.com/JosManoel/Con2IoT-2025.2-BTI-UFRN/blob/main/LICENSE).

<hr>

<div align = "center">
  
  👋🏾 Feito por [JosManoel](https://github.com/JosManoel) com 🕹️ , 🎧 e 💻.
</div> 