def register(_bot):
    global bot
    bot = _bot
    with open('admins.info') as file:
        nonlocal admins
        admins = file.readlines()
    bot.admins.extend(admins)
    bot.register_trigger('!ping', ping)
    bot.register_trigger('!shutdown', shutdown)
    bot.register_flow_triggers('!pause', '!resume')

          
async def ping(client, message):
    tag = get_tag(message)
    if tag in bot.admins:
        await client.send_message(message.channel, 'Pong!')
    
async def shutdown(client, message):
    tag = get_tag(message)
    if tag in bot.admins:
        bot.debug('Shutdown called by {}. Shutting down.'.format(tag))
        await client.send_message(message.channel, 'Bye bye!')
        import sys
        sys.stderr.close()
        await client.close()
        sys.exit(0)
        
def get_tag(message):
    tag = '{}#{}'.format(message.author.name, message.author.discriminator)
    return tag