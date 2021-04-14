import discord
import os
import random
from keep_alive import keep_alive
from discord.ext import commands
from replit import db

client = commands.Bot(command_prefix='!', help_command=None,)

homo = ['gay', 'gai']

risadas = ["kk", "kkk", "KK", "KKK", "KS", "ks",]

resposta_risadas = ["Ta rindo fdp?", "Para de rir mlk"]

sn = ['sim', 'não']

flof = ['rato']

nomes = [
    "Adolf hitler", "Joseph Stalin", "Jair Bolsonaro", "Lula",
    "Felipe Pereira", "Patokarma", "Gabriel Henrique", "Brewl", "Artur Amaro",
    "Arquiterio", "Miguel", "Raiven", "Aquibaldo", "Jon Kleber", "Caio Kleber",
    "Kleber Kleber", "Aquibaldomóvel", "Grongos", "Murilão", "Hugão",
    "Ricardão", "Hideri", "Anando", "Liu Pigas", "Fly Emirates", "Carlos",
    "Marcelo Alves", "Tristana Ap do Brewl", "Bardo M7",
    "Shaco Psicopata do Liu Pig", "Espinela Gay", "Carolis", "Pijas",
    "Chogath Jg do Jon", "Pedra Assassina", "Nego Ney", "Neymar",
    "Cristiano Ronaldo", "Rodolfão", "Ricean", "Yooo Zaunitas", "Jacquin",
    "Felipe Dormindo", "Kami", "Jean Mago", "Major Mateus", "Faker",
    "The Rake", "Sartin", "Fluffy", "Flof", "Raul Seixas", "Vampiro Doidão", "Padre Marcelo Musculoso", "Não", "Sim", "Megamente"
]

poderes = [
    "Daltonismo", "Quebrar Códigos", "Miguelismo", "Bill Gates", "Sucesso",
    "Barriga Cósmica", "Violão", "Invisibilidade", "Destruir Códigos",
    "Wall do Yasuo (cringe)", "Fúria do Sartin", "Liu Pigas Psicopata",
    "Velocidade Veloz", "Nazismo", "Derreter e Desderreter",
    "Braço Direito Forte", "Estar em Choque", "Estar em Jooj",
    "JoJo Reference", "Gayzismo", "Super Força", "Pulo Pulado", "Pau Grosso",
    "Pau Colossal", "Artur Amaro", "Big Brain", "Preguiça de Bahiano",
    "Cagar Lava!", "*Mostra M7*", "Comer Todos", "Poder Kleber",
    "Poder Bárbaro", "0 ms", "Ser Bronze(cringe)", "Ser Prata (Deus)",
    "Comer Casadas", "RAIO DO VOLIBÉR", "Deus das Tiradas",
    "Ganhador da Batalha da Aldeia", "Aura Bárbara",
    "Vencer x1 de Akali Contra o Arthur", "Peaky Blinders",
    "Fundou a Microsoft",
    "O melhor amigo foi esmagado por uma pedra (Kléber reference)",
    "Ganhou num x1 de Akali contra Arthur", "Fez chover pão na África",
    "Atacou as Torres Gêmeas", "Foi eleito o ser mais gostoso do Universo",
    "Com um soco, impediu que um asteroide destruísse o Brasil",
    "Descobriu ser gay", "Caiu no bait da Neeko do Felipe",
    "Lutou ao lado de Coronel Pança na Guerra Das Cecília",
    "Peidou e sem querer extinguiu a vida",
    "Bateu uma no banho, caiu, bateu a cabeça e ficou desacordado com pau ereto",
    "Está treinando para ser o ser com maior pau do Universo",
    "Não é devoto a Ednaldo Pereira", "É precoce", "Devora os inimigos",
    "Joga Free Fire", "É main Yasuo", "Perdeu os pais num acidente de carro",
    "Matou milhões de pessoas", "Busca o lanche em Marte", "Comeu a sua mãe",
    "Gosta de criancinhas, hihihi", "É fanboy do Carlos",
    "Está gravido(a) de um relacionamento com o Ricean", "Ama a Jessica",
    "Gosta de censurar as pessoas", "É completamente apaixonado pelo Shrek",
    "Já foi na Disneyland", "É o(a) atual namorado(a) do Heitor."
]

