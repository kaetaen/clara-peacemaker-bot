import telebot
import env
from positive_vibes_api import PositiveVibesAPI as Media

bot = telebot.TeleBot(env.TOKEN)
bot.remove_webhook()

@bot.message_handler(commands=['start', 'sobre'])
def welcome(msg):
    bot.send_message(msg.chat.id, 'Olá  sou a Clara, posso te ajudar nos momentos de crise de ansiedade.  \nPara saber mais sobre o conteúdo disponibilizado acesse: positive-vibes-api.herokuapp.com/')


@bot.message_handler(commands=['respire'])
def breathe(msg):
    bot.send_document(msg.chat.id, 'https://media.giphy.com/media/1xVc4s9oZrDhO9BOYt/source.gif')


@bot.message_handler(commands=['reflita'])
def think(msg):
    episode = Media().get_podcast()
    bot.send_document(msg.chat.id, episode["url"], caption=episode["title"])
    

@bot.message_handler(commands=['escute'])
def listen(msg):
    music = Media().get_music()
    msg_title = f'🎵 Canção: {music["song_name"]} \n👨 Artista: {music["artist_name"]}'
    bot.send_document(msg.chat.id, music["file"], caption=msg_title)


@bot.message_handler(commands=['contemple'])
def enjoy(msg):
    image = Media().get_image()
    quote = Media().get_quote()
    bot.send_photo(msg.chat.id, image, caption=quote)


@bot.message_handler(commands=['converse'])
def talk(msg):
    content = """
As vezes buscar a paz por meio da arte não é o suficiente...
As vezes precisamos mesmo conversar com alguém.
As vezes precisamos de alguém para nos ouvir.

Não tenha medo.
Não tenha vergonha.
Não hesite.


📌 CVV

O Centro de Valorização da Vida realiza apoio emocional e prevenção do suicídio

📞 Telefone: 188
📧 Via email: https://www.cvv.org.br/e-mail/
💬 Chat online: https://www.cvv.org.br/chat/


📌 CRAS

O CRAS é um local público onde são oferecidos os serviços de Assistência Social.
Se você se encontra em situação vulnerável, é um direito seu!

🔗 Conheça: https://www.gov.br/pt-br/servicos/acessar-o-cras-centro-de-referencia-da-assistencia-social
📍 Encontre: https://aplicacoes.mds.gov.br/sagi/mops/serv-cras.php?


📌 CAPS

Os Centros de Atenção Psicossocial (CAPS) são pontos de serviços de saúde de caráter aberto e comunitário constituído por equipe multiprofissional e que atua sobre a ótica interdisciplinar e realiza prioritariamente atendimento às pessoas com sofrimento ou transtorno mental, incluindo aquelas com necessidades decorrentes do uso de álcool e outras drogas.

🔗 Conheça: https://www.gov.br/saude/pt-br/acesso-a-informacao/acoes-e-programas/centro-de-atencao-psicossocial-caps
📍 Encontre: https://sage.saude.gov.br/paineis/planoCrack/lista_caps.php?output=html&
"""
    bot.send_message(msg.chat.id, content, disable_web_page_preview=True)

if __name__ == '__main__':
    bot.polling()

