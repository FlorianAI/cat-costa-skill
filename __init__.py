from mycroft import MycroftSkill, intent_file_handler


class CatCosta(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('costa.cat.intent')
    def handle_costa_cat(self, message):
        produsul = message.data.get('produsul')

        self.speak_dialog('costa.cat', data={
            'produsul': produsul
        })


def create_skill():
    return CatCosta()