origem = [
    "inferno", "Alemanha Nazista", "Cama do Felipe", "Sala da Ivone",
    "Itália Facista", "União Soviética", "Coréia do Norte", "Demacia", "Noxus",
    "Ionia", "Piltover", "Minecraft", "Freljord", "Angola",
    "França Napoleonica", "Zaun", "Banheiro do Kleber", "Cu da Mãe do Felipe",
    "Barriga do Miguel", "Mansão do Bill Gates", "Mansão do Jeff Besus",
    "Casa do Jair Bolsonaro", "Cama do Ricean", "Japão", "Hiroshima",
    "Nagasaki", "Chernobyl", "Palestina", "Acre", "Irã", "Afeganistão", "Pensamentos de Aristóteles"
]

gays_server = [
    "felipe", "patokarma", "miguel", "anando", "Felipe", "Yasuo", "yasuo"
]

resposta_gays = [
    "Nome de gay esse q vc disse!",
    "Sinto cheiro de bronze com esse nome que vc disse!",
    "Esse nome q vc disse é a  VERGONHA de kleber!"
    ""
]

egirl = [
    "UwU", "OwO", ">///<", ">:)", "( ͡° ͜ʖ ͡°)", ">:(", ":)", ":(", ":D", "•~•"
]

nunu = [
    "nunu1.jpeg", "nunu2.jpeg", "nunu3.jpeg", "nunu4.jpeg", "nunu5.jpeg",
    "nunu6.jpeg", "nunu7.jpeg", "nunu8.jpeg"
]

def update_flof(flof1):
  if "flofs" in db.keys():
    flofs = db["flofs"]
    flofs.appen(flof1)
    db["flofs"] = flofs
  else:
    db["flofs"] = [flof1]  

def delete_flof(index):
  flofs = db["flofs"]
  if len(flofs) > index:
    del flofs[index]
  db["flofs"] = flofs  

#quando conectado


@client.event
async def on_ready():
    print('Me conectei como {0.user}'.format(client))


#quando mensagem é recebida


