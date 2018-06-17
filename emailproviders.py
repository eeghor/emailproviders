from bs4 import BeautifulSoup
import requests
import os
from collections import defaultdict
import re
from unidecode import unidecode
import json

class EmailProviders:

	def __init__(self):

		# create a data directory if it doesn't exits

		if not os.path.exists('data'):
			os.mkdir('data')

		self.eps = []

	def get_from_mashable(self):
		"""
		source: https://mashable.com/2007/09/05/email-toolbox/#7VffFoZiaGqg
		"""
		BASE_URL = 'https://mashable.com/2007/09/05/email-toolbox/#7VffFoZiaGqg'

		soup = BeautifulSoup(requests.get(BASE_URL).text, 'lxml')

		for _ in soup.find('h2', text='Email Services').next_siblings:

			if _.name:
				if _.name == 'p':
					print(_.find('a')['href'])

	def get_mailcom(self):

		soup = BeautifulSoup(requests.get('https://www.mail.com/email/#.2068504-stage-simplebody1-1').text, 'lxml')

		for _ in soup.find_all('div', class_='domainlists'):
			for a in _.find_all('a'):
				print(a.text.strip())

if __name__ == '__main__':

	ep = EmailProviders().get_mailcom()