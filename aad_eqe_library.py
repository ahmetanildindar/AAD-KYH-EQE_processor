# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 11:39:26 2016

@author: adindar
"""
#%%
from datetime import datetime
import urllib2

#%%
# İstasyon verisi okuma fonksiyonu yaratalım. 
istasyon_url = 'http://kyhdata.deprem.gov.tr//2K/genAcc.php?dst=TU9EVUxFX05BTUU9ZXZ0RmlsZSZNT0RVTEVfVEFTSz1zaG93Jk1PRFVMRV9TVUJUQVNLPUFMTCZNT0RVTEVfVEFSR0VUPW9sZCZUQVJHRVQ9MjAxNjA4MDIxOTMwNTJfMTgwNCZUQVJHRVRfU0VSSUFMPTIyMTI5'
#%%
#def kyh_verisi_okuma(istasyon_url):
kyh_istasyon_homepage_content = urllib2.urlopen( istasyon_url )
kyh_istasyon_html = kyh_istasyon_homepage_content.read()
#%%
baslangic = kyh_istasyon_html.find('a href="') 
bitis = kyh_istasyon_html.find('"><img src=') 
#%%
# Indirilecek dosyanin Url'sinin belirlenmesi
data_url = 'http://kyhdata.deprem.gov.tr/' + kyh_istasyon_html[baslangic+8:bitis-1]
# Dosyayı indirelim

mget(data_url)

# Dosyanin iceriginin okunmasi
kyh_istasyon_data_content = urllib2.urlopen( data_url )
kyh_istasyon_data = kyh_istasyon_data_content.read()
#%%
print('\n'+ datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '| Dosya okundu')

eqe_data_satir = ''
eqe_data_satir = kyh_istasyon_data.split('\n')
eqe_x = [0]
eqe_data_satir
counter = 1
for i in eqe_data_satir:
    if counter > 19: #and counter  < 30:
        satir = i.split(' ')
        #print len(satir)
        counter_satir = 1 
        for j in satir:
            if len(j) > 1:
                eqe_x.append(float(j))
    counter = counter + 1
#print eqe_x
time = range(len(eqe_x))