@client.event
async def on_message(message):

    if message.author == client.user:
        return
    msg = message.content
    if message.content.startswith('!sup'):
        await message.channel.send(file=discord.File('diff.jpeg'))
    if message.content.startswith('!amogus'):
       await message.channel.send(file=discord.File('amogus1.jpeg'))
    if message.content.startswith('!felipe'):
        await message.channel.send(file=discord.File('felipe.mp4'))      
    if message.content.startswith('!sus'):
        await message.channel.send(file=discord.File('amongus.jpeg'))
    if message.content.startswith('!drip'):
        await message.channel.send(file=discord.File('drip.jpeg'))  
    if message.content.startswith('!neeko'):
        neeko = 0
        neeko = neeko + 1
        await message.channel.send('Trolado pela neeko pela {} vez!' .format(neeko))
    if message.content.startswith('!p'):
        await message.channel.send(random.choice(sn))
    if message.content.startswith('?'):
        await message.channel.send('?') 
    if message.content.startswith('!report'):
        await message.channel.send('Reportado com sucesso!')       
    if message.content.startswith('!galinha'):
        await message.channel.send('$im Chicken (HTTYD)')    
    if message.content.startswith('!dale'):
        await message.channel.send('Dale!')
    if message.content.startswith('!bomdia'):
        await message.channel.send('Bom dia!')    
    if message.content.startswith('!soumjogo'):
        await message.channel.send('MULEQUE, É SÓ UM JOGO? CALMA AÍ, LEAGUE OF LEGENDS É SÓ UM JOGO?ELE FALOU QUE LEAGUE OF LEGENDS É SÓ UM JOGO E QUE EU TENHO QUE JOGAR PRA ME DIVERTIR, MULEQUE POR ISSO QUE ELE TÁ NO BRONZE MULEQUE POR ISSO QUE ELE TÁ NO BRONZE POR ISSO QUE ELE VAI MORRER NO BRONZE, EU NÃO POSSO JOGAR COM BRONZE CARA, O CARA FALA QUE EU TENHO QUE JOGAR PRA ME DIVERTIR MULEQUE SE EU QUISESSE ME DIVERTIR EU TAVA NA PRAIA CATANDO TATU, EU TINHA BOTADO NO TV XUXA NA TELEVISÃO, EU TAVA COMENDO PUTA, FAZENDO ALGUMA COISA EU NÃO TAVA JOGANDO A MERDA DESSE JOGO, EU NÃO SERIA PLATINA, EU NÃO JOGARIA PRA CARALHO PRA porra MULEQUE PRA ME DIVERTIR, QUANDO EU JOGO EU JOGO PRA VENCER, EU NÃO JOGO PRA ME DIVERTIR, EU JÁ FALEI, MULEQUE, SE EU JOGO E O CARA FAZ AQUILO, O CARA ME MATA O CARA MANDA UM JAX ME DAR UM BEIJO, O QUE QUE TU QUER QUE EU FAÇA MULEQUE O QUE QUE TU QUER QUE FAÇA???MULEQUE SE EU TE CHAMAR PRA JOGAR, E TU FOR A merda DE UM JOGADOR CASUAL TU NÃO ACEITA A PORRA DO CONVITE, POR QUE TU VAI LEVAR RAGE TU VAI FICAR IGUAL UMA putinha TU NÃO VAI AGUENTAR O RAGE E VAI FICAR CHORANDO VAI FALAR QUE EU LEVO A PORRA DO JOGO A SÉRIO, SE EU TÔ JOGANDO O JOGO SE EU TÔ VENCENDO SE EU GOSTO DE VENCER EU LEVO A PORRA DO JOGO A SÉRIO, E NÃO VEM FALAR aAaAaAaAaA vOcE tEm QuE LeVaR o JoGo Na BrInCaDeIrA SE EU QUISESSE BRINCAR EU NÃO TAVA JOGANDO A PORRA DE LEAGUE OF LEGENDS, EU TAVA JOGANDO ADOLETA LÁ NA PUTA QUE PARIU!')
    if message.content.startswith('!soumbot'):
        await message.channel.send('MULEQUE, É SÓ UMA BOT? CALMA AÍ, LAIKA É SÓ UMA BOT?VC FALOU QUE A LAIKA É SÓ UMA BOT E QUE EU TENHO QUE USA-LA PRA ME DIVERTIR, MULEQUE POR ISSO QUE VC TÁ NO BRONZE E É POR ISSO QUE VC VAI MORRER NO BRONZE, EU NÃO POSSO FALAR COM BRONZE CARA, O CARA FALA QUE EU TENHO QUE USA-LA PRA ME DIVERTIR MULEQUE SE EU QUISESSE ME DIVERTIR EU TAVA NA PRAIA CATANDO TATU, EU TINHA BOTADO NO TV XUXA NA TELEVISÃO, EU TAVA COMENDO PUTA, FAZENDO ALGUMA COISA EU NÃO TAVA USANDO A MERDA DESSA BOT, EU NÃO SERIA PLATINA, EU NÃO USARIA ELA PRA CARALHO PRA porra MULEQUE PRA ME DIVERTIR, QUANDO EU USO ELA EU USO PRA VENCER, EU NÃO USO PRA ME DIVERTIR, EU JÁ FALEI, MULEQUE, SE EU USO E O CARA FAZ AQUILO, O QUE QUE TU QUER QUE EU FAÇA MULEQUE O QUE QUE TU QUER QUE FAÇA???MULEQUE SE EU TE CHAMAR PRA USAR, E TU FOR A merda DE UM USADOR  CASUAL TU NÃO ACEITA A PORRA DO CONVITE, POR QUE TU VAI LEVAR RAGE TU VAI FICAR IGUAL UMA putinha TU NÃO VAI AGUENTAR O RAGE E VAI FICAR CHORANDO VAI FALAR QUE EU LEVO A PORRA DO JOGO A SÉRIO, SE EU TÔ USANDO A BOT SE EU TÔ VENCENDO SE EU GOSTO DE VENCER EU LEVO A PORRA DA BOT A SÉRIO, E NÃO VEM FALAR aAaAaAaAaA vOcE tEm QuE LeVaR a BoT Na BrInCaDeIrA SE EU QUISESSE BRINCAR EU NÃO TAVA USANDO A PORRA DA LAIKA, EU TAVA USANDO A MUDAE LÁ NA PUTA QUE PARIU!')      
    if any(word in msg for word in homo):
        await message.channel.send('Cala a boca homofobico de merda')
    if any(word in msg for word in gays_server):
        await message.channel.send(random.choice(resposta_gays))
    if any(word in msg for word in risadas):
        await message.channel.send(random.choice(resposta_risadas))    
    if message.content.startswith('!ficha'):
       myEmbed = discord.Embed(title="Ficha", description="---------", color=0x00ff00)
       myEmbed.add_field(name="Personagem: {}".format(random.choice(nomes)),value="---------", inline=False)
       myEmbed.add_field(name="Lore: {}".format(random.choice(poderes)),value="---------", inline=False)
       myEmbed.add_field(name="Origem: {}".format(random.choice(origem)),value="---------", inline=False)
       await message.channel.send(embed=myEmbed)       
    if message.content.startswith('!egirl'):
        await message.channel.send(random.choice(egirl))
    if message.content.startswith('!nunu'):
        await message.channel.send(file=discord.File(random.choice(nunu)))
    if message.content.startswith('!bill'):
       myEmbed1 = discord.Embed(title="Bill Gates", description="Fundador da Micropênis", color=0x00ff00)
       myEmbed1.set_image(url='https://cdn.discordapp.com/attachments/803809170683068437/814579227105558558/bill.gif')
       await message.channel.send(embed=myEmbed1)
    if message.content.startswith('!fon'):
        await message.channel.send(file=discord.File('fon.mp4'))
    if message.content.startswith('!memesgarcia'):
        await message.channel.send(file=discord.File('garcia.jpeg'))
    if message.content.startswith('!bot'):
       myEmbed2 = discord.Embed(title="Laika Sakuranomiya", description="Melhor bot do servidor", color=0x00ff00)
       myEmbed2.set_image(url='https://cdn.discordapp.com/attachments/802615548944973924/814813692654780536/photo.jpeg') 
       await message.channel.send(embed=myEmbed2)
    if message.content.startswith('!miguel'):
       myEmbed3 = discord.Embed(title="Miguel Yuji", description="Mono yasuo carente", color=0x00ff00)
       myEmbed3.set_image(url='https://cdn.discordapp.com/attachments/605588543158485012/814854178165489724/WhatsApp_Image_2021-02-26_at_10.39.05.jpeg') 
       await message.channel.send(embed=myEmbed3)
    if message.content.startswith('!garcia'):
       myEmbed4 = discord.Embed(title="Gustavo Garcia do Nascimento", description="Piadista profissional", color=0x00ff00)
       myEmbed4.set_image(url='https://cdn.discordapp.com/attachments/605588543158485012/814855427376283658/WhatsApp_Image_2021-02-26_at_10.36.06.jpeg') 
       await message.channel.send(embed=myEmbed4)   
    if message.content.startswith('!dinho'):
       myEmbed5 = discord.Embed(title="Dinho Virtuoso", description="Um dia você tem tudo, no outro você não tem NADA", color=0x00ff00)
       myEmbed5.set_image(url='https://cdn.discordapp.com/attachments/803809170683068437/814878497813299220/6e650f5ae4b01334bdbc4cd9c61e9cae.png') 
       await message.channel.send(embed=myEmbed5) 
    if message.content.startswith('!comandos'):
        await message.channel.send('1.!garcia 2.!garciamemes 3.!miguel 4.!nunu 5.!fon 6.!dinho 7.!bot 8.!ficha 9.!egirl 10.!bill 11.!dale 12.!soumjogo 13.!major')  
    if message.content.startswith('!major'):
       myEmbed6 = discord.Embed(title="Major Mateus", description="Mono Nunu, meu pau no seu cu", color=0x00ff00)
       myEmbed6.set_image(url='https://cdn.discordapp.com/attachments/802615548944973924/815940928464355359/Screenshot_20210225-073728_YouTube.jpg') 
       await message.channel.send(embed=myEmbed6)     
    if message.content.startswith('!troll'): 
       await message.channel.send('<:troll:814105329565564959>')
    options = flof
    if "flofs" in db.keys():
      options = options + db['flofs']
    if message.content.startswith('!flof'):
        await message.channel.send(random.choice(options))
    if msg.startswith('!new'):
      flof_comando = msg.split("!new ",1)[1]
      update_flof(flof_comando)
      await message.channel.send("adiciona")    
    if message.content.startswith('!cama'): 
        await message.channel.send(file=discord.File('cama.jpeg'))   



keep_alive()
client.run(os.getenv('TOKEN'))
