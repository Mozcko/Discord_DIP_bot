rules ={
    1:"no pelien 🤝",
}

comms = {
    "misceláneos": "help \ninvite \nsugerencias",
    "música": "join \nplay \npause \nleave \nresume",
    "moderación": "ban \nunban \nkick \nmute \nunmute \nclear"
}

# esto se puede convertir en un json
exp_comms = {
    "help": {
        "permission": None,
        "description": "el comando de ayuda",
        "usage": "!help {comando (opcional)}",
        "Special": None
        },
    "invite": {
        "permission": None,
        "description": "crea un link de invitación temporal",
        "usage": "!invite",
        "Special": None
        },
    "sugerencias": {
        "permission": None,
        "description": "muestra el link al buzón de quejas",
        "usage": "!sugerencias",
        "Special": None
        },
    "join": {
        "permission": None,
        "description": "hace que el bot se conecte a un canal de voz",
        "usage": "!join",
        "Special": None
        },
    "play": {
        "permission": None,
        "description": "reproduce música desde el canal de voz",
        "usage": "!play {URL de la canción}",
        "Special": None
        },
    "pause": {
        "permission": None,
        "description": "pausa la canción que este reproduciendo en el momento",
        "usage": "!pause",
        "Special": None
        },
    "leave": {
        "permission": None,
        "description": "deja el canal de voz",
        "usage": "!leave",
        "Special": None
        },
    "resume": {
        "permission": None,
        "description": "reanuda la canción que este pausada",
        "usage": "!resume",
        "Special": None
        },
    "ban": {
        "permission": "Ban Members",
        "description": "bannea a un miembro",
        "usage": "!ban {@miembro}",
        "Special": None
        },
    "unban": {
        "permission": "Ban Members",
        "description": "des bannea a un miembro",
        "usage": "!unban {nombre#id}",
        "Special": None
        },
    "kick": {
        "permission": "Kick Members",
        "description": "kickea a un miembro",
        "usage": "!kick {@miembro}",
        "Special": None
        },
    "mute": {
        "permission": "Manage Messages, Manage Roles",
        "description": "mutea a un miembro",
        "usage": "!mute {@miembro}",
        "Special": None
        },
    "unmute": {
        "permission": "Manage Messages, Manage Roles",
        "description": "des mutea a un miembro",
        "usage": "!unmute {@miembro}",
        "Special": None
        },
    "clear": {
        "permission": "Manage Messages",
        "description": "limpia los mensajes del canal de texto (por defecto 30)",
        "usage": "!clear {cantidad de mensajes (opcional)}",
        "Special": None
        },
}