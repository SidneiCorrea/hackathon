from .forms \
	import FormCreateFoto
from django.shortcuts \
	import render
from libs.multi_form_view.base \
    import MultiModelFormCreateView

class GravadorFotoCreateView(MultiModelFormCreateView):

	def __init__(self):
		super(GravadorFotoCreateView, self)\
			.__init__()
