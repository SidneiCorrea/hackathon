from .forms \
	import FormCreateAudio
from django.shortcuts \
	import render
from libs.multi_form_view.base \
    import MultiModelFormCreateView

class GravadorAudioCreateView(MultiModelFormCreateView):

	def __init__(self):
		super(GravadorAudioCreateView, self)\
			.__init__()
		