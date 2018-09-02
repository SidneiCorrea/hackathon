import time
import datetime
import cv2
import wave
import os

from base64 import b64encode, b64decode

from microfone.models \
    import VozUsuario
from camera.models \
    import ImagemUsuario
from libs.gravador_audio.gravador \
    import Recorder
from django.shortcuts \
    import render
from camera.views \
    import GravadorFotoCreateView
from microfone.views \
    import GravadorAudioCreateView
from security.settings \
    import MEDIA_ROOT
from watson_developer_cloud \
    import VisualRecognitionV3, SpeechToTextV1, WatsonApiException

class Imagem:

    def __init__(self):
        super(Imagem, self).__init__()

    def save_imagem():
        #ACESSA API DE RECONHECIMENTO FACIAL
        visualrecognition = VisualRecognitionV3(
            version='2018-03-19',
            iam_apikey='hAYJfnWPUHGIgdUlVxt0cjDal_gcOr647Y7grO9CLjlp',
            iam_api_key='hAYJfnWPUHGIgdUlVxt0cjDal_gcOr647Y7grO9CLjlp',
        )

        #SALVA IMAGEM
        camera = cv2.VideoCapture(0)

        ramp_frames = 30

        retval, img = camera.read()

        for i in range(ramp_frames):
            temp = img

        camera_capture = img

        url_imagem = MEDIA_ROOT + "/usuario" + str(datetime.datetime.now()) + ".jpg"

        cv2.imwrite(
            url_imagem, 
            camera_capture
        )

        try:
            recognized_imagem = visualrecognition.detect_faces(
                images_file = open(url_imagem, 'rb').read()
            )
            print(recognized_imagem)

            ImagemUsuario.objects.cria_imagem(
                imagemusuario_padrao = url_imagem
            )

            cv2.waitKey(0)
            camera.release()
            cv2.destroyAllWindows()

            return {
                'url_imagem':url_imagem,
                'recognized_imagem':recognized_imagem
            }

        except WatsonApiException as ex:
            cv2.waitKey(0)
            camera.release()
            cv2.destroyAllWindows()

            print("Código de erro " + str(ex.code) + ": " + ex.message)

class Audio:

    rec = Recorder()

    def __init__(self):
        super(Audio, self).__init__()

    def create_audio():

        Audio.rec.start()

    def save_audio():
        #ACESSA API DE RECONHECIMENTO DE AUDIO
        speechtotext = SpeechToTextV1(
            username='275e5bb5-07ca-4599-a9ef-5e89b1222301', 
            password='JFKcvHTpUCG3'
        ) 
    
        #SALVANDO AUDIO
        Audio.rec.stop()

        url_voz = MEDIA_ROOT + "/usuario" + str(datetime.datetime.now()) + ".wav"

        Audio.rec.save(
            url_voz
        )

        vetor_audio = open(url_voz, 'rb').read() 

        try:
            recognized_audio = speechtotext.recognize(
                audio=vetor_audio,
                content_type='audio/wav',
                model='pt-BR_BroadbandModel',
                interim_results=False,
                keywords=['conta', 'cooperativa', 'valor', 'transferir'],
                keywords_threshold=0.3,
                max_alternatives=3
            )

            print(recognized_audio)

            VozUsuario.objects.cria_voz(
                vozusuario_padrao = url_voz
            )
    
            return {
                'url_voz':url_voz,
                'recognized_audio':recognized_audio
            }

        except WatsonApiException as ex:
            Audio.rec.delete(
                url_voz
            )
            print("Código de erro " + str(ex.code) + ": " + ex.message)


        

class UsuarioCreateView(GravadorAudioCreateView, 
                        GravadorFotoCreateView,
                        Audio, Imagem):

    template_name = "frontend/faceadd.html"

    def __init__(self):
        super(UsuarioCreateView, self)\
            .__init__()

    def get_ajax(request):

        UsuarioCreateView.create_audio()

        return request

    def set_ajax(request):
        imagem = UsuarioCreateView.save_imagem()
        audio = UsuarioCreateView.save_audio()

        return render(
            request, 
            'frontend/audio.html', 
            {
                'imagem': imagem,
                'audio': audio['recognized_audio'],
            }
        )

class AntifraudeValidadorCreateView(UsuarioCreateView):

    template_name = "frontend/webcam.html"
