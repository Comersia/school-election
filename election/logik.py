from django.core.files import File
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
import random
import csv


def generate_password(length=8):
	chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
	password = ''
	for i in range(length):
		password += random.choice(chars)
	return password

def register_file(file):
	form = file.name[:-4]
	csvfile = open('temp.csv', 'w', newline='')
	writer = csv.writer(csvfile, delimiter=',')
	for line in file:
		name = str(line.decode('utf-8')).strip()
		name += '_' + generate_password(length=3)
		password = generate_password()
		user = User(username=name)
		user.set_password(password)
		user.save()
		user.profile.form = form
		user.save()
		writer.writerow([name, password])
	csvfile.close()
	with open('temp.csv', 'r') as csvfile:
		file_to_save = File(csvfile)
		fs = FileSystemStorage()
		filename = fs.save(file.name, file_to_save)
		uploaded_file_url = fs.url(filename)
	return uploaded_file_url	
