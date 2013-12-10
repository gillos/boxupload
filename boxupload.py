 from requests import *
 import json
 from settings import *
  #http://www.bittorrent.com/sync/developers/api
 #f; name of file @localdisk
 #fname; name of file @box
 def splitfile(f):
 	chapters=0
 	with open(f,'rb') as src:
 		while True:
 			w=open(f+'.%03d' % chapters, 'w')
 			w.close()
 			chapters+=1
 	return None

 def getfolder(fldr_name):
 	r=s.get('https://api.box.com/2.0/folders/0/items')
 	j=[x['entries']['id'] for x in json.loads(r.text) if x['entries']['type']=='folder' and x['entries']['name']=='fldr_name']
 	return j[0]
 		
 s=Session()
 s.headers.update({"Authorization":"Bearer %s" % box_token})
 r=s.post('https://upload.box.com/api/2.0/files/content',params={'parent_id':getfolder(fldr_name)},files={'file':(fname,open(f,'rb'))}) 