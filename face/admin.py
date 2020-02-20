from django.contrib import admin
from .models import Opencv
from django.utils.html import mark_safe
from django.conf import settings
import cv2
from pathlib import Path

# Register your models here.
class OpencvAdmin(admin.ModelAdmin):
	
	readonly_fields = ['headshot_image']

	def headshot_image(self, obj):
		return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
			url = obj.file_output.url,
			width=700,
			height='auto',
			)
	)

	def save_model(self,request,obj,form,change):
		path = settings.BASE_DIR + '/media/' + str(obj.file_input)
		print(path)
		string = str(obj.file_input)
		print(obj.file_input)
		condition = settings.BASE_DIR + '/media/'
		new = path.split('.')[0]
		# name = string.split('/')
		# print(name)
		# print(new)
		print(new + '_output.' + path.split('.')[1])
		path2 = settings.BASE_DIR + '/face/haarcascade_frontalface_default.xml'
		print(path2)

		if Path(path).is_file(): 
			face_cascade = cv2.CascadeClassifier(path2)
			img = cv2.imread(path)
			gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
			faces = face_cascade.detectMultiScale(gray, 1.1, 4)
			for (x, y, w, h) in faces:
				cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
			cv2.imwrite(new + '_output.' + path.split('.')[1], img)
			x = string.split('.')[0]  + '_output.' + path.split('.')[1]
			name = (x.split('/')[1])

			obj.file_output = 'images/' + str(name)
		super(OpencvAdmin,self).save_model(request,obj,form,change)


admin.site.register(Opencv,OpencvAdmin)