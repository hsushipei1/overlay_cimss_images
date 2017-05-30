import datetime, os, shutil

startd = datetime.datetime(2017,5,1)
endd = datetime.datetime(2017,5,29)
deltad = datetime.timedelta(days=+1) 
subt = ["00", "12"] # 00Z 12Z

try:
	os.makedirs("processing_his_cimss")
	os.makedirs("overlaid")
except:
	pass

while startd <= endd:
	strd_str = startd.strftime('%Y%m%d')
	for hh in subt:
		print "Processing "+strd_str+" "+hh+"..."
		# Cropping
		os.system("convert ./Indian/"+strd_str+"/IRImageNHCEnhancement/"+strd_str+"."+hh+".Indian.IRImageNHCEnhancement.png \
					-crop 1080x666+0+0 \
					./processing_his_cimss/cropped_io_"+strd_str+"."+hh+".GIF")
		os.system("convert ./Australia/"+strd_str+"/IRImageNHCEnhancementWest/"+strd_str+"."+hh+".Australia.IRImageNHCEnhancementWest.png \
					-crop 868x680+260+0 \
					./processing_his_cimss/cropped_wau_"+strd_str+"."+hh+".GIF")
		os.system("convert ./NWPacific/"+strd_str+"/IRImageNHCEnhancement/"+strd_str+"."+hh+".NWPacific.IRImageNHCEnhancement.png \
					-crop 1080x644+0+0 \
					./processing_his_cimss/cropped_wnp_"+strd_str+"."+hh+".GIF")

		# Overlaying
		os.system("convert -size 1965x1242 xc:black ./processing_his_cimss/bk_"+strd_str+"."+hh+".png")
		os.system("convert -composite -geometry +0+277.1 ./processing_his_cimss/bk_"+strd_str+"."+hh+".png \
					./processing_his_cimss/cropped_io_"+strd_str+"."+hh+".GIF ./processing_his_cimss/out1_"+strd_str+"."+hh+".png")
		os.system("convert -composite -geometry +872+555.1 ./processing_his_cimss/out1_"+strd_str+"."+hh+".png \
					./processing_his_cimss/cropped_wau_"+strd_str+"."+hh+".GIF ./processing_his_cimss/out2_"+strd_str+"."+hh+".png")
		os.system("convert -composite -geometry +889+0 ./processing_his_cimss/out2_"+strd_str+"."+hh+".png \
					./processing_his_cimss/cropped_wnp_"+strd_str+"."+hh+".GIF ./overlaid/overlaid_cimss_IR_"+strd_str+"."+hh+".png")

	startd = startd + deltad

# Delete intermediate files
shutil.rmtree("./processing_his_cimss")

print "Done overlaying multiple images! Thank you!"
