from fbchat import log, Client, Message
from basededatos import myneo4j
from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from os.path import join, dirname
correo = "ups_uclqlhf_chatt@tfbnw.net"
contra = "***123456789"
neo = myneo4j()

authenticatorV = IAMAuthenticator('rQkJz0iTpTyboZqk6SymQ2hh6zfG7sfmxdZBD9V9qQIV')
service = TextToSpeechV1(authenticator=authenticatorV)
service.set_service_url('https://stream.watsonplatform.net/text-to-speech/api')


def voz(text, service):
    with open(join(dirname(__file__), 'output.mp3'),
              'wb') as audio_file:
        response = service.synthesize(
            text, accept='audio/mp3',
            voice="es-LA_SofiaV3Voice").get_result()
        audio_file.write(response.content)


class EchoBot(Client):
    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        self.markAsDelivered(thread_id, message_object.uid)
        self.markAsRead(thread_id)

        if author_id != self.uid:
            messenger = message_object.text
            print(messenger)
            if messenger.upper() == 'GRAFO' or messenger.upper() == 'VER GRAFO':
                self.sendLocalImage('graph.png', Message(text="Este es el grafo"), thread_id=thread_id, thread_type=thread_type)
                rest = neo.MyBase()
                self.send(Message(text=rest), thread_id=thread_id, thread_type=thread_type)
            try:
                # Cuales son los hoteles DE *Cuenca*
                exi = messenger.upper().index("COMO LLEGO")
                if exi > -1:
                    lugares = messenger.split("*")
                    l1 = lugares[1]
                    l2 = lugares[3]
                    print(l1 + "<<<>> " + l2)
                    rest, txtAudio = neo.ComollegoDA(l1,l2)
                    self.send(Message(text="El camino es:....."), thread_id=thread_id, thread_type=thread_type)
                    self.send(Message(text=str(rest)), thread_id=thread_id, thread_type=thread_type)
                    voz(txtAudio,service)
                    self.sendLocalVoiceClips('output.mp3', thread_id=thread_id, thread_type=thread_type)


            except:
                try:
                    exi = messenger.upper().index("COMO VOY")
                    if exi > -1:
                        lugares = messenger.split("*")
                        l1 = lugares[1]
                        rest, txtAudio = neo.ComollegoA(l1)
                        self.send(Message(text="Asi puede llegar a: *" + l1 + "*"), thread_id=thread_id,
                                  thread_type=thread_type)
                        self.send(Message(text=str(rest)), thread_id=thread_id, thread_type=thread_type)
                        voz(txtAudio, service)
                        self.sendLocalVoiceClips('output.mp3', thread_id=thread_id, thread_type=thread_type)
                except:
                    try:
                        exi = messenger.upper().index("HOTELES")
                        if exi > -1:
                            ciudad = messenger.split("*")
                            l1 = ciudad[1]
                            rest = neo.hoteles(l1)
                            self.send(Message(text="Los Hoteles de *" + l1 + "* son:"), thread_id=thread_id,
                                      thread_type=thread_type)
                            self.send(Message(text=rest), thread_id=thread_id, thread_type=thread_type)
                    except:
                        try:
                            exi = messenger.upper().index("UBICACION")
                            if exi > -1:
                                ciudad = messenger.split("*")
                                l1 = ciudad[1]
                                rest = neo.ubicacion(l1)
                                self.send(Message(text="Para llegar a: *" + l1 + "* ingresa al siguiente link"), thread_id=thread_id,
                                          thread_type=thread_type)
                                self.send(Message(text=rest), thread_id=thread_id, thread_type=thread_type)
                        except:
                            self.send(Message(text="******"), thread_id=thread_id, thread_type=thread_type)
                            print("aca")






if __name__ == '__main__':
    client = EchoBot(correo, contra)
    client.listen()
    #res = neo.ComollegoDA('Cuenca','Quito')
